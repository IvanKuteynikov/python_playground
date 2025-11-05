import pandas as pd

# --- Configuration ---
# The input is the file from our last step
INPUT_FILE = 'data/serbian_words_final_cleaned.csv'

# This will be our new, final file
OUTPUT_FILE = 'data/serbian_words_final_popular.csv'


# ---------------------

def clean_by_popularity(input_file, output_file):
    try:
        df = pd.read_csv(input_file)

        print(f"Loaded {len(df)} rows from '{input_file}'.")

        # We need to handle any rows that might not have a Russian translation
        df.dropna(subset=['Russian'], inplace=True)

        # 1. Sort the entire DataFrame by 'index' in ascending order
        # This makes the row with the lowest index appear first for any group
        print("Sorting by index to find most popular (lowest index) entries...")
        df_sorted = df.sort_values(by='index', ascending=True)

        # 2. Drop duplicates based on the 'Russian' column
        # By 'keeping=first', we keep the row that came first after sorting
        # which is the one with the lowest index.
        print("Removing duplicates based on Russian translation...")
        df_final = df_sorted.drop_duplicates(subset=['Russian'], keep='first')

        # 3. Save the new file
        df_final.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

        print("\n--- Success! ---")
        print(f"Original unique lemma rows: {len(df)}")
        print(f"Final 'most popular' rows: {len(df_final)}")
        print(f"Final file saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        print("Please make sure you have run the 'clean_scripts.py' script first.")
    except Exception as e:
        print(f"An error occurred: {e}")


# --- Main execution ---
if __name__ == "__main__":
    clean_by_popularity(INPUT_FILE, OUTPUT_FILE)