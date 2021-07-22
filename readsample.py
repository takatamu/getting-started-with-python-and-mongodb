from pymongo import MongoClient

MONGODB_URL = "YOUR MONGODB URL"
client = MongoClient(MONGODB_URL)
db = client.business

fivestar = db.reviews.find_one({'rating': 5})
print(fivestar)

print('The number of 5 star reviews:')
fivestarcount = db.reviews.count_documents({'rating': 5})
# fivestarcount = db.reviews.find({'rating': 5}).count_documents()
print(fivestarcount)

print('\nThe sum of each rating occurance across all data grouped by rating ')
stargroup = db.reviews.aggregate(
    [
        {
            '$group':
            {'_id': '$rating',
            "count": {
                '$sum': 1
                }
            }
        },
        {
            '$sort': {
                '_id': 1
            }
        }
    ]
)

for group in stargroup:
    print(group)