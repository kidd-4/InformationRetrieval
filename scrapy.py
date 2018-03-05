from bs4 import BeautifulSoup
import robotparser
import urllib2
import os

# class LinkParser(HTMLParser):
#
#     def getLinks(self,url):
#         self.links = []
#
#
#     def spider(url,maxPages):
#         pagesToVisit = [url]
#         visited = 0
#
#         while(visited < maxPages and pagesToVisit != []):
#             url = pagesToVisit[0]
#             pagesToVisit = pagesToVisit[1:]
#
#             print(visited,"visiting: ",url)
#             parser = LinkParser()

STARTING_WEBPAGES = ["https://csu.qc.ca/content/student-groups-associations",
                     "https://www.concordia.ca/artsci/students/associations.html",
                     "http://www.cupfa.org",
                     "http://cufa.net"]

number_of_page_to_crawl = 100
crawal_per_start_page = number_of_page_to_crawl/len(STARTING_WEBPAGES)
raw_page_output_dir = '/raw_webpages'
total_crawled_pages = 0
visited_page = []
docID_to_URL = {}
user_agent = 'COMP6791'


for webpage in STARTING_WEBPAGES:
    print "Crawaling from " + str(webpage) +"\n"

    crawaled_pages = 0
    pages_to_crawal = []
    pages_to_crawal.append(webpage)

    while crawaled_pages < crawal_per_start_page and len(pages_to_crawal) >0:
        url = pages_to_crawal.pop()
        url = url.encode('utf8')

        if url in visited_page:
            print "Already visited" + str(url)
            continue
        else:
            visited_page.append(url)


        parser = robotparser.RobotFileParser()
        parser.set_url(url + "/robots.txt")

        # Try to get the robots.txt file, if none at this host, skip the website
        try:
            parser.read()
        except:
            print "Cannot find a robots.txt file at " + url + "/robots.txt"
            continue

        # Only go to pages allowed by robots.txt
        if not parser.can_fetch(user_agent,url):
            print "Cannot parse" + str(url)
            continue

        # Get content from webpage
        try:
            content = urllib2.urlopen(url).read()
        except:
            print "Cannot open contents of " + str(url)
            continue

        soup = BeautifulSoup(content,"html.parser")
        docID_to_URL[total_crawled_pages] = str(url)

        filename = raw_page_output_dir + "/" + str(total_crawled_pages) + ".txt"
        #getcwd() returns current working directory of a process.
        raw_output = open(os.getcwd()+filename,'w+')

        try:
            raw_output.write(str(soup.get_text))
        except:
            print "cannot write contents of " + str(url)
            continue

        # extract all the URLs found within a page's <a> tags
        for link in soup.find_all('a'):
            l = link.get('href')
            if l is None:
                continue
            pages_to_crawal.append(l)

        print "Parsing: " + str(url)

        crawaled_pages += 1
        total_crawled_pages +=1