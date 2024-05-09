import pandas as pd
import numpy as np
import json
import requests
import codecs
import glob
from bs4 import BeautifulSoup as bs
from docx import Document
from tqdm.auto import tqdm, trange
import nltk
import matplotlib.pyplot as plt
import pymorphy2
import string

import re
from nltk.stem import *
from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
import seaborn as sns
from scipy.stats import shapiro
from scipy.stats import anderson
from scipy.stats import normaltest
import pylab 
import scipy.stats as stats

dfHabr = {"TitleCompany": [], 'Description': [], 'Reiting' : [], 'Categories' : [], 'DatePublish': [], "TextPost": []}