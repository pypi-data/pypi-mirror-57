#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Import Modules
from bs4 import BeautifulSoup
import requests


# Define Function to load Site and convert to BeautifulSoup
def _make_soup(url: str):
    src = requests.get(url).content
    soup = BeautifulSoup(src, "lxml")
    return soup