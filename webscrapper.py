#------------requests library------------------------

# api application programming interface
# json javascript object notation-set of key value pairs

import requests # requests library
import pprint   #pretty print

r = requests.get('https://api.dailysmarty.com/posts') # store in r variable- requests.get and then pass in the api correctly
r.json() # to view what what the json looks like
pprint.pprint(r.json()['posts'][0]) # call pprint and then called r json and the function
                                    # next lets reach out to the posts (and treated like a dictionary) call the first post with [0]
pprint.pprint(r.json()['posts'][0]['url_for_post'])  # this command will bring in the URL using 

#---------------------------------------------

#  WEB SCRAPER!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# application to go to website-scrape all content-then filter down-and only bring back links to post
# in the python repl import requests and bs4(beautiful soup) from bs4 import beautifulSoup
# then perform a get request create the variable r  r= request.get('then website') and puled it in and stored in r variable
# r.text will return everything
# now say variable soup = BeautifulSoup(r.text, 'html.parser')  # second string tells the html what to parse
# returns the full html response formatted
# variable links = soup.find_all('a')   # takes in an element from page by calling the a tags 
# for loop    # for link in links:
# print(link['href'])


import requests                   # import the requests library
from bs4 import BeautifulSoup     # then from bs4 import beautiful soup
from inflection import titleize   # to capitaleize say from the inflection library you want to import the titleize 

def title_generator(links):       # function that takes in links
    titles = []                   # titles will be returned as a list by setting it equal to an empty list here

    def post_formatter(url):            # fucntion in the generator-but passed in url
        if 'posts' in url:              # conditional if the posts in url 
            url = url.split('/')[-1]    # reassigning the string and grabbing last element-here we are removing the / using the split function--this returns a list  
            url = url.replace('-', ' ') # using replace function first what we want to replace and then with what and here we are replacing the - with blank spaces
            url = titleize(url)         # now using the titleize function to get all first words capitalized-this expects a string so pass in rul
            titles.append(url)          # filtering down the list-looping over 

    
    for link in links:                # for the link in links
        post_formatter(link["href"])   # href passes in the url here


    return titles


r = requests.get('http://www.dailysmarty.com/topics/python') # pull in the site by using the requests.get 
soup = BeautifulSoup(r.text, 'html.parser')                  # soup object and pass in the response.tet and the html parser (to access links)
links = soup.find_all('a')                                   # to find all the a tags
titles = title_generator(links)                              # call title geneerator and pass in links

for title in titles:                                         # for title in the titles print the title by looping over using for in loop
    print(title)