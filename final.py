from urllib.parse import urlparse
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
from selenium.webdriver.chrome.options import Options


'''Breadth first search is an algorithm used for tree transversal on graphs or tree data structures. BFS can be easily implemented
using recursion and data structures like dictionaries and lists.
The algorithm: 
1)Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
2)If there are no remaining adjacent vertices left, remove the first vertex from the queue.
3)Repeat step 1 and step 2 until the queue is empty or the desired node is found.'''
#the graph will be represented by an adjacency list


emails = []

def lengthofset(setlist):
  counter = 0
  for i in set(setlist):
    counter += 1

  return counter


def openscrape(url):
  chrome_options = Options()  
  chrome_options.add_argument("--headless") 
  chrome_options.add_argument("user-agent= G.Alonso Scraper contact me if my bot is behaving intrusively: geronimoalonso@icloud.com")
  driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options) #set the search engine
  driver.get(url)
  doc = driver.page_source
  emails.extend(list(set(re.findall(r'[\w\.-]+@+[\w\.-]+', doc)))) #regex to search emails

  href_list = []
  links = driver.find_elements_by_tag_name("a")
  for link in links:
    if localurlchecker(link, url) == True:
      href_list.append(link.get_attribute('href'))
    else:
      continue
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

def crawling(baseurl, emaillimit):
  global emails 
  emails = []
  graph = {}
  visited = []
  queue = []
  visited.append(baseurl)
  queue.append(baseurl)

  while queue:
    if lengthofset(emails) < emaillimit:
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
  print(set(emails))
  with open('emails.txt', 'a') as f:
    for item in set(emails):
      f.write(item + '\n')




crawling('https://www.dentalplanet.com', 5)
crawling('https://rtechdental.com',5)
crawling('https://abcdentalworks.com',5)
crawling('https://www.useddentalequipment.net',5)
crawling('https://www.atlasresell.com',5)
crawling('https://qualitydentalequip.com',5)
crawling('https://www.recycledental.com',5)
crawling('https://bimedis.com',5)
crawling('https://dentalequipmentused.net',5)
crawling('https://www.dentaltown.com',5)
crawling('https://dentalequipmentused.net',5)
crawling('https://dentalequipmentused.net',5)
crawling('https://www.renewdigital.com',5)
crawling('https://dentalequipmentused.net',5)
crawling('https://superdentalusa.com',5)
crawling('https://www.servi-dent.com',5)




