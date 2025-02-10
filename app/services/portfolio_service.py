import pandas as pd


def process_portfolio(filepath):
    try:
        # read the csv file
        df = pd.read_csv(filepath)

        # validate required columns
        required_columns = {
            "Stock Symbol",
            "Quantity",
            "Purchase Price",
            "Purchase Date"
        }

        # check whether required columns are present in csv file or not
        if not required_columns.issubset(df.columns):
            return {
                "error": "Missing required Columns"
            }

        # convert purchase date to datetime field or datatype
        df["Purchase Date"] = pd.to_datetime(df["Purchase Date"])

        # compute Initial Investment Per Stock
        df["Total Investment"] = df["Quantity"] * df["Purchase Price"]

        # return the dataframe as a dict
        return {
            "portfolio": df.to_dict(orient="records")
        }

    except Exception as ex:
        return {
            "error": str(ex)
        }
