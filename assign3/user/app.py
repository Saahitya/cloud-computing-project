from flask import Flask, jsonify, request, abort
import re
import pickle
#d
app = Flask(__name__)

# categories = set(["category1", "category2"]);
#
# no_of_acts_categories_dict = {
#     "category1" : 0,
#     "category2" : 0,
# }
#
# user_list = [] #List of dictionaries with each dictionary corresponding to one user with 2 keys : username and password
#
# range_list = []
k=0
#
# acts_list_categories_dict = {
#     "category1" : [],
#     "category2" : [],
# }
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

# 1_final [Add users]
@app.route('/api/v1/users',methods = ['POST'])
def add_user():
    users = []	#List of existing usernames in the database
    for i in user_list:
        users.append(i["username"])
    if(request.json["username"] not in users):
        hex = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
        passwd = request.json["password"]
        if(len(passwd) == 40):
            for i in passwd:
                if(i not in hex):
                    abort(400)
            d = {}
            d["username"] = request.json["username"]
            d["password"] = request.json["password"]
            user_list.append(d)
            return jsonify({}),201
        else:
            abort(400)
    else:
        abort(405)

# 2_final [Remove users]
@app.route('/api/v1/users/<string:username>',methods = ['DELETE'])
def rem_user(username):
    #print(username)
    users = []
    for i in user_list:
        users.append(i["username"])
    if(username in users):
        index = users.index(username)
        del(user_list[index])
        return jsonify({}),200
    else:
        abort(405)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    pickle.dump(categories, open("categories.p", "wb"))
    pickle.dump(no_of_acts_categories_dict, open("no_of_acts_categories_dict.p", "wb"))
    pickle.dump(user_list, open("user_list.p", "wb"))
    pickle.dump(range_list, open("range_list.p", "wb"))
    pickle.dump(acts_list_categories_dict, open("acts_list_categories_dict.p", "wb"))
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == '__main__':
    no_of_acts_categories_dict = pickle.load(open("no_of_acts_categories_dict.p", "rb"))
    categories = pickle.load(open("categories.p", "rb"))
    user_list = pickle.load(open("user_list.p", "rb"))
    range_list = pickle.load( open("range_list.p", "rb"))
    acts_list_categories_dict = pickle.load(open("acts_list_categories_dict.p", "rb"))
    app.run("0.0.0.0",port=80)
