import requests

# url = 'http://174.138.37.68/brands?pretty&embedded={"models":1}'
# url = 'http://127.0.0.1:5000/employees?firstname=f&born=asd'  # for 400 code
# url = 'http://127.0.0.1:5000/employees?where={"_created": {"$gte":"Wed, 25 Feb 1987 17:00:00 GMT"}}'
# url = 'http://127.0.0.1:5000/employees?where={"firstname": {"$gte":"Misha"}}'
# data = {"firstname": "t", "born": "asdf"}
# data = {'where': '{"firstname":"Misha"}'}
# data = {'where': 'where=firstname==Misha'}
# data = {'where': '{"firstname": {"$regex": "^Mis"}}'}
# data = {'max_results': 2, 'page': 1}
# data = {"name": "Zafira", "fuel": ["gasoline", "propane"]}
# data = {"title": "Opel", "models": ["5a271a1f42aa902d2c22e5e8"]}
# data = {"title": "Opel", "models": ["5a27169442aa902c10d01a0d"]}
# IF-Match for concurrency control

url = 'http://174.138.37.68/models'

# data = {"brand": "Lexus"}
data = {"model": "Insignia", "brand": "Opel"}

h = {"Accept": "application/json"}

# r = requests.get(url, headers=h)

# print(r.headers["ETag"])

# print(r.text)
# brand_e_tag = r.headers["ETag"]
# h = {"Accept": "application/json", "If-Match": brand_e_tag}
# # r = requests.get(url, headers=h)
r = requests.post(url, json=data, headers=h)
# # print(r)
print(r.headers)
print(r.text)
