from pymongo import MongoClient
from random import randint

MONGODB_URL = "YOUR MONGODB URL"
client = MongoClient(MONGODB_URL)
db = client.business

names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

# businesses = []
for x in range(1, 501):
    business = {
        'name' : names[randint(0, (len(names) - 1))] + ' ' + names[randint(0, (len(names) - 1))] + ' ' + company_type[randint(0, (len(company_type) - 1))],
        'rating' : randint(1, 5),
        'cuisine': company_cuisine[randint(0, (len(company_cuisine) - 1))]
    }
    # businesses.append(business)

    result = db.reviews.insert_one(business)
    print('Created {0} of 500 as {1}'.format(x, result.inserted_id))

# db.reviews.insert_many(businesses)
print('finished creating 500 business reviews')