from ingestor import get_reviews
from migrator import write_reviews
import pickle

try:
	reviews = pickle.load(open('save.p', 'rb'))
except:
	reviews = get_reviews("https://www.aliexpress.com/item/32968759175.html?spm=a2g0o.productlist.0.0.31e052f8ysXwMR&algo_pvid=5939d449-6b3a-4310-b383-22e7957728c0&algo_expid=5939d449-6b3a-4310-b383-22e7957728c0-1&btsid=c93f3ce4-1503-4b45-beb1-ea8b89bdef15&ws_ab_test=searchweb0_0,searchweb201602_3,searchweb201603_52")
pickle.dump(reviews, open('save.p', 'wb'))
write_reviews("https://opticats.com", reviews)