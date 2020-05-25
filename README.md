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

### List of commands
For download.py:
-V or --version || show program version
-U or --url || takes in novel url as a parameter
-S or --start || start downloading from this chapter number
-P or --path || file path to save wuxia novel  

For create_ebook.py:
-V or --version || show program version
-B or --book || takes in book name
-P or --path || file path to save wuxia novel  

### Examples with parameters
If you wish to update your previously downloaded folder with the latest chapters, run the following line:

```
python download.py --url [url_link] --start [the chapter number you wish to start downloading from]
```
for example if the last time I trawled till chapter 366, then the next time I run the code I will want to trawl from chapter 367 onwards, thus the commands to run will be the following:
```
python download.py --url [url_link] --start 367
```

If you have moved your previously trawled folder to another file location, pass in the file location as a path parameter

```
python download.py --url [url_link] --path [file path to existing trawled folder]
```

If you have shifted the folder of trawled chapters to a different file path

```
python create_ebook.py --book [book_name] --path [new file path location]
```
