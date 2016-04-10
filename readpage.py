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
text = soup.get_text()
name = "/tmp/" + str(random.random() * (10**15)) + ".txt"

f = open(name, 'w')
print(text, file=f)
f.close()
execute_unix("espeak -f %s -s 390 -w %s" % (name, name + ".wav"))

execute_unix("xdg-open %s" % name + ".wav")
