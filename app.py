# accept list of URLs as input
# the 'validators' package is one possible option
import validators

# for all our URL request handling
import requests

# for DOM handling
from bs4 import BeautifulSoup

# File containing our URLs
urls = 'urls.txt'

# TODO: Add functionality that checks if URL is an RSS feed;
# if not, search URL response body for the feed URL. This can
# be a relative or absolute path, so need to account for both.
# It can also be extensionless (/feed/) or have an extension
# (/feed/rss.xml). Should be able to confirm type based on HTTP
# response.

# Loop through list of URLs
with open(urls) as urls:
    for url in urls:
        try:
            # Request each URL and get the content type from the response
            r = requests.get(url)
            content_type = r.headers.get('content-type')
            print(content_type)

            # If the URL is text/html, we need to do some additional work
            if ("text/html" in content_type):

                # Turn the response into a BeautifulSoup object for
                # ease of processing/searching
                soup = BeautifulSoup(r.text, 'html.parser')
                print(soup)

                # Get all elements with type of rss+xml
                links = soup.find_all(type="application/rss+xml")
                print(links)
            elif ("application/xml" in content_type):
                print("XML file")
        except requests.exceptions.MissingSchema:
            print('No scheme on URL')
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)
        

# handle errors, if any

# if it checks out, generate the "meat" of the OPML file

# finally, export the output - an OPML file.