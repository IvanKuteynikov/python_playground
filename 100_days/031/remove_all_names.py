import classla
import pandas as pd
from tqdm import tqdm

# --- Configuration ---
# ⚠️ Make sure this is the input from your last script!
INPUT_FILE = 'data/serbian_words_final_popular_no_caps.csv'
OUTPUT_FILE = 'data/serbian_words_FULLY_CLEANED_FINAL.csv'
SERBIAN_COLUMN = 'Latin_Lemma'  # The standardized Serbian column
#RUSSIAN_COLUMN = 'Russian'  # The Russian column
BATCH_SIZE = 500


# ---------------------

def get_entities_for_column(df, column_name, lang_code):
    """
    Helper function to run NER on a specific column and return
    a set of all words that are named entities.
    """
    print(f"\n--- Processing Language: {lang_code.upper()} ---")

    # 1. Load the specific language pipeline
    print(f"Loading {lang_code.upper()} NLP pipeline (tokenize,pos,ner)...")
    try:
        nlp = classla.Pipeline(lang_code, processors='tokenize,pos,ner')
    except Exception as e:
        print(f"Error loading pipeline for {lang_code}: {e}")
        print(f"Please make sure you have run: classla.download('{lang_code}')")
        return None
    print(f"Pipeline for {lang_code.upper()} loaded.")

    # 2. Get unique, non-null words from the column
    df.dropna(subset=[column_name], inplace=True)
    words_to_check = df[column_name].astype(str).unique()

    print(f"Found {len(words_to_check)} unique words to check in '{column_name}'.")

    # 3. Process words in batches
    entity_words = set()  # A set to store all words that are names
    num_batches = len(words_to_check) // BATCH_SIZE + 1

    print(f"Starting NER in {num_batches} batches...")
    for i in tqdm(range(num_batches)):
        batch_words = words_to_check[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]
        if not batch_words.any():
            continue

        batch_text = "\n".join(batch_words)
        doc = nlp(batch_text)

        # Add all found entity text to our set
        for ent in doc.ents:
            entity_words.add(ent.text)

    print(f"NER check for {lang_code.upper()} finished. Found {len(entity_words)} entity words.")
    return entity_words


# --- Main execution ---
if __name__ == "__main__":
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"Loaded {len(df)} rows from '{INPUT_FILE}'.")

        # --- Step 1: Get all Serbian named entities ---
        serbian_entities = get_entities_for_column(df, SERBIAN_COLUMN, 'sr')

        # --- Step 2: Get all Russian named entities ---
        #russian_entities = get_entities_for_column(df, RUSSIAN_COLUMN, 'ru')

        if serbian_entities is None:
            print("\nExiting due to error in loading NLP models.")
            exit()

        # --- Step 3: Filter the DataFrame ---
        print("\nFiltering DataFrame based on both entity lists...")

        # Check if the Serbian word is a Serbian entity
        is_serbian_entity = df[SERBIAN_COLUMN].isin(serbian_entities)

        # Check if the Russian word is a Russian entity
        #is_russian_entity = df[RUSSIAN_COLUMN].isin(russian_entities)

        # We keep the row only if it is NOT a Serbian entity AND NOT a Russian entity
        df_cleaned = df[~is_serbian_entity] # df[~is_serbian_entity & ~is_russian_entity]

        # --- Step 4: Save the final file ---
        df_cleaned.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

        print("\n--- Success! ---")
        print(f"Original rows: {len(df)}")
        print(f"Rows after removing ALL names: {len(df_cleaned)}")
        print(f"Final file saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        print("Please make sure you have run all previous cleaning scripts.")
    except Exception as e:
        print(f"An error occurred: {e}")