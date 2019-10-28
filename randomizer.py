from Crawler import Crawler
from pathlib import Path
from names import get_first_name, get_last_name
from random import random

def random_page(url):
	crawler = Crawler()
	crawler.get(url)
	assert "Urban Dictionary" in crawler.title, "TITLE INCORRECT"
	try:
		# find random page
		random_button = crawler.findElementByXPath("//a[@class='circle-button' and @href='/random.php']")
		crawler.highlight("//a[@class='circle-button' and @href='/random.php']")
		crawler.click(random_button)

		# extract content
		word = crawler.findElementByXPath("(//a[@class='word'])[1]").text
		crawler.highlight("(//a[@class='word'])[1]")
		meaning = crawler.findElementByXPath("(//div[@class='meaning'])[1]").text
		crawler.highlight("(//div[@class='meaning'])[1]")
		content = f'The word {word} means {meaning}'
		return content
	except:
		print('MISSING', e)
	crawler.close()