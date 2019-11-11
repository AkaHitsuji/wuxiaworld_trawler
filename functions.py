import requests
import re
import os
from bs4 import BeautifulSoup

def get_book(url_link):
    cwd = os.getcwd()
    novel_name = url_link.split("/")[-1]

    page = requests.get(url_link).text
    soup = BeautifulSoup(page, 'html.parser')

    chapters_soup = soup.find("div", class_="p-15")
    book_title = chapters_soup.find("h4").text
    book_path = os.path.join(cwd,book_title)
    create_book_folder(book_path)

    img_soup = soup.find_all("img", class_="media-object")
    download_cover(img_soup,book_path)

    cache_path = os.path.join(book_path,"chapter_list.txt")
    list_chapterUrls = generate_chapter_list(chapters_soup,cache_path,novel_name)

    for title, link in list_chapterUrls:
        download_chapter(url_link,link,book_path)

def create_book_folder(path):
    if os.path.exists(path):
        print(path+" already exists.")
    else:
        os.mkdir(path)
        print("directory at "+path+" created.")

def generate_chapter_list(chapters_soup,cache_path,novel_name):
    list_chapterUrls = []

    if os.path.exists(cache_path):
        print("cache already exists")

        #read into list
        f = open(cache_path, "r")
        lines = f.readlines()
        for line in lines:
            title = line.split(":")[0]
            link = line.split(":")[1].rstrip()
            chapter_tuple = (title, link)
            list_chapterUrls.append(chapter_tuple)
        f.close()

        #TODO: figure out how to read and update


    else:
        for a in chapters_soup.find_all('a', href=re.compile("novel/"+ novel_name)):
            chapter_title = a.text
            chapter_title = chapter_title.lstrip().rstrip()
            chapter_tuple = (chapter_title, a['href'])
            list_chapterUrls.append(chapter_tuple)

        #write into text file
        file = open(cache_path, "w", encoding="utf8")
        for title, link in list_chapterUrls:
            file.write(title + ':' + link + '\n')
        file.close

    return list_chapterUrls

def download_cover(soup,path_to_store):
    if soup is None:
        soup = ''
    else:
        soup = soup[0]['src']
        image_url = soup
    try:
        r = requests.get(image_url)
        r.raise_for_status()
        img_data = requests.get(image_url).content
        file_path = os.path.join(path_to_store,'cover_page.jpg')
        with open(file_path, 'wb') as handler:
            handler.write(img_data)
        print("Cover page downloaded")
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print(e)
        print("Cover page image was not downloaded")

def download_chapter(novel_link,url_link,storage_path):
    chapter_link = url_link.split("/")[-1]
    download_link = novel_link + "/" + chapter_link
    page = requests.get(download_link).text
    soup = BeautifulSoup(page, 'html.parser')

    # get chapter title
    chapter_title = soup.find("img", {"src": '/images/title-icon.png'}).find_next_sibling().text

    # get chapter content
    chapter_content = soup.find(id="chapter-content")
    chapter_content = chapter_content.get_text(separator='\n\n')
    chapter_content = chapter_content.replace("Previous Chapter", "").replace("Next Chapter", "")
    chapter_content = chapter_content.lstrip().rstrip()

    chapter_path = os.path.join(storage_path,chapter_title)
    with open(chapter_path, 'w', encoding="utf8") as handler:
        handler.write(chapter_content)
    print(chapter_title + " downloaded")
