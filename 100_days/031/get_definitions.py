import pandas as pd
import time
from wiktionaryparser import WiktionaryParser
from tqdm import tqdm

# --- Configuration ---
INPUT_FILE = 'data/serbian_words_final_lowercase_only.csv'
OUTPUT_FILE = 'data/serbian_words_with_DEFINITIONS.csv'

# This is the cleanest, standardized column to use
COLUMN_TO_DEFINE = 'Latin_Lemma'

# Time to wait between requests (in seconds).
POLITE_DELAY = 1.0  # 1 second is safer for scraping


# ---------------------

def get_definitions_from_file(input_file, output_file, column_name):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' was not found.")
        print("Please make sure you have run all the cleaning scripts first.")
        return

    # --- For testing, run on a small sample first! ---
    # To test the script, uncomment the next line:
    df = df.head(20)
    # ----------------------------------------------------

    # Initialize the parser
    parser = WiktionaryParser()

    definitions_list = []
    print(f"Starting to fetch definitions for {len(df)} words from Wiktionary...")
    print(f"This will take approximately {round((len(df) * POLITE_DELAY) / 3600, 1)} hours.")

    # Use tqdm to create a progress bar
    for word in tqdm(df[column_name]):
        try:
            # --- This is the key part ---
            # We fetch the word and specify the language 'serbian'
            # The library handles Cyrillic/Latin variants (e.g., 'srpskohrvatski')
            # We use 'sh' (Serbo-Croatian) as it's often the language code
            # used on Wiktionary for Serbian, Croatian, Bosnian.

            # Let's try 'serbian' first
            word_data = parser.fetch(word, 'serbian')

            # If 'serbian' fails, try 'serbo-croatian' which is more common
            if not word_data:
                word_data = parser.fetch(word, 'serbo-croatian')

            if not word_data:
                definitions_list.append(None)  # No entry found
                time.sleep(POLITE_DELAY)  # Still sleep so we don't hammer the server
                continue

            # --- Extract definitions ---
            # The result is a list of dictionaries, one for each Part of Speech
            formatted_defs = []
            for entry in word_data:
                if 'definitions' in entry:
                    for definition_entry in entry['definitions']:
                        pos = definition_entry.get('partOfSpeech', 'def')
                        if definition_entry['text']:
                            # Get the first definition text
                            def_text = definition_entry['text'][0].strip()
                            # Clean up the definition text (it often has extras)
                            def_text = def_text.split('\n')[0]
                            formatted_defs.append(f"({pos}) {def_text}")

            if formatted_defs:
                definitions_list.append("; ".join(formatted_defs))
            else:
                definitions_list.append(None)  # Entry found, but no definitions text

        except Exception as e:
            # Handle any other errors (network, etc.)
            print(f"Error processing word '{word}': {e}")
            definitions_list.append(None)

        # --- CRITICAL ---
        # Be polite to the server.
        time.sleep(POLITE_DELAY)

    print("Definition fetching complete.")

    df['Definition'] = definitions_list

    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\n--- Success! ---")
    print(f"File saved to: {output_file}")


# --- Main execution ---
if __name__ == "__main__":
    get_definitions_from_file(INPUT_FILE, OUTPUT_FILE, COLUMN_TO_DEFINE)