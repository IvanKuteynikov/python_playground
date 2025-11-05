import pandas as pd
import numpy as np

# --- Configuration ---
# Input from the 'clean_scripts.py' step
INPUT_FILE = 'data/serbian_words_final_cleaned.csv'
OUTPUT_FILE = 'data/serbian_words_final_popular_no_caps.csv'

# Min length for uppercase check (to protect 'A', 'У', etc.)
MIN_LEN_FOR_UPPERCASE_CHECK = 1


# ---------------------

def clean_caps_and_find_popular(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        print(f"Loaded {len(df)} rows from '{input_file}'.")

        # --- Step 1: Remove All-Caps Words First ---

        # Ensure columns are strings and handle potential NaN values
        df['Serbian'] = df['Serbian'].astype(str)
        df['Russian'] = df['Russian'].astype(str)
        df['Len'] = df['Len'].fillna(0).astype(int)

        # Find rows where Serbian is all-caps
        is_serbian_upper = (df['Serbian'] == df['Serbian'].str.upper()) & \
                           (df['Len'] >= MIN_LEN_FOR_UPPERCASE_CHECK)

        # Find rows where Russian is all-caps
        is_russian_upper = (df['Russian'] == df['Russian'].str.upper()) & \
                           (df['Russian'].str.len() >= MIN_LEN_FOR_UPPERCASE_CHECK)

        # Keep a row ONLY if both conditions are FALSE
        df_no_caps = df[~is_serbian_upper & ~is_russian_upper]

        removed_count = len(df) - len(df_no_caps)
        print(f"Removed {removed_count} rows containing all-caps words.")

        # --- Step 2: Find Most Popular (Lowest Index) from Remaining Words ---

        print("Sorting by index to find most popular (lowest index) entries...")

        # Sort the remaining data by 'index'
        df_sorted = df_no_caps.sort_values(by='index', ascending=True)

        # Drop duplicates based on 'Russian', keeping the first (lowest index)
        df_final = df_sorted.drop_duplicates(subset=['Russian'], keep='first')

        print("Duplicates removed based on Russian translation.")

        # --- Step 3: Save the Result ---
        df_final.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

        print("\n--- Success! ---")
        print(f"Original rows: {len(df)}")
        print(f"Rows after removing caps: {len(df_no_caps)}")
        print(f"Final 'most popular' rows (no caps): {len(df_final)}")
        print(f"Final file saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        print("Please make sure you have run 'clean_scripts.py' first.")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- Main execution ---
if __name__ == "__main__":
    clean_caps_and_find_popular(INPUT_FILE, OUTPUT_FILE)