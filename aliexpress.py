from Crawler import Crawler
import urllib.request

def get_reviews():		
	posts = []
	crawler = Crawler()
	crawler.get("https://www.aliexpress.com/item/32968759175.html?spm=a2g0o.productlist.0.0.31e052f8ysXwMR&algo_pvid=5939d449-6b3a-4310-b383-22e7957728c0&algo_expid=5939d449-6b3a-4310-b383-22e7957728c0-1&btsid=c93f3ce4-1503-4b45-beb1-ea8b89bdef15&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_52")
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