from flask import Flask, jsonify, request, abort,redirect, url_for , Response
import requests
import re
import pickle
import time
import threading
import os
no_of_connections = 0
app = Flask(__name__)
cont_dict = {}
def init_container():
    con = os.popen("sudo docker run -p 8000:80 -d acts").read()
    con_real = con.rstrip()
    con_dict[8000] = con_real
@app.route('/api/v1/categories', methods=['GET'])
def fun():
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/categories', methods=['POST'])
def cat_post():
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/categories/<string:categoryName>', methods=['DELETE'])
def rem_cat(categoryName):
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/categories/<string:categoryName>/acts', methods=['GET'])
def list_acts_for_category(categoryName):
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/categories/<string:categoryName>/acts/size', methods=['GET'])
def number_of_acts_for_category(categoryName):
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/acts/upvote', methods=['POST'])
def upvote_an_act():
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,    t1 = threading.Thread(target=print_square, args=(10,))
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/acts/<int:task_id>',methods = ['DELETE'])
def delete_act(task_id):
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/acts', methods=['POST'])
def upload_an_act():
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/_count',methods=['GET'])
def count_fun():
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/_count',methods=['DELETE'])
def del_count():
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response

@app.route('/api/v1/acts/count',methods=['GET'])
def count1():
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    new_url = "http://127.0.0.1:8000"+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    return response


if __name__ == '__main__':
    init_container()
    app.run("0.0.0.0",port=80)
    t1 = threading.Thread(target=auto_scale)
    t1.start()
    t1.join()
