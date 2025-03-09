import pdfplumber
import pandas as pd

# Define file path
pdf_path = r"C:\Users\hp\OneDrive\Desktop\project\data2014\Frequency-Profile-Report-for-2024-January.pdf"

# Extract text from PDF
with pdfplumber.open(pdf_path) as pdf:
    text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

# Process extracted text into structured format
lines = text.split("\n")

# Extract column headers (Days)
days = lines[1].split(">")[1].strip().split()

# Extract rows (Time Blocks and corresponding values)
data = []
for line in lines[3:]:  # Skipping first three lines (titles and headers)
    parts = line.split()
    if len(parts) == len(days) + 1:  # Ensuring correct data structure
        time_block = parts[0]
        values = parts[1:]
        data.append([time_block] + values)

# Create DataFrame
df = pd.DataFrame(data, columns=["Block"] + days)

# Save as CSV
csv_path = "frequency_profile.csv"
df.to_csv(csv_path, index=False)

# Transpose DataFrame
df_transposed = df.set_index("Block").T.reset_index()
df_transposed.columns = ["Day"] + list(df["Block"])

# Save transposed CSV
csv_transposed_path = r"C:\Users\hp\OneDrive\Desktop\project\transform_data2024\January.csv"
df_transposed.to_csv(csv_transposed_path, index=False)

print("CSV files saved successfully.")