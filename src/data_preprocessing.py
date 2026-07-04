import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    """
    Load the dataset and remove the Id column.
    """
    df = pd.read_csv(file_path)

    if "Id" in df.columns:
        df.drop("Id", axis=1, inplace=True)

    return df


def preprocess_data(df):
    """
    Split the dataset into features and target.
    """
    X = df.drop("quality", axis=1)
    y = df["quality"]

    return X, y


def split_data(X, y):
    """
    Split the dataset into training and testing sets.
    """
    return train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )


def scale_data(X_train, X_test):
    """
    Scale numerical features using StandardScaler.
    """
    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, scaler