from urllib.parse import urlparse
import re
from lxml import html
import requests






'''Breadth first search is an algorithm used for tree transversal on graphs or tree data structures. BFS can be easily implemented
using recursion and data structures like dictionaries and lists.
The algorithm: 
1)Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
2)If there are no remaining adjacent vertices left, remove the first vertex from the queue.
3)Repeat step 1 and step 2 until the queue is empty or the desired node is found.'''
#the graph will be represented by an adjacency list


emails = []
def openscrape(url):
  page = requests.get(url)
  webpage = html.fromstring(page.content)
  emails.extend(list(set(re.findall(r'[\w\.-]+@+[\w\.-]+', webpage)))) #regex to search emails
  href_list = []
  links = webpage.xpath('//a/@href')
  for link in links:
    href_list.append(link.get_attribute('href'))
  driver.quit()

  return href_list
'''This function algorithm is the following:
      1) opens the url defined in the parameter
      2) scrape for emails in said url.
      3) save the emails into a global list
      4) finds all links in url, hereby defined as sons
      5) saves sons into a list '''


def localurlchecker(trial, url):
  base = urlparse('url').netloc
  test = urlparse('trial').netloc
  if base == test:
    return True
  else:
    return False

    '''This function algorithm is the following:
    We are trying to see if the child node is part of the initial url and not a large non local site such as facebook which would
    collapse out system as scraping it approximates to infinity
    1) Receives parameter (trial) which is the child node we are testing to see if it is part of the original site
    2) Receives parameter (url) which is the url from the original node from our site
    3) with netlock whe extract the most basic part of the urls
    4) we compare both netlocs, if they are true, they belong to the same site and the function returns True.
    5) in the other cases it returns false '''

def crawling(baseurl):
  graph = {}
  visited = []
  queue = []
  visited.append(baseurl)
  queue.append(baseurl)

  while queue:
    if len(emails) < emaillimit:
      try:
        s = queue.pop(0)
        openscrape(s)
        print(s)
        graph[s] = openscrape(s)
        for hijo in graph[s]:
          url_local = localurlchecker(hijo, baseurl)
          if hijo not in visited and url_local == True :
            visited.append(hijo)
            queue.append(hijo)
      except:
        continue
    else:
      break
  print(emails)







crawling('http://bathforliving.com')


