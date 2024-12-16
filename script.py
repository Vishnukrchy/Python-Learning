import pandas as pd

# Load the CSV file
file_path = 'Untitled spreadsheet - Sheet1.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Ensure the column names match the CSV file
db_trade_list = data['dbTrade'].dropna().tolist()  # Replace with the exact column name for dbTrade
new_trade_list = data['newTrade'].dropna().tolist()  # Replace with the exact column name for newTrade

# Exact matches
exact_matches = [trade for trade in new_trade_list if trade in db_trade_list]

# Not available in dbTrade
not_available = [trade for trade in new_trade_list if trade not in db_trade_list]

# Similar trades (partial matches)
similar_trades = [
    trade for trade in new_trade_list
    if any(trade.lower() in db_item.lower() for db_item in db_trade_list)
]

# Find the maximum length among the lists
max_length = max(len(exact_matches), len(not_available), len(similar_trades))

# Pad the lists with None to make them the same length
exact_matches += [None] * (max_length - len(exact_matches))
not_available += [None] * (max_length - len(not_available))
similar_trades += [None] * (max_length - len(similar_trades))

# Create a DataFrame to save results
results_df = pd.DataFrame({
    'Exact Matches': exact_matches,
    'Not Available': not_available,
    'Similar Trades': similar_trades
})

# Save results to a CSV file
output_file_path = 'comparison_results.csv'  # Specify your desired output file name
results_df.to_csv(output_file_path, index=False)

# Print results to console
print("=== Exact Matches ===")
print(exact_matches)
print("\n=== Not Available ===")
print(not_available)
print("\n=== Similar Trades ===")
print(similar_trades)

print(f"\nResults have been written to {output_file_path}")
