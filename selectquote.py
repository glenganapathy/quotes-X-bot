import csv
import random
import os

def read_quotes_from_csv(csv_file):
    quotes = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            quotes.append(row)
    return quotes

def write_quotes_to_csv(quotes, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['quote', 'author']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for quote in quotes:
            writer.writerow(quote)

def randomly_select_and_remove_quote(csv_file):
    # Read quotes from CSV into a list of dictionaries
    quotes = read_quotes_from_csv(csv_file)
    
    if not quotes:
        print("No more quotes left to select.")
        return None
    
    # Select a random quote
    selected_quote = random.choice(quotes)

    tweet = f"{selected_quote['quote']} - {selected_quote['author']}"
    
    # Remove the selected quote from the list
    quotes.remove(selected_quote)
    
    # Write the updated quotes back to the CSV file
    write_quotes_to_csv(quotes, csv_file)
    
    return tweet

# Define your CSV file path
csv_file = r'path\to\your\quotes.csv'

# Check if the CSV file exists before proceeding
if not os.path.exists(csv_file):
    print(f"Error: The file '{csv_file}' does not exist.")
    exit(0)
