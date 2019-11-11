import os
import ebook_functions as ef
import argparse

help_text = 'This is a program to convert downloaded folders into ebooks. Please download ebook with download.py prior to using this programme.'
# initiate the parser
parser = argparse.ArgumentParser(description = help_text)
parser.add_argument("-V", "--version", help="show program version", action="store_true")
parser.add_argument("-B", "--book", help="takes in book name")

# read arguments from the command line
args = parser.parse_args()

if args.version:
    print("this is myprogram version 0.1")

if args.book:
    cwd = os.getcwd()
    book_path = os.path.join(cwd,args.book)
    if os.path.exists(book_path):
        ef.createbook(book_path)
    else:
        print("book folder does not exist")

# url_test = "https://www.wuxiaworld.com/novel/nine-star-hegemon"
# functions.get_book(url_test)
