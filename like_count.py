from bs4 import BeautifulSoup as bs

soup = bs(open('liked_posts.html', encoding="utf8"), 'html.parser')

print("Number of posts liked  : ",len(soup.find_all('a')))
