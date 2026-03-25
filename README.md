# Books.toscrape Web Scraper & Data Analyzer

A Python project that scrapes 1,000 books from [books.toscrape.com](https://books.toscrape.com/) and performs data cleaning and basic analysis using Pandas.

## Overview

This project demonstrates a streamlined approach to web scraping and data processing. Instead of sending requests to individual book pages, it extracts all necessary data (title, price, image URL, and stock status) directly from the 50 catalogue pages. This optimization reduces total HTTP requests from 1,050 to just 50, significantly improving execution speed and reducing server load.

## Features

* **Efficient Scraping:** Uses `requests` and `BeautifulSoup` to iterate through pagination and extract HTML elements.
* **Data Export:** Saves the raw scraped data into a structured CSV file (`1000_books_data.csv`).
* **Data Cleaning:** Uses `pandas` to process the raw CSV, removing currency symbols (`£`) and encoding artifacts (`Â`), and casting string prices to float.
* **Basic Analysis:** Queries the cleaned DataFrame to find aggregate statistics and identify specific data points (e.g., locating the most expensive book in the store).

## Project Structure

* `scraper_1000.py`: The main web scraping script.
* `data_analysis.py`: The Pandas script for data cleaning and analysis.
* `1000_books_data.csv`: The generated dataset.
* `.gitignore`: Git ignore file for virtual environments and Python caches.

## How to Run

1. Clone the repository and navigate to the project directory.
2. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4 pandas
