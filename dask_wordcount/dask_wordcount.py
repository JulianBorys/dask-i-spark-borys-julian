import dask.bag as db
import os

from program_arguments import define_and_return_arguments
from load_words_dictionary import load_word_dictionary

if __name__ == '__main__':

    # Get the file name as the program argument
    file_path = define_and_return_arguments()

    # Load the words dictionary
    words_dictionary = load_word_dictionary()

    # Convert the dictionary to a set for efficient lookup
    words_set = set(words_dictionary)

    # Read the text file and split it into words
    words = db.read_text(file_path).map(lambda line: line.split(" "))

    # Flatten the list of words
    words = words.flatten()

    # Filter words that are at least 3 characters in length
    filter_words = words.filter(lambda word: len(word) >= 3)

    # Filter words that are in the dictionary
    filtered_words = filter_words.filter(lambda word: word in words_set)

    # Count the occurrences of each word
    wordsCounts = filtered_words.frequencies()

    # Convert the Bag object to a dictionary
    wordsCountsDict = dict(wordsCounts.compute())
    wordsCountsDict = dict(sorted(wordsCountsDict.items(), key=lambda item: item[1], reverse=True))
    
    # Define the output path
    output_path = "output"

    # Check if the output directory exists
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Save the word counts to a text file
    with open(os.path.join(output_path, 'word_counts.txt'), 'w') as f:
        for word, count in wordsCountsDict.items():
            f.write(f"{word}: {count}\n")