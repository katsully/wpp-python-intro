import requests

# get the html for this webpage 
page = requests.get("https://dataquestio.github.io/web-scraping-pages/simple.html")
# this will return an HTML document that is pretty tricky to decipher
# in the next example we'll use the BeautifulSoup library to help
print(page.content)
