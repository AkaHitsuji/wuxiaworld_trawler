import os
from ebooklib import epub

def createbook(book_path):
    book = epub.EpubBook()
    book_title = book_path.split("/")[-1]

    # set metadata
    book.set_identifier('id123456')
    book.set_title(book_title + ' - EPUB generator by AkaHitsuji')
    book.set_language('en')

    # set cover image
    image_path = os.path.join(book_path,"cover_page.jpg")
    if os.path.exists(image_path):
        book.set_cover("cover_page.jpg", open(image_path, 'rb').read())
        print("cover page set")

    # retrieve chapter list and create chapters
    cache_path = os.path.join(book_path,"chapter_list.txt")
    list_chapters = []
    if os.path.exists(cache_path):
        f = open(cache_path, "r")
        lines = f.readlines()
        for line in lines:
            title = line.split("_:_")[0]
            link = line.split("_:_")[1].rstrip()
            chapter_tuple = (title, link)
            list_chapters.append(chapter_tuple)
        f.close()

    list_of_epub_chapters = []
    for title, link in list_chapters:
        chapter_filename = link.split("/")[-1]

        chapter_path = os.path.join(book_path,title)
        file = open(chapter_path, "r", encoding="utf8")
        lines = file.readlines()
        file.close()

        chapter_content = ""
        for line in lines:
            chapter_content += "<br />" + line

        epub_chapter = epub.EpubHtml(title=title, file_name=chapter_filename+".xhtml", lang="hr")
        epub_chapter.content = '<head>\n<title>' + title + '</title>\n</head>\n<body>\n<strong>' + title + '</strong>\n<p>' + chapter_content + '</p>\n</body>\n</html>'

        # add chapter
        book.add_item(epub_chapter)
        list_of_epub_chapters.append(epub_chapter)

        print(title+" added to book.")

    # define Table Of Contents
    for chap in list_of_epub_chapters:
        book.toc.append(chap)

    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # define CSS style
    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

    # add CSS file
    book.add_item(nav_css)

    # basic spine
    book.spine = ['nav']
    for chap in list_of_epub_chapters:
        book.spine.append(chap)

    # write to the file
    epub.write_epub(book_title + ' - EPUB generator by AkaHitsuji.epub', book)

    print("epub for " + book_title + " created :) Have fun reading!!!")
