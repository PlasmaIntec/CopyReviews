from Crawler import Crawler
from pathlib import Path
from names import get_first_name, get_last_name
from random import random

def write_review(review):
	crawler = Crawler()
	crawler.get("https://opticats.com")
	assert "Fall Animal Costumes" in crawler.title, "TITLE INCORRECT"
	try:
		crawler.switchFrameByXPath("//iframe[@id='looxReviewsFrame']")

		write_review_button = crawler.findElementByXPath("//button[@id='write']")
		crawler.scrollTo(write_review_button)
		crawler.highlight("//button[@id='write']")
		crawler.click(write_review_button)

		crawler.switchToParentFrame()

		crawler.switchFrameByXPath("//iframe[@id='looxDialog']")

		# rating review
		love_it_button = crawler.findElementByXPath("//div/span[contains(text(), 'Love')]/..")
		crawler.highlight("//div/span[contains(text(), 'Love')]/..")
		crawler.click(love_it_button)

		# photo review
		upload_button = crawler.findPresentElementByXPath("//input[@id='imageupload']")
		crawler.highlight("//label[contains(text(), 'Choose')]")
		crawler.click(upload_button)

		cwd = Path.cwd()
		file_name = f"{cwd}/{review['file']}"
		print(file_name)
		upload_button.send_keys(file_name)

		# generate user
		first_name = get_first_name(gender='male' if random() > .5 else 'female')
		last_name = get_last_name()
		email = f"{first_name}.{last_name}@gmail.com"

		# written review
		text_field = crawler.findElementByXPath("//textarea")
		crawler.highlight("//textarea")
		crawler.click(text_field)
		text_field.send_keys(review["text"])

		next_button = crawler.findElementByXPath("//div[contains(text(),'Next')]")
		crawler.highlight("//div[contains(text(),'Next')]")
		crawler.click(next_button)

		first_name_field = crawler.findElementByXPath("//input[@id='first_name']")
		crawler.highlight("//input[@id='first_name']")
		crawler.click(first_name_field)
		first_name_field.send_keys(first_name)
		print("FIRST NAME: ", first_name)

		last_name_field = crawler.findElementByXPath("//input[@id='last_name']")
		crawler.highlight("//input[@id='last_name']")
		crawler.click(last_name_field)
		last_name_field.send_keys(last_name)
		print("LAST NAME: ", last_name)

		email_field = crawler.findElementByXPath("//input[@id='email']")
		crawler.highlight("//input[@id='email']")
		crawler.click(email_field)
		email_field.send_keys(email)

		# exit review
		done_button = crawler.findElementByXPath("//button[contains(text(),'Done')]")
		crawler.highlight("//button[contains(text(),'Done')]")
		crawler.click(done_button)

		exit_button = crawler.findElementByXPath("//a[@id='close-elem']")
		crawler.highlight("//a[@id='close-elem']")
		crawler.click(exit_button)
	except Exception as e:
		print('MISSING', e)
	crawler.close()

def write_reviews(url, reviews):
	crawler = Crawler()
	crawler.get(url)
	assert "Fall Animal Costumes" in crawler.title, "TITLE INCORRECT"
	for review in reviews:
		try:
			crawler.switchFrameByXPath("//iframe[@id='looxReviewsFrame']")

			write_review_button = crawler.findElementByXPath("//button[@id='write']")
			crawler.scrollTo(write_review_button)
			crawler.highlight("//button[@id='write']")
			crawler.click(write_review_button)

			crawler.switchToParentFrame()

			crawler.switchFrameByXPath("//iframe[@id='looxDialog']")

			# rating review
			love_it_button = crawler.findElementByXPath("//div/span[contains(text(), 'Love')]/..")
			crawler.highlight("//div/span[contains(text(), 'Love')]/..")
			crawler.click(love_it_button)

			# photo review
			upload_button = crawler.findPresentElementByXPath("//input[@id='imageupload']")
			crawler.highlight("//label[contains(text(), 'Choose')]")
			crawler.click(upload_button)

			cwd = Path.cwd()
			file_name = f"{cwd}/{review['file']}"
			print(file_name)
			upload_button.send_keys(file_name)

			# generate user
			first_name = get_first_name(gender='male' if random() > .5 else 'female')
			last_name = get_last_name()
			email = f"{first_name}.{last_name}@gmail.com"

			# written review
			text_field = crawler.findElementByXPath("//textarea")
			crawler.highlight("//textarea")
			crawler.click(text_field)
			text_field.send_keys(review["text"])

			next_button = crawler.findElementByXPath("//div[contains(text(),'Next')]")
			crawler.highlight("//div[contains(text(),'Next')]")
			crawler.click(next_button)

			first_name_field = crawler.findElementByXPath("//input[@id='first_name']")
			crawler.highlight("//input[@id='first_name']")
			crawler.click(first_name_field)
			first_name_field.send_keys(first_name)
			print("FIRST NAME: ", first_name)

			last_name_field = crawler.findElementByXPath("//input[@id='last_name']")
			crawler.highlight("//input[@id='last_name']")
			crawler.click(last_name_field)
			last_name_field.send_keys(last_name)
			print("LAST NAME: ", last_name)

			email_field = crawler.findElementByXPath("//input[@id='email']")
			crawler.highlight("//input[@id='email']")
			crawler.click(email_field)
			email_field.send_keys(email)

			# exit review
			done_button = crawler.findElementByXPath("//button[contains(text(),'Done')]")
			crawler.highlight("//button[contains(text(),'Done')]")
			crawler.click(done_button)

			exit_button = crawler.findElementByXPath("//a[@id='close-elem']")
			crawler.highlight("//a[@id='close-elem']")
			crawler.click(exit_button)

			crawler.switchToParentFrame()
		except Exception as e:
			print('MISSING', e)
	crawler.close()