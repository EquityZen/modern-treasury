from flask import Flask, request, Response

app = Flask(__name__)

HTTP_METHODS = ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']


@app.route('/', methods=HTTP_METHODS)
def respond():
    print(request.json)
    return Response(status=200)
