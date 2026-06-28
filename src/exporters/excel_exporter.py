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

        
        

        with pd.ExcelWriter(output) as writer:
            self.dataframe.to_excel(writer, sheet_name="History")
            df_month.to_excel(writer, sheet_name="Month_Return")
            self.dataframe.to_excel(writer, sheet_name="Resume")


            for sheet_name in ["History", "Month_Return", "Resume"]:
                worksheet = writer.sheets[sheet_name]
                
                for column in worksheet.columns:
                    worksheet.column_dimensions[column[0].column_letter].width = 20
