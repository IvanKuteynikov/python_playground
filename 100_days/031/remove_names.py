import classla
import pandas as pd
from tqdm import tqdm

# --- Configuration ---
INPUT_FILE = 'data/serbian_words_final_popular.csv'  # Input from the last step
OUTPUT_FILE = 'data/serbian_words_fully_cleaned.csv'  # The final file
COLUMN_TO_CHECK = 'Latin_Lemma'  # The standardized column
BATCH_SIZE = 500  # How many words to process at once


# ---------------------

def filter_named_entities(input_file, output_file, column_name):
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' was not found.")
        print("Please make sure you have run all previous cleaning scripts.")
        return

    # 1. Initialize the NLP pipeline with NER
    # We need 'tokenize', 'pos', AND 'ner'
    print("Loading NLP pipeline for NER (this may take a moment)...")
    try:
        nlp = classla.Pipeline('sr', processors='tokenize,pos,ner')
    except Exception as e:
        print(f"Error loading pipeline: {e}")
        print("Please ensure the Serbian ('sr') model is downloaded.")
        print("You can download it by running: classla.download('sr')")
        return
    print("Pipeline loaded.")

    # 2. Get unique words to process
    df.dropna(subset=[column_name], inplace=True)
    df[column_name] = df[column_name].astype(str)
    words_to_check = df[column_name].unique()

    print(f"Found {len(df)} total rows, {len(words_to_check)} unique words to check for names.")

    # 3. Process words in batches
    is_entity_map = {}  # Dictionary to map: word -> True (if name) or False
    num_batches = len(words_to_check) // BATCH_SIZE + 1

    print(f"Starting NER in {num_batches} batches...")

    for i in tqdm(range(num_batches)):
        batch_words = words_to_check[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]
        if not batch_words.any():
            continue

        # Join words with a newline. The pipeline will treat each as a separate doc.
        batch_text = "\n".join(batch_words)

        # Process the entire batch at once
        doc = nlp(batch_text)

        # --- NEW, SAFER METHOD ---
        # Get a set of all words that the NER processor identified as an entity.
        # This avoids accessing the .ner attribute on a word that might not have it.
        entity_texts = {ent.text for ent in doc.ents}

        # Create the mapping for this batch
        # Assume a word is NOT an entity, unless it was in the 'doc.ents' list
        for word in batch_words:
            if word in entity_texts:
                is_entity_map[word] = True  # It's a name
            else:
                is_entity_map[word] = False  # Not a name
        # --- END OF NEW METHOD ---

    print("NER check finished.")

    # 4. Map the results back to the DataFrame
    print("Mapping results back to DataFrame...")
    df['is_named_entity'] = df[column_name].map(is_entity_map)

    # 5. Filter the DataFrame
    df_cleaned = df[df['is_named_entity'] == False]

    # Drop the temporary column
    df_cleaned = df_cleaned.drop(columns=['is_named_entity'])

    # 6. Save the final, clean file
    df_cleaned.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

    print("\n--- Success! ---")
    print(f"Original rows: {len(df)}")
    print(f"Rows after removing names: {len(df_cleaned)}")
    print(f"Final file saved to: {OUTPUT_FILE}")


# --- Main execution ---
if __name__ == "__main__":
    filter_named_entities(INPUT_FILE, OUTPUT_FILE, COLUMN_TO_CHECK)