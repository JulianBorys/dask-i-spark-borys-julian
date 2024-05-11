import argparse


def define_and_return_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", metavar="file_path", type=str, help="Path to the file to count words in")
    args = parser.parse_args()
    return args.filepath


if __name__ == '__main__':
    print(define_and_return_arguments())