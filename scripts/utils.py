import os
from pathlib import Path
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm

def get_day_folders(base_path):
    return sorted([
        folder for folder in os.listdir(base_path)
        if os.path.isdir(os.path.join(base_path, folder)) and folder.startswith("2024")
    ])

def load_file_selected_columns(file, columns):
    try:
        return pd.read_parquet(file, columns=columns)
    except Exception as e:
        return None

def load_file_selected_columns(file, columns):
    try:
        # Load the parquet file
        df = pd.read_parquet(file)
        
        # Check which columns exist in the file
        existing_columns = [col for col in columns if col in df.columns]
        
        # If no required columns exist, skip this file
        if not existing_columns:
            return None
        
        # Select the existing columns and return the dataframe
        return df[existing_columns]
        
    except Exception as e:
        print(f"⚠️ Error reading {file}: {e}")
        return None

def load_all_data_selected_columns(base_path, subfolder_name, columns):
    all_files = []
    for folder in get_day_folders(base_path):
        path_pattern = Path(base_path) / folder / 'data' / 'raw' / subfolder_name
        all_files.extend(path_pattern.glob("*.parquet"))

    dfs = []
    failed_files = 0
    success_files = 0

    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(load_file_selected_columns, file, columns) for file in all_files]
        for future in tqdm(as_completed(futures), total=len(futures), desc="Loading selected columns"):
            result = future.result()
            if result is not None:
                dfs.append(result)
                success_files += 1
            else:
                failed_files += 1

    print(f"✔️ Successfully loaded {success_files} files.")
    print(f"⚠️ Skipped {failed_files} files due to missing columns.")

    return pd.concat(dfs, ignore_index=True) if dfs else None