import requests
from bs4 import BeautifulSoup

link = input('Link:\t')
tag = input('Tag:\t')
page = requests.get(link)
soup = BeautifulSoup(page.content, "html.parser")

all_elems = soup.find_all("div", class_="thing text-text")

ls_to_text_ls = lambda x : [y.text for y in x]
word_ls = [ls_to_text_ls(elem.find_all("div", class_="text")) for elem in all_elems]

with open(f'../temp/memrise-{link.split("/")[-3].split("-")[-1]}-level-{link.split("/")[-2]}.md','w', encoding='utf-8') as file:
  file.write(f'# _0. Korean Sentences\n\n')
  for word in word_ls:
    tup = (word[0],word[-1])
    file.write(f'## {tup[0]}\n')
    file.write(f'{tup[1]}\n[{tag}]()\n\n')
    file.write(f'## {tup[1]}\n')
    file.write(f'{tup[0]}\n[{tag}]()\n\n')
  file.close()

