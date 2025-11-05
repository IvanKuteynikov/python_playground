import pandas as pd
import numpy as np

# --- Configuration ---
INPUT_FILE = 'data/serbian_words_fully_cleaned.csv'
OUTPUT_FILE = 'data/serbian_words_no_caps.csv'

# We'll only check words longer than 2 chars.
# This prevents removing valid short words like 'A' (and) or 'У' (in).
MIN_LEN_FOR_UPPERCASE_CHECK = 1


# ---------------------

def clean_uppercase_words(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} rows from '{input_file}'.")

        # Ensure columns are strings and handle potential NaN values
        df['Serbian'] = df['Serbian'].astype(str)
        df['Russian'] = df['Russian'].astype(str)
        df['Len'] = df['Len'].fillna(0).astype(int)

        # 1. Find Serbian words that are all-caps AND longer than our minimum
        is_serbian_upper = (df['Serbian'] == df['Serbian'].str.upper()) & \
                           (df['Len'] >= MIN_LEN_FOR_UPPERCASE_CHECK)

        # 2. Find Russian words that are all-caps AND longer than our minimum
        is_russian_upper = (df['Russian'] == df['Russian'].str.upper()) & \
                           (df['Russian'].str.len() >= MIN_LEN_FOR_UPPERCASE_CHECK)

        # 3. We keep a row ONLY if both conditions are FALSE.
        #    (i.e., we remove it if EITHER is True)
        df_cleaned = df[~is_serbian_upper & ~is_russian_upper]

        # 4. Save the new file
        df_cleaned.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

        print("\n--- Success! ---")
        print(f"Original rows: {len(df)}")
        print(f"Removed {len(df) - len(df_cleaned)} rows containing all-caps words.")
        print(f"Final rows: {len(df_cleaned)}")
        print(f"Final file saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        print("Please make sure you have run 'clean_by_popularity.py' first.")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- Main execution ---
if __name__ == "__main__":
    clean_uppercase_words(INPUT_FILE, OUTPUT_FILE)