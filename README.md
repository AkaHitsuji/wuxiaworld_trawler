# Wuxiaworld trawler
I am a big fan of many wuxiaworld novels and I wanted to learn python. But I often get frustrated that i'm not able to save the chapters for offline reading. So I used this as a  motivation to create a python script that downloads chapters and saves them into an ePub format for easy reading on my iPhone.

All content belongs to wuxiaworld and I claim no credit. This project was started for me to find a practical way to learn python and information retrieval.

## Prerequisites

You will need to have python 3 installed.

## Step-by-step Tutorial

This python script was written and tested on MacOSX and Windows10 To run first run the following line on terminal/command line.

```
pip install -r dependencies.txt
```

There are two steps to downloading and creating a ePub file for the particular novel to be downloaded:
1. Downloading the chapters into text files
2. Generating an ePub from the text files

The splitting of steps is to enable easier modifications in the future if the user wishes to generate books of different formats from the downloaded content (eg. pdf/mobi etc.). The downloaded chapters are saved within the same folder under the title of the Novel.

To download the content, run the following line

```
python download.py --url [url_link]
```

To generate the ePub, run the following line

```
python create_ebook.py --book [book_name]
```


### Work in progress
