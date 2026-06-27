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
        with pd.ExcelWriter(output) as writer:
            self.dataframe.to_excel(writer, sheet_name="History")
            self.dataframe.to_excel(writer, sheet_name="Month_Return")
            self.dataframe.to_excel(writer, sheet_name="Resume")


            for sheet_name in ["History", "Month_Return", "Resume"]:
                worksheet = writer.sheets[sheet_name]
                
                for column in worksheet.columns:
                    worksheet.column_dimensions[column[0].column_letter].width = 20
