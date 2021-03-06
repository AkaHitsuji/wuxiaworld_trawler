import requests
import re
import os
from bs4 import BeautifulSoup

# requests parameter for server validation
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def get_book(url_link,start_chapter,book_path):
    cwd = os.getcwd()
    novel_name = url_link.split("/")[-1]

    page = requests.get(url_link, headers=HEADERS).text
    soup = BeautifulSoup(page, 'html.parser')

    chapters_soup = soup.find("div", class_="tabbable light")
    book_title = soup.find("h2").text

    # create bookpath in curr directory if not indicated and update book_path variable
    if book_path == "NADA":
        book_path = os.path.join(cwd,book_title)
        create_book_folder(book_path)

    img_soup = soup.find_all("img", class_="media-object")
    download_cover(img_soup,book_path)

    cache_path = os.path.join(book_path,"chapter_list.txt")
    list_chapterUrls = generate_chapter_list(chapters_soup,cache_path,novel_name)

    print("the start chapter is "+str(start_chapter))
    if start_chapter == -1:
        for title, link in list_chapterUrls:
            download_chapter(url_link,link,book_path)
    else:
        if len(list_chapterUrls) < start_chapter:
            lastChapter = get_last_chapter_number(list_chapterUrls[-1][1])
            startIndex = lastChapter - start_chapter
            startIndex = list_chapterUrls.index(list_chapterUrls[-startIndex])
            start_chapter = startIndex + 1

        for title, link in list_chapterUrls[start_chapter-1:]:
            print(title,link)
            download_chapter(url_link,link,book_path)

    print("Book downloaded! Thank you for using the code Akahitsuji wrote :)")

def get_last_chapter_number(url):
    lastelement = url.split("/")[-1]
    chapNum = lastelement.split("-")[-1]
    return int(chapNum)

def create_book_folder(path):
    if os.path.exists(path):
        print(path+" already exists.")
    else:
        os.mkdir(path)
        print("directory at "+path+" created.")

def generate_chapter_list(chapters_soup,cache_path,novel_name):
    list_chapterUrls = []

    # if file exists, delete first
    if os.path.exists(cache_path):
        print("deleting existing cache")
        os.remove(cache_path)

    # write into cache at file path
    for a in chapters_soup.find_all('a', href=re.compile("novel/"+ novel_name)):
        chapter_title = a.text
        chapter_title = chapter_title.lstrip().rstrip()
        chapter_title = re.sub(r'[\\/*?:"<>|’]',"",chapter_title)
        chapter_tuple = (chapter_title, a['href'])
        list_chapterUrls.append(chapter_tuple)

    #write into text file
    file = open(cache_path, "w", encoding="utf8")
    for title, link in list_chapterUrls:
        file.write(title + '_:_' + link + '\n')
    file.close

    return list_chapterUrls

def download_cover(soup,path_to_store):
    if soup is None:
        soup = ''
    else:
        soup = soup[0]['src']
        image_url = soup
    try:
        r = requests.get(image_url, headers=HEADERS)
        r.raise_for_status()
        img_data = requests.get(image_url, headers=HEADERS).content
        file_path = os.path.join(path_to_store,'cover_page.jpg')
        if os.path.exists(file_path):
            print("cover page has already been downloaded")
        else:
            with open(file_path, 'wb') as handler:
                handler.write(img_data)
            print("Cover page downloaded")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        print("Cover page image was not downloaded")

def download_chapter(novel_link,url_link,storage_path):
    chapter_link = url_link.split("/")[-1]
    download_link = novel_link + "/" + chapter_link
    page = requests.get(download_link, headers=HEADERS).text
    soup = BeautifulSoup(page, 'html.parser')

    # get chapter title
    chapter_title = soup.find("img", {"src": '/images/title-icon.png'}).find_next_sibling().text.lstrip().rstrip()
    chapter_title = re.sub(r'[\\/*?:"<>|’]',"",chapter_title)

    # check if chapter has already been downloaded, if not, download and write
    chapter_path = os.path.join(storage_path,chapter_title)

    if os.path.exists(chapter_path):
        print(chapter_title+" has already been downloaded")
    else:
        # get chapter content
        chapter_content = soup.find(id="chapter-content")
        chapter_content = chapter_content.find_all("p")
        content = ""
        for c in chapter_content:
            content += c.text.strip() + "\n\n"

        with open(chapter_path, 'w', encoding="utf8") as handler:
            handler.write(content)
        print(chapter_title + " downloaded")