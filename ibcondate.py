import pandas as pd
from datetime import datetime

# Load your file
input_file = 'MHI_25032026_24042026_revised.txt'   # Change if needed
output_file = 'MHI_converted_DMY.txt'

df = pd.read_csv(input_file)

# Convert YYYY/M/D → D/M/YYYY
def convert_date(date_str):
    try:
        dt = datetime.strptime(date_str.strip(), '%Y/%m/%d')
        return dt.strftime('%d/%m/%Y')
    except:
        return date_str  # Keep original if error

df['Date'] = df['Date'].apply(convert_date)

# Save the result
df.to_csv(output_file, index=False)

print(f"✅ Conversion complete! Saved to: {output_file}")
print("First few dates:", df['Date'].head().tolist())
