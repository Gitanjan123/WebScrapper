from utils.scraper import get_disease_links, scrape_disease_details
import json
import time
import os

# Ensure the data directory exists
os.makedirs('data', exist_ok=True)

# Step 1: Scrape disease names and URLs
disease_links = get_disease_links()

# Save the disease links to a file
with open('data/disease_links.json', 'w') as file:
    json.dump(disease_links, file, indent=2)

print("Step 1 complete: Disease names and URLs scraped.")

# Step 2: Scrape details for each disease
all_disease_details = []
for disease in disease_links:
    print(f"Scraping details for {disease['name']}")
    details = scrape_disease_details(disease['url'])
    details['name'] = disease['name']
    all_disease_details.append(details)
    time.sleep(1)  # Sleep to avoid hitting the server too hard

# Save the disease details to a file
with open('data/disease_details.json', 'w') as file:
    json.dump(all_disease_details, file, indent=2)

print("Step 2 complete: Disease details scraped.")
