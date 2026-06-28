import pandas as pd
from pathlib import Path
import openpyxl

output = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "working"
    / "stock_analysis.xlsx"
)

class ExcelExporter():
    def __init__(self, dataFrame):
        self.dataframe = dataFrame

    def CreateSheetStructure(self):

        df = self.dataframe.reset_index()
        df = df.rename(columns={'level_0':'Ticker'})
        df_month = df.groupby("Ticker").resample("ME", on="Date")["Close"].last()
        df_month = df_month.pct_change()
        df_month.index = df_month.index.set_levels(df_month.index.levels[1].date, level=1)

        df_resume = df.groupby("Ticker").agg({
            "Close": ["first", "last", "min", "max"],
            "Volatility": "median"
})
        df_resume["Rise"] = (
            df_resume[("Close", "max")] / df_resume[("Close", "min")] - 1
        ) * 100

        df_resume["Lower"] = (
            df_resume[("Close", "min")] / df_resume[("Close", "max")] - 1
        ) * 100

        df_resume["Total_Return"] = (
            df_resume[("Close", "last")] / df_resume[("Close", "first")] - 1
        ) * 100

        df_resume.columns = df_resume.columns.set_levels(
            df_resume.columns.levels[1].str.capitalize(), level=1
        )

        with pd.ExcelWriter(output) as writer:
            self.dataframe.to_excel(writer, sheet_name="History")
            df_month.to_excel(writer, sheet_name="Month_Return")
            df_resume.to_excel(writer, sheet_name="Resume")


            for sheet_name in ["History", "Month_Return", "Resume"]:
                worksheet = writer.sheets[sheet_name]
                
                for column in worksheet.columns:
                    try:
                        worksheet.column_dimensions[column[0].column_letter].width = 20
                    except AttributeError:
                        pass