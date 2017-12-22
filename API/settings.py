MONGO_HOST = '165.227.84.108'
MONGO_PORT = 27017
MONGO_DBNAME = 'api'
MONGO_QUERY_BLACKLIST = ['$where']

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
VALIDATION_ERROR_STATUS = 400

# CACHE_EXPIRES = 10
CACHE_CONTROL = "max-age=30"

# SERVER_NAME = '127.0.0.1:8081'

# X_EXPOSE_HEADERS = ['Content-Type']
# XML, JSON = True, False
X_DOMAINS = "*"
X_HEADERS = ['Content-Type', 'If-Match']  # Needed for the "Try it out" buttons / CORS

DOMAIN = {
    # Resource `/models`
    'models': {
        'schema': {
            'model': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
                'required': True,
            },
            'engine': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 15,
            },
            'fuel': {
                'type': 'list',
                'allowed': ["gasoline", "diesel", "methane", "propane", "electric", "hybrid"],
            },
            'body': {
                'type': 'list',
                'allowed': ["sedan", "coupe", "hatchback", "minivan",
                            "van", "cabriolet", "universal", "suv",
                            "pickup", "offroad", "truck"],
            },
            'year': {
                'type': 'datetime',
            },
            'price': {
                'type': 'integer',
                'default': 0
            },
            'brand': {
                'type': 'string',
                'required': True,
                'data_relation': {
                    'resource': 'brands',
                    'field': 'brand',
                    'embeddable': True
                }
            }
        }
    },

    # Resource `/brands`
    'brands': {
        'schema': {
            'brand': {
                'type': 'string',
                'minlength': 3,
                'maxlength': 32,
                'required': True,
                'unique': True
            },
            'year': {
                'type': 'integer'
            },
            'country': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 32,
            }
        }
    }
}
