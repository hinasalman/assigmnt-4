import csv
import pandas as pd
from bs4 import BeautifulSoup
import requests

def read_csv(filename):
    """Reads a CSV file and returns data as a list of dictionaries."""
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return []

def write_csv(data, filename):
    """Writes data to a CSV file."""
    if not data:
        print("⚠ No data to save!")
        return
    
    headers = data[0].keys()
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Data successfully saved as {filename}.")
    except Exception as e:
        print(f"❌ Error writing CSV: {e}")

def save_as_excel(data, filename="output.xlsx"):
    """Saves data as an Excel file."""
    try:
        df = pd.DataFrame(data)
        df.to_excel(filename, index=False)
        print(f"✅ Data successfully saved as {filename}.")
    except Exception as e:
        print(f"❌ Error saving Excel file: {e}")

def filter_data(data, keyword):
    """Filters data based on a keyword."""
    return [row for row in data if keyword.lower() in row['text'].lower()]

def sort_data(data, order="asc"):
    """Sorts data alphabetically based on the 'text' field."""
    reverse = True if order.lower() == "desc" else False
    return sorted(data, key=lambda x: x['text'], reverse=reverse)

def scrape_images(url):
    """Scrapes image URLs from a webpage."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return [{"type": "image", "url": img["src"]} for img in soup.find_all("img", src=True)]
    except Exception as e:
        print(f"❌ Error scraping images: {e}")
        return []

# Load data
csv_file = "scrape_data.csv"
data = read_csv(csv_file)

# User options
keyword = input("Enter keyword to filter data (leave blank for all): ").strip()
if keyword:
    data = filter_data(data, keyword)

sort_order = input("Sort data? (asc/desc/no): ").strip().lower()
if sort_order in ["asc", "desc"]:
    data = sort_data(data, sort_order)

save_csv = input("Save filtered data to CSV? (yes/no): ").strip().lower()
if save_csv == "yes":
    write_csv(data, "filtered_data.csv")

save_xlsx = input("Save data as Excel file? (yes/no): ").strip().lower()
if save_xlsx == "yes":
    save_as_excel(data, "output.xlsx")

# Web Scraping
website_url = input("Enter website URL to scrape images: ").strip()
if website_url:
    image_data = scrape_images(website_url)
    write_csv(image_data, "images.csv")
