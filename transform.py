from bs4 import  BeautifulSoup
import  os
import bs4
import nltk
import sys

scrapy_dirctory = os.getcwd() + "/raw_webpages"
output_dirctory = os.getcwd() + "/documents"

def writechildren(soup,outputfile):
    if type(soup) is bs4.element.NavigableString:
        outputfile.write(soup.encode('utf8') + "\n")
    elif type(soup) is bs4.element.Comment or type(soup) is bs4.element.Doctype:
        None
    else:
        for child in soup.children:
            writechildren(child,outputfile)




for filename in os.listdir(scrapy_dirctory):
    scrapy_file = open(scrapy_dirctory +"/" + filename,'r')
    soup = BeautifulSoup(scrapy_file,"html.parser")
    outputfile = open(output_dirctory+"/" + filename,'w+')

    # Remove Javascript and CSS
    sections_to_remove = ["script","style"]
    for child in soup.descendants:
        if child.name in sections_to_remove:
            # removes a tag or string from the tree. It returns the tag or string that was extracted
            child.extract()
    writechildren(soup,outputfile)