import os
import csv
from collections import Counter

def read_exclusion_words(file_path):
    with open(file_path, 'r') as file:
        exclusion_words = set(word.strip().lower() for word in file)
    return exclusion_words

def process_text_files(directory, exclusion_words):
    word_count = Counter()

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(directory, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    words = line.split()
                    for word in words:
                        clean_word = ''.join(filter(str.isalpha, word)).lower()
                        if clean_word and clean_word not in exclusion_words:
                            word_count[clean_word] += 1

    return word_count

def write_to_csv(word_count, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Word', 'Count']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for word, count in word_count.items():
            writer.writerow({'Word': word, 'Count': count})

def main():
    exclusion_file = 'exclusion.txt'
    text_files_directory = 'text_files'
    output_csv = 'word_count.csv'

    exclusion_words = read_exclusion_words(exclusion_file)
    word_count = process_text_files(text_files_directory, exclusion_words)
    write_to_csv(word_count, output_csv)

if __name__ == "__main__":
    main()
