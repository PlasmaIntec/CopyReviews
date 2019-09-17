from aliexpress import get_reviews
from opticats import write_reviews
import pickle

try:
	reviews = pickle.load(open('save.p', 'rb'))
except:
	reviews = get_reviews()
pickle.dump(reviews, open('save.p', 'wb'))
write_reviews(reviews)