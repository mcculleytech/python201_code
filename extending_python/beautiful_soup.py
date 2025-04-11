import requests
from bs4 import BeautifulSoup

page = requests.get("https://247ctf.com/scoreboard")
print(page.text)

soup = BeautifulSoup(page.content, "html.parser")

print(soup.text)

print(soup.title)
print(soup.title.name)
print(soup.title.string)

print(soup.find("a"))

for line in soup.find_all("a"):
	print(line)

print(soup.find(id="fetch-error"))
print(soup.find(class_="nav-link"))
print(soup.find("a", class_="nav-link"))

table = soup.find("table")
#print(table)
table_body = table.find("tbody")
rows = table_body.find_all("tr")

for row in rows:
	# print("---")
	# print(row)
	cols = [x.text.strip() for x in row.find_all("td")]
	# print(cols)
	print("{} is in place with {} points".format(cols[2], cols[0], cols[4]))
