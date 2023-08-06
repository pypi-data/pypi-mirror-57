#!/usr/bin/env python3
# -*- coding: utf-8 -*-

name = 'goodreads_book_quotes'

import requests
from bs4 import BeautifulSoup
import hashlib

def findBetween(text, start, end):
	index1 = text.find(start)
	index2 = text.find(end, index1)
	return text[index1 + len(start) : index2]

def getRequest(url, params = {}):
	cache = 'tmp_' + hashlib.sha224(url.encode('utf-8') + str(params).encode('utf-8')).hexdigest()[:10] + '.html'
	try:
		with open(cache) as f:
			return f.read()
	except:
		content = requests.get(url, params=params).text
		with open(cache, 'w') as f:
			f.write(content)
		return content

def cleanupQuote(item):
	names = ['span', 'script']
	for name in names:
		for x in item.find_all(name):
			x.decompose()
	for br in item.find_all("br"):
		br.replace_with("\n")
	result = item.text
	return result.strip()[:-1].strip()

class GQ(object):
	def __init__(self, key):
		self.key = key
		self.search_url = "https://www.goodreads.com/search/index.xml"
		self.quote_url = "https://www.goodreads.com/work/quotes/"

	def searchBook(self, book):
		result = getRequest(
			self.search_url, 
			params={
				'q': book,
				'key': self.key})
		return int(findBetween(
			result, '<id type="integer">', '</id>'))

	def getQuotes(self, book_id):
		page_id = 1
		while page_id < 6:
			result = getRequest(self.quote_url + str(book_id) + '?page=' + str(page_id))
			soup = BeautifulSoup(result, features="lxml")
			has_item = False
			for item in soup.find_all('div', class_='quoteText'):
				has_item = True
				yield cleanupQuote(item)
			if not has_item:
				break
			page_id += 1


	def get(self, book, limit=100):
		book_id = self.searchBook(book)
		return self.getQuotes(book_id)
