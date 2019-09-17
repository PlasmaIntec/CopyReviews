from Crawler import Crawler
import urllib.request

def get_reviews(url):		
	posts = []
	crawler = Crawler()
	crawler.get(url)
	assert "Sunglasses" in crawler.title, "TITLE INCORRECT"
	try:
		close_banner = crawler.findElementByXPath("//a[@class='next-dialog-close']")
		crawler.click(close_banner)

		product_details = crawler.findElementByXPath("//div[@id='product-detail']")
		crawler.scrollTo(product_details)

		reviews_tab = crawler.findElementByXPath("//div[@id='product-detail']//ul/li[@ae_object_type='feedback']")
		crawler.scrollTo(reviews_tab)
		crawler.highlight("//div[@id='product-detail']//ul/li[@ae_object_type='feedback']")
		crawler.click(reviews_tab)

		crawler.switchFrameByXPath("//iframe[@id='product-evaluation']")

		photo_filter = crawler.findElementByXPath("//label[text()[contains(.,'Photo')]]")
		crawler.click(photo_filter)
		crawler.highlight("//label[text()[contains(.,'Photo')]]")

		reviews = crawler.findElementsByXPath("//div[@class='feedback-item clearfix']")
		for count, review in enumerate(reviews):
			post = {}
			post["text"] = review.find_element_by_xpath(".//dt/span").text
			print(post["text"])
			review_pic = review.find_element_by_xpath(".//img")
			post["src"] = review_pic.get_attribute("src")
			print(post["src"])
			post["file"] = f"{count}_review.png"
			urllib.request.urlretrieve(post["src"], post["file"])
			posts.append(post)
	except Exception as e:
		print('ERROR', e)
	crawler.close()
	return posts