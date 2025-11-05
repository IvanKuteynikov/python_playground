import classla
import pandas as pd

# --- Configuration ---
INPUT_FILE = 'data/50k popular serbian words - data.csv'
OUTPUT_FILE = 'data/serbian_words_cleaned_lemmatized.csv'
COLUMN_TO_CLEAN = 'Serbian' # The name of the column with Serbian words
BATCH_SIZE = 1000 # How many words to process at once
# ---------------------

def lemmatize_dataframe(df, column_name):
    """
    Lemmatizes a specific column in the DataFrame using batch processing.
    """
    # 1. Initialize the NLP pipeline
    # We use 'tokenize', 'pos' (Part-of-Speech), and 'lemma'
    # POS tagging helps the lemmatizer be more accurate.
    print("Loading NLP pipeline (this may take a moment)...")
    nlp = classla.Pipeline('sr', processors='tokenize,pos,lemma')
    print("Pipeline loaded.")

    # 2. Get unique words to process (avoids duplicate work)
    df.dropna(subset=[column_name], inplace=True)
    df[column_name] = df[column_name].astype(str)
    unique_words = df[column_name].unique()

    print(f"Found {len(df)} total rows, {len(unique_words)} unique words to lemmatize.")

    # 3. Process words in batches (much faster than one by one)
    lemmas = {} # Dictionary to map: word -> lemma
    num_batches = len(unique_words) // BATCH_SIZE + 1

    print(f"Starting lemmatization in {num_batches} batches...")

    for i in range(num_batches):
        batch_words = unique_words[i*BATCH_SIZE : (i+1)*BATCH_SIZE]
        if not batch_words.any():
            continue

        # Join words with a newline. The pipeline will treat each as a separate item.
        batch_text = "\n".join(batch_words)

        # Process the entire batch at once
        doc = nlp(batch_text)

        # Extract the lemmas
        # We expect one sentence (and one word) for each word we put in.
        lemmatized_words = [s.words[0].lemma for s in doc.sentences if s.words]

        # Create the mapping for this batch
        for original_word, lemma in zip(batch_words, lemmatized_words):
            lemmas[original_word] = lemma

        print(f"  Batch {i+1}/{num_batches} complete.")

    print("Lemmatization finished.")

    # 4. Map the lemmas back to the original DataFrame
    print("Mapping lemmas back to DataFrame...")
    df['Lemma'] = df[column_name].map(lemmas)
    return df

def clean_duplicates(df):
    """
    Sorts by length and removes duplicates based on the 'Lemma' column.
    """
    print("Cleaning duplicates...")

    # 1. Sort by length ('Len' column)
    # This helps ensure that the word we keep is the shortest,
    # which is often the base form (e.g., "човек" instead of "човека").
    df_sorted = df.sort_values(by='Len')

    # 2. Drop duplicates based on the 'Lemma', keeping the first (shortest) one
    df_cleaned = df_sorted.drop_duplicates(subset=['Lemma'], keep='first')

    return df_cleaned

# --- Main execution ---
if __name__ == "__main__":
    try:
        df = pd.read_csv(INPUT_FILE)

        # Step 1: Lemmatize
        df_lemmatized = lemmatize_dataframe(df, COLUMN_TO_CLEAN)

        # Step 2: Clean duplicates
        df_final = clean_duplicates(df_lemmatized)

        # Step 3: Save the result
        df_final.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

        print("\n--- Success! ---")
        print(f"Original rows: {len(df)}")
        print(f"Cleaned rows (unique lemmas): {len(df_final)}")
        print(f"Cleaned file saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
