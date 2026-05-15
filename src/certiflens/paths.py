"""Utility module for managing file paths in the project."""
from pathlib import Path


def get_project_root() -> Path:
    """Get the root directory of the project."""
    # Get the root by going up from src/certiflens to the project root
    return Path(__file__).parent.parent.parent


def get_data_dir() -> Path:
    """Get the data directory path."""
    return get_project_root() / "data"


def get_raw_data_dir() -> Path:
    """Get the raw data directory path."""
    return get_data_dir() / "raw"


def get_raw_file_path(provider: str) -> Path:
    """Get the path for a raw data file."""
    return get_raw_data_dir() / f"raw_{provider}_certifications.json"


def get_raw_final_data_path() -> Path:
    """Get the path for the raw final data file."""
    return get_raw_data_dir() / "raw_final_data.json"


def get_pre_predictions_data_path() -> Path:
    """Get the path for the pre-predictions data file."""
    return get_data_dir() / "pre_predictions_data.csv"


def get_post_predictions_data_path() -> Path:
    """Get the path for the post-predictions data file."""
    return get_data_dir() / "post_predictions_data.csv"


if __name__ == "__main__":
    print(f"Project root: {get_project_root()}")
    print(f"Data dir: {get_data_dir()}")
    print(f"Raw data dir: {get_raw_data_dir()}")
