import os
from bs4 import BeautifulSoup
#from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeout
import time

SEASONS = list(range(2018,2025))
DATA_DIR = 'data'
STANDINGS_DIR = os.path.join(DATA_DIR,'standings')
SCORES_DIR = os.path.join(DATA_DIR,'scores')

