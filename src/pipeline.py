import pandas as pd

class DataAnalyzer:
    def __init__(self, path: str):
        self.path = path
        self.df   = None

    def load_csv(self) -> pd.DataFrame:
        self.df = pd.read_csv(
            self.path,
            dtype = {
                "InvoiceNo" : "string",
                "StockCode" : "string",
                "CustomerID": "string"
            },
            parse_dates=["InvoiceDate"]
        )

        return self.df

    def missing_summary(self) -> pd.DataFrame:
        if self.df is None: raise ValueError("데이터가 로드되지 않았습니다.")
        
        result = pd.DataFrame({
            "count"  : self.df.isna().sum(),
            "percent": self.df.isna().mean() * 100
        })

        return result

    def handle_missing_values(self) -> pd.DataFrame:
        if self.df is None: raise ValueError("데이터가 로드되지 않았습니다.")

        required = [
            "InvoiceNo", "StockCode", "InvoiceDate",
            "Quantity" , "UnitPrice"
        ]

        self.df = self.df.dropna(subset=required).copy()
        self.df["Description"] = self.df["Description"].fillna("Unknown")

        return self.df

    def get_sales_data(self) -> pd.DataFrame:
        if self.df is None: raise ValueError("데이터가 로드되지 않았습니다.")

        mask = (
            (self .df["Quantity"]  > 0) &
            (self .df["UnitPrice"] > 0) &
            (~self.df["InvoiceNo"].str.startswith("C", na=False))
        )

        result = self.df.loc[mask].copy()
        result["Revenue"] = result["Quantity"] * result["UnitPrice"]

        return result

    def detect_outliers(
        self, column: str, 
        data: pd.DataFrame
    ) ->      pd.DataFrame:

        q1  = data[column].quantile(0.25)
        q3  = data[column].quantile(0.75)
        iqr = q3 - q1

        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr

        mask = (data[column] < lower) | (data[column] > upper)
        return data.loc[mask].copy()