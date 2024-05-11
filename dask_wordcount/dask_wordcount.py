import dask.bag as db
import re

from program_arguments import define_and_return_arguments

if __name__ == '__main__':

    # Get the file name as the program argument
    file_path = define_and_return_arguments()

    # Define the words length
    length = int(input("Enter the length of the words to count: "))

    # Read the text file and split it into words
    words = db.read_text(file_path).map(lambda line: line.split(" "))

    # Flatten the list of words
    words = words.flatten()

    # Function to remove special characters from a word
    def remove_special_chars(word):
        # Define regex pattern to match alphanumeric characters
        pattern = re.compile(r'\w+')
        # Use regex to find alphanumeric characters in the word
        matches = pattern.findall(word)
        # Join the matches to form the cleaned word
        cleaned_word = ''.join(matches)
        return cleaned_word

    # Remove special characters from words
    clean_words = words.map(remove_special_chars)

    # Filter words that are at least 3 characters in length
    filter_words = clean_words.filter(lambda word: len(word) >= length)

    # Disable case sensitivity
    case_sensitive = filter_words.map(lambda word: word.lower())

    # Count the occurrences of each word
    wordsCounts = case_sensitive.frequencies()

    # Convert the Bag object to a dictionary
    wordsCountsDict = dict(wordsCounts.compute())
    wordsCountsDict = dict(sorted(wordsCountsDict.items(), key=lambda item: item[1], reverse=True))

    for word, count in wordsCountsDict.items():
        print(f'({word}, {count})')
