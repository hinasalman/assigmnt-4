# Web Scraping and Data Processing Script

## Overview

This Python script performs web scraping and data processing tasks, including:

- Reading and writing CSV files
- Filtering data based on a keyword
- Sorting data alphabetically (ascending or descending)
- Saving data as an Excel file
- Scraping image URLs from a given website

## Dependencies

Before running the script, ensure you have the following Python libraries installed:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Features & Functions

### 1. Read CSV File

**Function:** `read_csv(filename)`  
Reads data from a CSV file and returns a list of dictionaries.

### 2. Write Data to CSV

**Function:** `write_csv(data, filename)`  
Writes the given data to a CSV file.

### 3. Save Data as an Excel File

**Function:** `save_as_excel(data, filename="output.xlsx")`  
Saves the given data into an Excel (.xlsx) file.

### 4. Filter Data by Keyword

**Function:** `filter_data(data, keyword)`  
Filters the data based on a user-defined keyword.

### 5. Sort Data Alphabetically

**Function:** `sort_data(data, order="asc")`  
Sorts data based on the 'text' field in either ascending or descending order.

### 6. Scrape Images from a Website

**Function:** `scrape_images(url)`  
Extracts image URLs from the provided webpage and saves them to a CSV file.

## How to Use

1. Run the script and enter the CSV file name.
2. Enter a keyword (optional) to filter data.
3. Choose whether to sort data in ascending or descending order.
4. Decide if you want to save the filtered data as a CSV or Excel file.
5. Provide a website URL if you want to scrape image URLs.

## Output Files

- `filtered_data.csv`: Contains filtered and sorted data.
- `output.xlsx`: The same data saved in an Excel file.
- `images.csv`: List of scraped image URLs.

## Author

Developed by Hina. 🚀
