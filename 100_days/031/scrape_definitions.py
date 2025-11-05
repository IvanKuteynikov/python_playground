import pandas as pd
import time
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# --- Configuration ---
INPUT_FILE = 'data/serbian_words_final_lowercase_only.csv'
OUTPUT_FILE = 'data/serbian_words_scraped_definitions.csv'

COLUMN_TO_DEFINE = 'Latin_Lemma'

# 1 second is the bare minimum.
POLITE_DELAY = 1.0


# ---------------------

def get_serbian_definition(word):
    """
    Scrapes the sh.wiktionary.org page for a word's definition.
    This is fragile and depends on the website's HTML structure.
    """
    url = f"https://sh.wiktionary.org/wiki/{word}"

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=5)

        if response.status_code != 200:
            return None  # Page doesn't exist

        soup = BeautifulSoup(response.text, 'html.parser')

        # --- THIS IS THE CORRECTED LOGIC ---

        # 1. Find the <h2> tag with the ID, not a <span>
        serbian_heading = soup.find('h2', {'id': 'Srpskohrvatski'})
        if not serbian_heading:
            serbian_heading = soup.find('h2', {'id': 'Serbo-Croatian'})

        if not serbian_heading:
            return None  # No Serbo-Croatian section on this page

        # 2. Find the first <ol> (ordered list) *after* this heading.
        for sibling in serbian_heading.find_next_siblings():

            # If we hit another <h2>, we've gone too far
            if sibling.name == 'h2':
                break

            # If we find an ordered list, that's our definitions
            if sibling.name == 'ol':
                first_definition = sibling.find('li')
                if first_definition:
                    # Get the clean text, as you pointed out!
                    return first_definition.get_text(strip=True).split('\n')[0]
                else:
                    return None  # Found the list, but it was empty

        return None  # Found the heading but no <ol> after it

    except Exception as e:
        print(f"  Error on '{word}': {e}")
        return None


# --- Main function ---
def scrape_all_definitions(input_file, output_file, column_name):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' was not found.")
        return

    # --- For testing, run on a small sample first! ---
    # To test the script, uncomment the next line:
    df = df.head(20)
    # ----------------------------------------------------

    definitions_list = []
    print(f"Starting to SCRAPE definitions for {len(df)} words...")
    print("This will be slow and you may see some errors.")

    for word in tqdm(df[column_name]):
        definition = get_serbian_definition(word)
        definitions_list.append(definition)
        time.sleep(POLITE_DELAY)  # <-- Be polite!

    print("Scraping complete.")

    df['Definition'] = definitions_list

    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\n--- Success! ---")
    print(f"File saved to: {output_file}")


# --- Main execution ---
if __name__ == "__main__":
    scrape_all_definitions(INPUT_FILE, OUTPUT_FILE, COLUMN_TO_DEFINE)