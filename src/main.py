from extractors.extractor_yfinance import StockExtractor
from transformers.stock_transformer import StockTransformer
from exporters.excel_exporter import ExcelExporter

extractor = StockExtractor(["NVDA", "PETR4.SA", "VALE3.SA", "AMD", "TSM", "ASML", "WEGE3.SA", "MGLU3.SA", "ITUB4.SA", "^BVSP", "^SOX"], "1y")

extractor.download()

transformer = StockTransformer(extractor.data)

df = transformer.transform()

excel_export = ExcelExporter(df)

excel_export.CreateSheetStructure()

print(df)