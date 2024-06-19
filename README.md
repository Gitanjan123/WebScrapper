# Web Scraper for Disease Information

## Overview

This project contains a web scraper to extract detailed information about diseases from the 1mg website.

## File Structure

- `data/`: Contains the JSON files with scraped data.
  - `disease_links.json`: List of disease names and URLs.
  - `disease_details.json`: Detailed information about each disease.
- `main.py`: Main script to run the scraping process.
- `requirements.txt`: Python dependencies.
- `utils/`: Utility scripts.
  - `scraper.py`: Functions for scraping.
  
## Setup

1. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
