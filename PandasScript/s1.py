import pandas as pd

# Load the CSV file
file_path = 'Untitled spreadsheet - Sheet1.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Ensure the column names match the CSV file
db_trade_list = data['dbTrade'].dropna().tolist()  # Replace with the exact column name for dbTrade
new_trade_list = data['newTrade'].dropna().tolist()  # Replace with the exact column name for newTrade

# Convert both lists to lowercase for case-insensitive comparison
db_trade_lower = [trade.lower() for trade in db_trade_list]
new_trade_lower = [trade.lower() for trade in new_trade_list]

# Exact matches (case-insensitive)
exact_matches = [new_trade for new_trade in new_trade_list if new_trade.lower() in db_trade_lower]

# Not Available in dbTrade (case-insensitive)
not_available = [new_trade for new_trade in new_trade_list if new_trade.lower() not in db_trade_lower]

# Similar trades (partial matches)
similar_trades = []
for new_trade in new_trade_list:
    matches = [
        db_trade for db_trade in db_trade_list if new_trade.lower() in db_trade.lower()
    ]
    similar_trades.append(", ".join(matches) if matches else None)

# Short or Long Form Matches
short_long_form = []
for new_trade in new_trade_list:
    matches = [
        db_trade for db_trade in db_trade_list
        if new_trade.lower() in db_trade.lower() or db_trade.lower() in new_trade.lower()
    ]
    short_long_form.append(", ".join(matches) if matches else None)

# Find the maximum length among the lists
max_length = max(len(exact_matches), len(not_available), len(similar_trades), len(short_long_form))

# Pad the lists with None to make them the same length
exact_matches += [None] * (max_length - len(exact_matches))
not_available += [None] * (max_length - len(not_available))
similar_trades += [None] * (max_length - len(similar_trades))
short_long_form += [None] * (max_length - len(short_long_form))

# Create a DataFrame to save results
results_df = pd.DataFrame({
    'Exact Matches': exact_matches,
    'Not Available': not_available,
    'Similar Trades': similar_trades,
    'Short/Long Form Matches': short_long_form
})

# Save results to a CSV file
output_file_path = 'comparison1_results.csv'  # Specify your desired output file name
results_df.to_csv(output_file_path, index=False)

# Print results to console
print("=== Exact Matches ===")
print(exact_matches)
print("\n=== Not Available ===")
print(not_available)
print("\n=== Similar Trades ===")
print(similar_trades)
print("\n=== Short/Long Form Matches ===")
print(short_long_form)

print(f"\nResults have been written to {output_file_path}")
