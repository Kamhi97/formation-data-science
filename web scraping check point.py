#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1.1) Write a function to Get and parse html content from a Wikipedia page
import requests
from bs4 import BeautifulSoup

def get_html_content(url):
    # Send a request to the URL and get the response
    response = requests.get(url)

    # Parse the response using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Return the parsed HTML content
    return soup
def get_article_title(soup):
    # Find the article title element and extract the text
    title_element = soup.find('h1', {'id': 'firstHeading'})
    title = title_element.text.strip()

    # Return the article title
    return title

#1.2) Write a function to Extract article title
def get_article_title(soup):
    # Find the article title element and extract the text
    title_element = soup.find('h1', {'id': 'firstHeading'})
    title = title_element.text.strip()

    # Return the article title
    return title

#1.3) Write a function to Extract article text for each paragraph with their respective
def get_article_content(soup):
    # Find the content element and extract all the headings and paragraphs
    content_element = soup.find('div', {'class': 'mw-parser-output'})
    headings = content_element.find_all(['h2', 'h3', 'h4', 'h5', 'h6'])
    paragraphs = content_element.find_all('p')

    # Create a dictionary to store the heading-paragraph mappings
    content = {}

    # Loop through the headings and paragraphs and add them to the dictionary
    current_heading = None
    current_paragraphs = []
    for element in headings + paragraphs:
        if element.name.startswith('h'):
            # If the current heading has a name, add it to the content dictionary
            if current_heading is not None and len(current_paragraphs) > 0:
                content[current_heading] = '\n'.join(current_paragraphs)

            # Set the new heading and reset the paragraphs list
            current_heading = element.text.strip()
            current_paragraphs = []
        else:
            # Add the paragraph text to the current paragraphs list
            current_paragraphs.append(element.text.strip())

    # Add the last set of paragraphs to the content dictionary
    if current_heading is not None and len(current_paragraphs) > 0:
        content[current_heading] = '\n'.join(current_paragraphs)

    # Return the content dictionary
    return content

#headings. Map those headings to their respective paragraphs in the dictionary.

#1.4) Write a function to collect every link that redirects to another Wikipedia page
def get_internal_links(soup):
    # Find all the link elements
    link_elements = soup.find_all('a')

    # Loop through the link elements and extract the URLs that start with '/wiki/'
    links = []
    for link_element in link_elements:
        href = link_element.get('href')
        if href is not None and href.startswith('/wiki/'):
            links.append('https://en.wikipedia.org' + href)

    # Return the list of internal links
    return links

#1.5) Wrap all the previous functions into a single function that takes as parameters a Wikipedia link
def scrape_wikipedia(url):
    # Get the HTML content
    soup = get_html_content(url)

    # Get the article title
    title = get_article_title(soup)

    # Get the article content
    content = get_article_content(soup)

    # Get the internal links
    links = get_internal_links(soup)

    # Return a dictionary containing the title, content, and links
    return {
        'title': title,
        'content': content,
        'links': links
    }

#1.6) Test the last function on a Wikipedia page of your choice
url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'


# In[ ]:




