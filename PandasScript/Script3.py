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

# Similar trades (word-level matches)
similar_trades = []
for new_trade in new_trade_list:
    new_trade_words = set(new_trade.lower().split())  # Split the newTrade into individual words
    matches = []
    for db_trade in db_trade_list:
        db_trade_words = set(db_trade.lower().split())  # Split the dbTrade into individual words
        # Check if any word in new_trade matches any word in db_trade
        if new_trade_words & db_trade_words:  # Intersection of words
            matches.append(db_trade)
    similar_trades.append(", ".join(matches) if matches else None)

# Short or Long Form Matches
short_long_form = []
for new_trade in new_trade_list:
    matches = [
        db_trade for db_trade in db_trade_list
        if new_trade.lower() in db_trade.lower() or db_trade.lower() in new_trade.lower()
    ]
    short_long_form.append(", ".join(matches) if matches else None)

# Combine the data for output
results = {
    'newTrade': new_trade_list,
    'dbTrade': db_trade_list + [None] * (len(new_trade_list) - len(db_trade_list)),  # Align lengths
    'Exact Matches': exact_matches + [None] * (len(new_trade_list) - len(exact_matches)),
    'Not Available': not_available + [None] * (len(new_trade_list) - len(not_available)),
    'Similar Trades': similar_trades + [None] * (len(new_trade_list) - len(similar_trades)),
    'Short/Long Form Matches': short_long_form + [None] * (len(new_trade_list) - len(short_long_form))
}

# Create a DataFrame to save results
results_df = pd.DataFrame(results)

# Save results to a CSV file
output_file_path = 'PandasScript/comparison2_results.csv'  # Specify your desired output file name
results_df.to_csv(output_file_path, index=False)

# Print results to console
print(results_df)

print(f"\nResults have been written to {output_file_path}")
