from eve import Eve
from flask import request, make_response

accept = ["application/json", "application/xml", "*/*", "*/*;q=0.8", "application/xml;q=0.9"]
# accept = ["application/json", "application/xml"]

app = Eve()


@app.after_request
def after_request(response):
    req_accept = request.headers["Accept"].split(",")
    if not any(a in accept for a in req_accept):
        response = make_response('{"_error": {"code": 406, "message": "NOT ACCEPTABLE"},"_status": "ERR"}', 406)
        response.content_type = "application/json"
    return response


def main():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    main()
