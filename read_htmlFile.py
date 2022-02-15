# CODE TO READ A HTML FILE

from bs4 import BeautifulSoup

#re MODULE FOR REGULAR EXPRESSION
import re


with open("index.html", "r") as f:
    soup = BeautifulSoup(f, "html.parser")

print(soup.prettify())

tag = soup.find("p")  # TO GET A TAG
tag.string = "hello"  # MODIFYING THE CONTENTS OF THE TAG
print(tag)

# FINDING MULTIPLE TAGS AT A TIME
tags = soup.find_all(["TITLE", "p"])
print(tags)

# SEARCHING THROUGH REGULAR EXPRESSIONS

tag1 = soup.find_all(
    text=re.compile("\$.*"))  # FINDING THE TEXT AROUND A PARTICULAR LETTER(LIKE $ HERE)
print(tag1)

# WRITING A MODIFIED FILE

with open('changed.html', 'w') as file:
    file.write(str(soup))
