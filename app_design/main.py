import argparse
import cProfile
import pstats
import io
from difflib import SequenceMatcher
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    filtered_words = [word for word in words if word.lower() not in stop_words and word.isalnum()]
    return " ".join(filtered_words)


def calculate_similarity(text1, text2):
    matcher = SequenceMatcher(None, text1, text2)
    similarity = matcher.ratio()
    return similarity


def main():
    PARSER = argparse.ArgumentParser()
    PARSER.add_argument('--sample_text', type=str, required=True)
    PARSER.add_argument('--reference_text', type=str, required=True)
    PARSER.add_argument('--test_outcome', type=str, required=True)
    ARGS = PARSER.parse_args()

    try:
        with open(ARGS.sample_text, 'r', encoding='utf-8') as file:
            SAMPLE_TEXT = file.read()
    except FileNotFoundError:
        print(f"Error: The file {ARGS.sample_text} does not exist.")
        return
    except IOError:
        print(f"Error: Could not read the file {ARGS.sample_text}.")
        return

    try:
        with open(ARGS.reference_text, 'r', encoding='utf-8') as file:
            REFERENCE_TEXT = file.read()
    except FileNotFoundError:
        print(f"Error: The file {ARGS.reference_text} does not exist.")
        return
    except IOError:
        print(f"Error: Could not read the file {ARGS.reference_text}.")
        return

    PROCESSED_SAMPLE = preprocess_text(SAMPLE_TEXT)
    PROCESSED_REFERENCE = preprocess_text(REFERENCE_TEXT)

    SIMILARITY_SCORE = calculate_similarity(PROCESSED_SAMPLE, PROCESSED_REFERENCE)
    print(f"Similarity Score: {SIMILARITY_SCORE}")

    try:
        with open(ARGS.test_outcome, 'w', encoding='utf-8') as result_file:
            result_file.write(f"Similarity Score: {SIMILARITY_SCORE:.2f}\n")
    except IOError:
        print(f"Error: Could not write to the file {ARGS.test_outcome}.")


if __name__ == "__main__":
    pr = cProfile.Profile()
    pr.enable()
    main()
    pr.disable()
    s = io.StringIO()
    sortby = 'cumulative'
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    ps.print_stats()
    print(s.getvalue())
