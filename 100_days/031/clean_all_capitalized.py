import pandas as pd
import numpy as np

# --- Configuration ---
# Input from the 'clean_popular_and_caps.py' script
INPUT_FILE = 'data/serbian_words_final_popular_no_caps.csv'
OUTPUT_FILE = 'data/serbian_words_final_lowercase_only.csv'


# ---------------------

def clean_capitalized_words(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} rows from '{input_file}'.")

        # Ensure columns are strings and handle potential NaN/empty values
        df['Serbian'] = df['Serbian'].fillna('').astype(str)
        df['Russian'] = df['Russian'].fillna('').astype(str)

        # --- New Filtering Logic ---

        # 1. Find rows where the Serbian word starts with a capital
        #    We check if the first character is uppercase.
        #    .str[0] gets the first char, .isupper() checks it.
        #    We fillna(False) for any empty strings.
        is_serbian_capitalized = df['Serbian'].str[0].str.isupper().fillna(False)

        # 2. Find rows where the Russian word starts with a capital
        is_russian_capitalized = df['Russian'].str[0].str.isupper().fillna(False)

        # 3. Keep a row ONLY if both are FALSE.
        #    (i.e., we remove it if EITHER is True)
        df_cleaned = df[~is_serbian_capitalized & ~is_russian_capitalized]

        # 4. Save the new file
        df_cleaned.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

        print("\n--- Success! ---")
        print(f"Original rows: {len(df)}")
        print(f"Removed {len(df) - len(df_cleaned)} rows containing capitalized words.")
        print(f"Final rows: {len(df_cleaned)}")
        print(f"Final file saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        print("Please make sure you have run 'clean_popular_and_caps.py' first.")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- Main execution ---
if __name__ == "__main__":
    clean_capitalized_words(INPUT_FILE, OUTPUT_FILE)