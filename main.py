from aliexpress import get_reviews
from opticats import write_reviews

reviews = get_reviews()
write_reviews(reviews)