import pandas as pd

# --- Configuration ---
INPUT_FILE = 'data/serbian_words_cleaned_lemmatized.csv'  # The file from our previous step
OUTPUT_FILE = 'data/serbian_words_final_cleaned.csv'


# ---------------------

def serbian_cyr_to_lat(text):
    """
    A robust function to transliterate Serbian Cyrillic to Latin.
    Handles special digraphs (lj, nj, dž).
    """
    if not isinstance(text, str):
        return text

    # Dictionary for standard characters
    cyr_to_lat_map = {
        'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'ђ': 'đ', 'е': 'e',
        'ж': 'ž', 'з': 'z', 'и': 'i', 'ј': 'j', 'к': 'k', 'л': 'l', 'м': 'm',
        'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'ћ': 'ć',
        'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'č', 'ш': 'š',
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Ђ': 'Đ', 'Е': 'E',
        'Ж': 'Ž', 'З': 'Z', 'И': 'I', 'Ј': 'J', 'К': 'K', 'Л': 'L', 'М': 'M',
        'Н': 'N', 'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'Ћ': 'Ć',
        'У': 'U', 'Ф': 'F', 'Х': 'H', 'Ц': 'C', 'Ч': 'Č', 'Ш': 'Š'
    }

    # Special handling for digraphs (lj, nj, dž)
    digraph_map = {
        'љ': 'lj', 'њ': 'nj', 'џ': 'dž',
        'Љ': 'Lj', 'Њ': 'Nj', 'Џ': 'Dž'
    }

    # Handle mixed-case digraphs
    # If 'Љ' is followed by 'j', it should be 'Lj', not 'Ljj'
    # If 'Н' is followed by 'j', it should be 'Nj', not 'Njj'
    # etc.
    text = text.replace('Љj', 'Lj').replace('Њj', 'Nj').replace('Џj', 'Dž')

    trans_text = []
    i = 0
    while i < len(text):
        # Check for digraphs first
        if i + 1 < len(text) and text[i:i + 2] in digraph_map:
            trans_text.append(digraph_map[text[i:i + 2]])
            i += 2
        # Check for single character digraphs
        elif text[i] in digraph_map:
            trans_text.append(digraph_map[text[i]])
            i += 1
        # Check for standard characters
        elif text[i] in cyr_to_lat_map:
            trans_text.append(cyr_to_lat_map[text[i]])
            i += 1
        # If character is not in any map (e.g., it's already Latin, or punctuation)
        else:
            trans_text.append(text[i])
            i += 1

    return "".join(trans_text)


# --- Main execution ---
if __name__ == "__main__":
    try:
        df = pd.read_csv(INPUT_FILE)

        print(f"Loaded {len(df)} rows from '{INPUT_FILE}'.")

        # 1. Create the new 'Latin_Lemma' column
        print("Transliterating lemmas to a standard Latin script...")
        df['Latin_Lemma'] = df['Lemma'].apply(serbian_cyr_to_lat)

        # 2. Sort by length (to keep the shortest, base form)
        df_sorted = df.sort_values(by='Len')

        # 3. Drop duplicates based on the new 'Latin_Lemma' column
        df_final = df_sorted.drop_duplicates(subset=['Latin_Lemma'], keep='first')

        print("Duplicates removed based on standardized script.")

        # 4. Save the final cleaned file
        df_final.to_csv(OUTPUT_FILE, index=False, encoding='utf-8')

        print("\n--- Success! ---")
        print(f"Original lemmatized rows: {len(df)}")
        print(f"Final cleaned rows (unique lemmas, script-independent): {len(df_final)}")
        print(f"Final cleaned file saved to: {OUTPUT_FILE}")

    except FileNotFoundError:
        print(f"Error: The file '{INPUT_FILE}' was not found.")
        print("Please make sure you have run the lemmatization script first.")
    except Exception as e:
        print(f"An error occurred: {e}")