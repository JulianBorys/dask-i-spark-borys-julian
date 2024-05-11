from pyspark import SparkConf, SparkContext

from program_arguments import define_and_return_arguments
from load_words_dictionary import load_word_dictionary

if __name__ == '__main__':
    
    # Spark configuration
    configuration = SparkConf().setMaster("local").setAppName("Spark - Word Count")
    sc = SparkContext.getOrCreate(conf=configuration)
    sc.setLogLevel('WARN')

    # Get the file name as the program argument
    file_path = define_and_return_arguments()

    # Load the words dictionary
    words_dictionary = load_word_dictionary()

    # Convert the dictionary to a set
    words_set = set(words_dictionary)

    # Read the text file and split it into words
    words = sc.textFile(file_path).flatMap(lambda line: line.split(" "))

    # Filter words that are at least 3 characters in length
    filter_words = words.filter(lambda word: len(word) >= 3)

    # Filter words that are in the dictionary
    filtered_words = filter_words.filter(lambda word: word in words_set)

    # Count the occurrences of each word
    wordsCounts = filtered_words.map(lambda word: (word, 1)).reduceByKey(lambda a,b: a + b)
    wordsCounts = wordsCounts.sortBy(lambda a: a[1], ascending=False)

    # Save the word count to a text file
    wordsCounts.saveAsTextFile("output")
    