import os
import download_functions as df
import argparse

help_text = 'This is a program to download ebooks based on the input url from wuxiaworld.com'

# initiate the parser
parser = argparse.ArgumentParser(description = help_text)
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-U", "--url", help="takes in novel url")

# read arguments from the command line
args = parser.parse_args()

if args.version:
    print("this is myprogram version 0.1")

if args.url:
    df.get_book(args.url)

# url_test = "https://www.wuxiaworld.com/novel/nine-star-hegemon"
# functions.get_book(url_test)
