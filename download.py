import os
import download_functions as df
import argparse

help_text = 'This is a program to download ebooks based on the input url from wuxiaworld.com'

# initiate the parser
parser = argparse.ArgumentParser(description = help_text)
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-U", "--url", help="takes in novel url")
parser.add_argument("-S", "--start", help="start downloading from this chapter number", type=int, default=-1)
parser.add_argument("-P", "--path", help="file path to save wuxianovel", default="NADA")

# read arguments from the command line
args = parser.parse_args()

if args.version:
    print("this is myprogram version 0.1")

if args.url and args.start and args.path:
    df.get_book(args.url, args.start, args.path)


# url_test = "https://www.wuxiaworld.com/novel/nine-star-hegemon"
# functions.get_book(url_test)
