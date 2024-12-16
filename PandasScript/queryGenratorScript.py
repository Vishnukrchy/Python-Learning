import csv
import sys

def generate_insert_queries(input_file, start_id):
    # Open the CSV file containing new trades (assuming the file is a CSV with 'master_name' as the column header)
    with open(input_file, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        trades = list(reader)

    # Start generating SQL queries for each trade
    queries = []

    # Generate an insert query for each trade in the file
    for i, trade in enumerate(trades, start=start_id):
        trade_name = trade['master_name']
        
        query = f"INSERT INTO public.master\n"
        query += f"(id, master_name, parent_id, master_type_id, logo_physical_path, logo_virtual_path, slug, active, geo_name, latitude, longitude, master_mapping, candidate_onboarding_master_type_id)\n"
        query += f"SELECT\n"
        query += f"    {i},\n"
        query += f"    '{trade_name}',\n"
        query += f"    NULL::INTEGER,\n"
        query += f"    1,\n"
        query += f"    NULL,\n"
        query += f"    NULL,\n"
        query += f"    '{trade_name}',\n"
        query += f"    true,\n"
        query += f"    '{trade_name}',\n"
        query += f"    NULL,\n"
        query += f"    NULL,\n"
        query += f"    NULL,\n"
        query += f"    50\n"
        query += f"WHERE NOT EXISTS (\n"
        query += f"    SELECT 1 FROM public.master m\n"
        query += f"    WHERE m.master_name = '{trade_name}'\n"
        query += f"    AND m.master_type_id = 1\n"
        query += f");\n"
        
        queries.append(query)
    
    # Combine all queries
    final_query = "BEGIN;\n\n" + "\n".join(queries) + "\n\nCOMMIT;\n"
    
    return final_query

def main():
    # Ensure the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python generate_sql.py <input_file> <start_id>")
        sys.exit(1)
    
    input_file = sys.argv[1]  # File containing the new trades (CSV format)
    start_id = int(sys.argv[2])  # Starting point for the ID (from command line argument)
    
    # Generate the insert queries
    sql_query = generate_insert_queries(input_file, start_id)
    
    # Print the generated SQL query
    print(sql_query)
    
    # Optionally, save the SQL query to a file
    with open('generated_insert_query.sql', 'w') as f:
        f.write(sql_query)
        print("SQL query has been written to 'generated_insert_query.sql'.")

if __name__ == "__main__":
    main()
