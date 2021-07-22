from pymongo import MongoClient
from pprint import pprint

MONGODB_URL = "YOUR MONGODB URL"
client = MongoClient(MONGODB_URL)
db = client.business

ASingleReview = db.reviews.find_one({})
print('A sample document:')
pprint(ASingleReview)

single_delete_result = db.reviews.delete_one({'_id': ASingleReview.get('_id')})
print('Number of documents deleted: ' + str(single_delete_result.deleted_count))

many_delete_result = db.restaurants.delete_many({'category': 'Bar Food'})
print('Number of documents deleted: ' + str(many_delete_result.deleted_count))