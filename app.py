# TODO: Add ability to find feeds linked from an HTML page
urls = "urls.txt"

top_part = '''<?xml version="1.0" encoding="UTF-8"?>
<opml version="2.0">
    <head>
        <title>EasyOPML.com URL List</title>
    </head>
    <body>
        <outline title="News" text="News">
'''
url_part = f"template"

with open(urls) as urls:
    for url in urls:
        
