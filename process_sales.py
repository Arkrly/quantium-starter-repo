import pandas as pd
import glob

# Read all CSV files in the data folder
csv_files = glob.glob('data/daily_sales_data_*.csv')
df_list = []

for file in csv_files:
    df = pd.read_csv(file)
    # Filter for pink morsel
    df = df[df['product'] == 'pink morsel']
    # Convert price: remove $ and convert to float
    df['price'] = df['price'].str.replace('$', '').astype(float)
    # Calculate sales
    df['sales'] = df['price'] * df['quantity']
    # Select and rename columns
    df = df[['sales', 'date', 'region']]
    df_list.append(df)

# Combine all dataframes
combined_df = pd.concat(df_list, ignore_index=True)

# Save to CSV
combined_df.to_csv('formatted_sales.csv', index=False)
print(f"Saved {len(combined_df)} rows to formatted_sales.csv")
