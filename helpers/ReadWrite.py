import pandas as pd


def save_data_frame(data: pd.DataFrame, address: str = "", name: str = "TwitterSA") -> None:
    """To save the csv."""
    data.to_csv(address + name + ".csv", index=False)


def read_data_frame(name: str, address: str = "") -> pd.DataFrame:
    """To read the csv."""
    return pd.read_csv(address + name)
