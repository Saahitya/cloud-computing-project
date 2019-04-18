
from flask import Flask, jsonify, request, abort,redirect, url_for , Response
import requests
import os
import re
import pickle
import threading
import sys
import time
cont_dict = {}
no_of_req = 0
first_req = 0
lock_no_of_req = threading.Lock()
app = Flask(__name__)
cur_cont = 0
def auto_scale():
    global no_of_req
    print('Hello world!', file=sys.stderr)
    while(1):
        time.sleep(30)
        lock_no_of_req.acquire()
        num_cont_needed = (no_of_req // 20) + 1
        if(len(cont_dict) != num_cont_needed):
            if(len(cont_dict) < num_cont_needed):
                max_cont_id = max(list(cont_dict.keys()))
                extra_cont = num_cont_needed - len(cont_dict)
                for i in range(extra_cont):
                    con = os.popen("sudo docker run -p " + str(max_cont_id + i + 1) + ":80 -d acts").read()
                    con_real = con.rstrip()
                    cont_dict[max_cont_id + i + 1] = con_real
                print(cont_dict,file=sys.stderr)
            else:
                max_cont_id = max(list(cont_dict.keys()))
                extra_cont = abs(num_cont_needed - len(cont_dict))
                while(extra_cont != 0):
                    cont_id_kill = cont_dict[max_cont_id]
                    tmp = os.popen("sudo docker container kill " + cont_id_kill).read()
                    del(cont_dict[max_cont_id])
                    max_cont_id = max_cont_id - 1
                    extra_cont = extra_cont - 1
                print(cont_dict,file=sys.stderr)
        else:
            print("Same number of containers",file=sys.stderr)
        no_of_req = 0
        lock_no_of_req.release()
def init_container():
    con = os.popen("sudo docker run -p 8000:80 -d acts").read()
    con_real = con.rstrip()
    cont_dict[8000] = con_real
#app = Flask(__name__)
@app.route('/api/v1/categories', methods=['GET'])
def fun():
    lock_no_of_req.acquire()
    global first_req
    global no_of_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/categories', methods=['POST'])
def cat_post():
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/categories/<string:categoryName>', methods=['DELETE'])
def rem_cat(categoryName):
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/categories/<string:categoryName>/acts', methods=['GET'])
def list_acts_for_category(categoryName):
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/categories/<string:categoryName>/acts/size', methods=['GET'])
def number_of_acts_for_category(categoryName):
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/acts/upvote', methods=['POST'])
def upvote_an_act():
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/acts/<int:task_id>',methods = ['DELETE'])
def delete_act(task_id):
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/acts', methods=['POST'])
def upload_an_act():
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/_count',methods=['GET'])
def count_fun():
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/_count',methods=['DELETE'])
def del_count():
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response

@app.route('/api/v1/acts/count',methods=['GET'])
def count1():
    lock_no_of_req.acquire()
    global no_of_req
    global first_req
    if(first_req == 0):
      first_req = 1
      no_of_req = 1
      t1 = threading.Thread(target=auto_scale)
      t1.start()
    old_url = request.url
    parts = old_url.split("http://35.171.62.224")
    global cur_cont
    cur_cont = (cur_cont + 1) % len(cont_dict)
    new_url = "http://127.0.0.1:"+str(cur_cont + 8000)+parts[1]
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    no_of_req = no_of_req + 1
    lock_no_of_req.release()
    return response


if __name__ == '__main__':
    init_container()
    #t1 = threading.Thread(target = auto_scale)
    #t1.start()
    app.run("0.0.0.0",port=80)
