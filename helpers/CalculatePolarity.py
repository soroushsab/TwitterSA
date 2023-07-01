import pandas as pd
import os
import importlib


def calculate_polarities(data: pd.DataFrame) -> pd.DataFrame:
    """To calculate polarity."""

    folder_path = "helpers\\SentimentAnalysisModels"

    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):  # Process only Python files
            module_path = os.path.join(folder_path, filename.split(".")[0])  # Get the full path to the module

            function_name = "auto_tag"

            module_path = module_path.replace("\\", ".")

            module = importlib.import_module(module_path)  # Import the module dynamically

            if hasattr(module, function_name):  # Check if the module has the specified function
                function = getattr(module, function_name)  # Get the function from the module

                data = function(data)  # Call the function with the provided data
                print(f"Processed data using '{module_path}.{function_name}'")

    print("Polarity calculation has finished!")
    return data
