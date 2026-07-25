import pandas as pd

def load_data(file_path):

    df = pd.read_csv(
        file_path,
        parse_dates=["datetime"]
    )

    df.set_index("datetime", inplace=True)

    return df