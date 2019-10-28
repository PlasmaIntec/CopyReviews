from Crawler import Crawler
from pathlib import Path
from names import get_first_name, get_last_name
from selenium.webdriver.common.keys import Keys
from random import random
from time import time

def load_more(url):
	crawler = Crawler()
	crawler.get(url)
	assert "Influencer Love | Fashion ID" in crawler.title, "TITLE INCORRECT"
	try:
		times_clicked = 0
		start = int(time())
		while True:
			# delete tab if we accidentally trip a twitter tab open
			if "Twitter" in crawler.getTitle():
				crawler.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
				any_button = crawler.findElementsByXPath("//a")[0]
				any_button.send_keys(Keys.COMMAND + 'w')
				crawler.closeExtraTabs()
			
			# find load more button
			load_more_button = crawler.findElementByXPath("//a[@id='ctf-more']")
			crawler.highlight("//a[@id='ctf-more']")
			crawler.click(load_more_button)
			times_clicked += 1
			print('%s CLICKS' % times_clicked)
			crawler.closeExtraTabs()

	except Exception as e:
		print('EXCEPTION', e)
	crawler.close()
	end = int(time())
	print(start)
	print(end)
	print('TOTAL TIME ELAPSED: %s' % (end - start))