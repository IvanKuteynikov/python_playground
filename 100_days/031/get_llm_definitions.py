import pandas as pd
import time
from openai import OpenAI
import os
from tqdm import tqdm

# --- Configuration ---
INPUT_FILE = 'data/serbian_words_final_lowercase_only.csv'
OUTPUT_FILE = 'data/serbian_words_LLM_definitions_v2.csv'
COLUMN_TO_DEFINE = 'Latin_Lemma'
POLITE_DELAY = 1.0  # Delay to respect API rate limits


# ---------------------

def get_llm_definition(client, word):
    """
    Asks an LLM for a high-quality, English-only definition.
    """

    # --- 1. THE NEW, BETTER PROMPT ---
    prompt = f"""
    Provide a short, one-sentence dictionary definition **in Russian** for the Serbian word: '{word}'.

    Rules:
    1. The definition must be in **Russian only**.
    2. Do not include the original Serbian word or any other language in your response.
    3. Start the definition directly.
    4. If the word is a proper name, pronoun, conjunction, or you don't know a definition, respond with the: "Не знаю определения"
    """

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a precise, helpful, multilingual dictionary.",
                },
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            # --- 2. THE NEW, BETTER MODEL ---
            model="gpt-4o-mini",  # Faster, cheaper, and smarter than gpt-3.5
            temperature=0.0  # We want factual, non-creative answers
        )

        definition = chat_completion.choices[0].message.content

        # Check if the model followed our "None" rule
        if "None" in definition or len(definition) > 200:
            return None
        return definition

    except Exception as e:
        print(f"  Error on '{word}': {e}")
        return None


# --- Main function (mostly the same) ---
def get_all_llm_definitions(input_file, output_file, column_name):
    # 1. Get API key from your computer's environment
    try:
        api_key = os.environ["OPENAI_API_KEY"]
        if not api_key:
            raise KeyError
    except KeyError:
        print("Error: OPENAI_API_KEY environment variable not set.")
        print("Please set your API key before running.")
        return

    # 2. Initialize the client
    client = OpenAI(api_key=api_key)

    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' was not found.")
        return

    #df = df.head(20) # For testing

    definitions_list = []
    print(f"Starting to get LLM definitions for {len(df)} words...")

    for word in tqdm(df[column_name]):
        definition = get_llm_definition(client, word)
        definitions_list.append(definition)
        time.sleep(POLITE_DELAY)

    print("LLM definitions complete.")

    df['Definition'] = definitions_list
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"\n--- Success! ---")
    print(f"File saved to: {output_file}")


# --- Main execution ---
if __name__ == "__main__":
    get_all_llm_definitions(INPUT_FILE, OUTPUT_FILE, COLUMN_TO_DEFINE)
