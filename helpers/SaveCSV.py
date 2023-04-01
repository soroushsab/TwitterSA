import pandas as pd


def save_data_frame(data: pd.DataFrame, address: str = "", name: str = "TwitterSA") -> None:
    """To save the csv."""
    data.to_csv(address + name + ".txt")
