from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, split, explode, col, length

from program_arguments import define_and_return_arguments

if __name__ == '__main__':
    
    # Spark configuration
    configuration = SparkSession.builder.appName("Word Count").getOrCreate()

    # Get the file name as the program argument
    file_path = define_and_return_arguments()

    # Read the text file
    df = configuration.read.text(file_path)

    words = df.select(explode(split(lower(col("value")), r"\s+")).alias("word"))

    # Define the words length
    min_length = int(input("Enter the length of the words to count: "))

    # Filter words that are at least 'length' characters in length
    filter_words = words.filter(length(col("word")) >= min_length)

    word_counts = filter_words.groupBy("word").count()

    sorted_word_counts = word_counts.orderBy(col("count").desc())

    for word, count in sorted_word_counts.collect():
        print(f'({word}, {count})')

    configuration.stop()
    