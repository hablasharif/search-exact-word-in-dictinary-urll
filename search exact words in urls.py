import pandas as pd
import re

# Define the path to your CSV file
csv_file_path = r"C:\Users\style\Downloads\Modified URLs.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Define the list of words to search for
search_words = ["shit"]

# Combine the search words into a single regex pattern allowing for specified delimiters or word boundaries
delimiters = r'(?:[ //./-/_\s])'
search_pattern = '|'.join([rf'((?<!\w){word}(?!\w)|{delimiters}{word}{delimiters})' for word in search_words])

# Function to check if a line contains any of the search words
def contains_search_words(line):
    return bool(re.search(search_pattern, line, re.IGNORECASE))

# Check each row in the DataFrame for the search words and print matching lines
matching_lines = df[df.apply(lambda row: any(contains_search_words(str(cell)) for cell in row), axis=1)]

# Print the matching lines
if not matching_lines.empty:
    for index, row in matching_lines.iterrows():
        print(row.to_string())
else:
    print("No matching lines found.")
