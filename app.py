# accept list of URLs as input
# the 'validators' package is one possible option
import validators

# validate input and check for errors
# here's a bad URL
url1 = "lksjdflkjsdlkfjslkdfjlksjdf"

# and here's a good URL
url2 = "http://www.theverge.com/rss/index.xml"

print("Valid URL!" if validators.url(url1) else "Invalid URL!")
print("Valid URL!" if validators.url(url2) else "Invalid URL!")

# handle errors, if any

# if it checks out, generate the "meat" of the OPML file

# finally, export the output - an OPML file.