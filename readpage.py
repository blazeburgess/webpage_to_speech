#! /usr/bin/python3

import argparse
from bs4 import BeautifulSoup
import requests
import subprocess
import random

def execute_unix(inputcommand):
  p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
  (output, err) = p.communicate()
  return output


parser = argparse.ArgumentParser()
parser.add_argument("url", help="Takes one argument: the url of the page to be read.", type=str)
url = (parser.parse_args()).url

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
#text = soup.get_text()
for tag in soup.select('script'):
  tag.clear()
for tag in soup.select('style'):
  tag.clear()
for tag in soup.select('nav'):
  tag.clear()
for tag in soup.select('header'):
  tag.clear()
for tag in soup.select('footer'):
  tag.clear()
#for tag in soup.select('form'):
#  tag.clear()
for tag in soup.select('select'):
  tag.clear()

text = soup.title.string + "\n" + soup.body.getText()
name = "/tmp/" + str(random.random() * (10**15)) + ".txt"

f = open(name, 'w')
print(text, file=f)
f.close()
execute_unix("espeak -f %s -s 390 -w %s" % (name, name + ".wav"))

execute_unix("xdg-open %s" % name + ".wav")
execute_unix("rm %s %s" % (name, name + ".wav"))

