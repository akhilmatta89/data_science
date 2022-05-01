from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np

indian_imdb_url = 'https://www.imdb.com/india/top-rated-indian-movies/'
imdb_response = requests.get(indian_imdb_url)
imdb_response
indian_imdb_soup = BeautifulSoup(imdb_response.content, 'html.parser')
