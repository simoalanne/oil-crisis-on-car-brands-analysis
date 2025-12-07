import pandas as pd

# Adjust the file path as necessary
FILE_PATH = "data/car-data.csv"
# All columns that are suppposed to be present in the CSV file
REQUIRED_COLUMNS = [
    "fuel_consumption",
    "cylinders",
    "displacement_l",
    "hp",
    "weight_kg",
    "acceleration",
    "year",
    "origin",
    "brand",
    "model",
]


def load_car_data():
    """Loads car data from a CSV file, ensuring required columns are present."""
    data = pd.read_csv(FILE_PATH, on_bad_lines="skip")
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in data.columns]

    # if any required columns are missing, raise an error because the program won't function correctly
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    return data
