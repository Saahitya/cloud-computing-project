from flask import Flask, jsonify, request, abort, redirect, url_for , Response
import requests
import os
import re
import pickle
from threading import Thread, Lock
import sys
import time

container_dictionary = {}
number_of_requests = 0
first_request = False
lock_number_of_requests = Lock()
container_dictionary_lock = Lock()
app = Flask(__name__)
current_container = 0

def start_last_container():
    max_cont_id = max(list(container_dictionary.keys()))
    container_id = os.popen("sudo docker run -v saksham:/app_act -p " + str(max_cont_id + i + 1) + ":80 -d acts").read().rstrip()
    container_dictionary[max_cont_id + 1] = container_id

def kill_last_container():
    max_cont_id = max(list(container_dictionary.keys()))
    cont_id_kill = container_dictionary[max_cont_id]
    tmp = os.popen("sudo docker container kill " + cont_id_kill).read()
    del(container_dictionary[max_cont_id])


def auto_scale():
    global number_of_requests
    print('Auto Scaling Started', file=sys.stderr)
    while(1):
        time.sleep(120)
        lock_number_of_requests.acquire()
        container_dictionary_lock.acquire()
        num_cont_needed = (number_of_requests // 20) + 1
        if(len(container_dictionary) != num_cont_needed):
            if(len(container_dictionary) < num_cont_needed):
                no_of_extra_containers = num_cont_needed - len(container_dictionary)
                for i in range(no_of_extra_containers):
                    start_last_container()
                    time.sleep(1)
                print(container_dictionary,file=sys.stderr)
            else:
                no_of_extra_containers = abs(num_cont_needed - len(container_dictionary))
                while(no_of_extra_containers != 0):
                    kill_last_container()
                    no_of_extra_containers = no_of_extra_containers - 1
                print(container_dictionary,file=sys.stderr)
        else:
            print("Same number of containers",file=sys.stderr)
        number_of_requests = 0
        container_dictionary_lock.release()
        lock_number_of_requests.release()

def load_balancer_handler(url):
    lock_number_of_requests.acquire()
    global number_of_requests, first_request
    if(first_request == False):
      first_request = True
      number_of_requests += 1
      t1 = Thread(target=auto_scale)
      t1.start()
    parts = url.split("http://localhost")
    global current_container
    container_dictionary_lock.acquire()
    current_container = (current_container + 1) % len(container_dictionary)
    new_url = "http://127.0.0.1:"+str(current_container + 8000)+parts[1]
    container_dictionary_lock.release()
    resp = requests.request(
        method=request.method,
        url= new_url,
        headers={key: value for (key, value) in request.headers if key != 'Host'},
        data=request.get_data())
    headers = [(name, value) for (name, value) in resp.raw.headers.items()]
    response = Response(resp.content, resp.status_code, headers)
    number_of_requests = number_of_requests + 1
    lock_number_of_requests.release()
    return response

def fault_tolerance():
    print("Fault tolereance started",file=sys.stderr)
    while(1):
        print("Fault check",file=sys.stderr)
        time.sleep(1)
        container_dictionary_lock.acquire()
        
        active_containers = list(container_dictionary.keys())
        for container_ip in active_containers:
            request_ = requests.get("http://127.0.0.1:"+str(container_ip)+"/api/v1/_health")
            if(request_.status_code == 500):
                os.popen("sudo docker container kill " + container_dictionary[container_ip]).read()
                del(container_dictionary[container_ip])
                container_id = os.popen("sudo docker run -p " + str(container_ip) + ":80 -d acts").read().rstrip()
                container_dictionary[container_ip] = container_id
                print("started a new container for "+str(container_ip),file=sys.stderr)
        
        container_dictionary_lock.release()


def init_container():
    con = os.popen("sudo docker run -v saksham:/app_act -p  8000:80 -d acts").read()
    con_real = con.rstrip()
    container_dictionary[8000] = con_real

@app.route('/api/v1/categories', methods=['GET'])
def fun():
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/categories', methods=['POST'])
def cat_post():
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/categories/<string:categoryName>', methods=['DELETE'])
def rem_cat(categoryName):
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/categories/<string:categoryName>/acts', methods=['GET'])
def list_acts_for_category(categoryName):
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/categories/<string:categoryName>/acts/size', methods=['GET'])
def number_of_acts_for_category(categoryName):
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/acts/upvote', methods=['POST'])
def upvote_an_act():
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/acts/<int:task_id>',methods = ['DELETE'])
def delete_act(task_id):
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/acts', methods=['POST'])
def upload_an_act():
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/_count',methods=['GET'])
def count_fun():
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/_count',methods=['DELETE'])
def del_count():
    response = load_balancer_handler(request.url)
    return response

@app.route('/api/v1/acts/count',methods=['GET'])
def count1():
    response = load_balancer_handler(request.url)
    return response

if __name__ == '__main__':
    init_container()
    Thread(target = fault_tolerance).start()
    app.run("0.0.0.0",port=80)
