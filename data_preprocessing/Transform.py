import pandas as pd

# Define file paths
file_paths = {
    "01": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\January.csv",
    "02": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\February.csv",
    "03": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\March.csv",
    "04": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\April.csv",
    "05": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\May.csv",
    "06": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\June.csv",
    "07": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\July.csv",
    "08": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\August.csv",
    "09": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\September.csv",
    "10": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\October.csv",
    "11": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\November.csv",
    "12": r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\December.csv"
}

# List to store DataFrames
df_list = []

for month, path in file_paths.items():
    try:
        # Read CSV file
        df = pd.read_csv(path)
        
        # Rename "Day" column to "Date" and format as DD-MM-YYYY
        df.rename(columns={"Day": "Date"}, inplace=True)
        df["Date"] = df["Date"].astype(str).str.zfill(2) + f"-{month}-2024"  # Assuming year 2024
        
        # Append to list
        df_list.append(df)
    except FileNotFoundError:
        print(f"File not found: {path}, skipping...")
    except Exception as e:
        print(f"Error reading {path}: {e}, skipping...")

# Merge all DataFrames
if df_list:
    merged_df = pd.concat(df_list, ignore_index=True)
    
    # Save the merged CSV
    merged_csv_path = r"C:\Users\hp\OneDrive\Desktop\project\transformed_data2024\merged_frequency_profile.csv"
    merged_df.to_csv(merged_csv_path, index=False)
    print(f"Merged CSV saved as {merged_csv_path}")
else:
    print("No valid CSV files found for merging.")