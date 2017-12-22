from eve import Eve
from flask import request, make_response
from eve_swagger import swagger, add_documentation

accept = ["application/json", "application/xml", "*/*", "*/*;q=0.8", "application/xml;q=0.9"]
# accept = ["application/json", "application/xml"]

app = Eve()
# app.register_blueprint(swagger)
#
# app.config['SWAGGER_INFO'] = {
#     'title': 'My Supercool API',
#     'version': '1.0',
#     'description': 'an API description',
#     'termsOfService': 'my terms of service',
#     'contact': {
#         'name': 'nicola',
#         'url': 'http://nicolaiarocci.com'
#     },
#     'license': {
#         'name': 'BSD',
#         'url': 'https://github.com/pyeve/eve-swagger/blob/master/LICENSE',
#     },
#     'schemes': ['http', 'https'],
# }
#
# app.config['SWAGGER_INFO'] = {
#     'title': 'My Supercool API',
#     'version': '1.0',
#     'description': 'an API description',
#     'termsOfService': 'my terms of service',
#     'contact': {
#         'name': 'nicola',
#         'url': 'http://nicolaiarocci.com'
#     },
#     'license': {
#         'name': 'BSD',
#         'url': 'https://github.com/pyeve/eve-swagger/blob/master/LICENSE',
#     },
#     'schemes': ['http', 'https'],
# }
#
# # optional. Will use flask.request.host if missing.
# app.config['SWAGGER_HOST'] = '127.0.0.1:5000'
#
# # optional. Add/Update elements in the documentation at run-time without deleting subtrees.
# add_documentation({'paths': {'/status': {'get': {'parameters': [
#     {
#         'in': 'query',
#         'name': 'foobar',
#         'required': False,
#         'description': 'special query parameter',
#         'type': 'string'
#     }]
# }}}})


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
