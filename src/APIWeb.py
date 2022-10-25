import re
import pandas as pd
import numpy as np
import pandas as pd
from pandas import json_normalize
import requests 
import json
import os
from dotenv import load_dotenv
import time


def myRequests(url):
    response = requests.get(url)
    response.json()["data"]
    charac_info = response.json()    
    return charac_info


def superpowers(row):  
    if "superhuman" in row['superpowers']:
        return 'superhuman'
    elif "magnetism" in row['superpowers']:
        return 'magnetism'
    elif "pathy" in row['superpowers']:
        return 'telepathy'
    elif "invisibility" in row['superpowers']:
        return 'invisibility'
    elif "flight" in row['superpowers']:
        return 'flight'    
    else:
        return 'others'


import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
import numpy as np

def getLinks(url):
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    products = soup.find_all("div", attrs={"class":"wikibase-snakview-value wikibase-snakview-variation-valuesnak"})
    for item in range(len(products)):
        if products[item].getText() == "male":
            return "male"
        elif products[item].getText() == "female":
            return "female"
        else:
            pass