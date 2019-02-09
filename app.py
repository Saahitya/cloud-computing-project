from flask import Flask, jsonify, request, abort
#d
app = Flask(__name__)

categories = set(["category1", "category2"]);

no_of_acts_categories_dict = {
    "category1" : 2,
    "category2" : 0,
}

user_list = [] #List of dictionaries with each dictionary corresponding to one user with 2 keys : username and password

range_list = []
k=0

acts_list_categories_dict = {
    "category1" : [
                    {
                        "actId": 1234,
                        "timestamp": "DD-MM-YYYY:SS-MM-HH",
                        "caption": "captiontext",
                        "upvotes": 25,
                        "imgUrl": "xyz.abc/img.png"

                    },
                ],
    "category2" : [],
}
@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

# 1_final [Add users]
@app.route('/api/v1/users',methods = ['POST'])
def add_user():
    if not request.is_json or len(request.json) != 2:
        abort(400)
    users = []	#List of existing usernames in the database
    for i in user_list:
        users.append(i["username"])
    if(request.json["username"] not in users):
        hex = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']
        passwd = request.json["password"]
        if(len(passwd) == 40):
            for i in passwd:
                if(i not in hex):
                    abort(405)
            d = {}
            d["username"] = request.json["username"]
            d["password"] = request.json["password"]
            user_list.append(d)
            return jsonify({}),201
        else:
            abort(405)
    else:
        abort(405)

# 2_final [Remove users]
@app.route('/api/v1/users/<string:username>',methods = ['DELETE'])
def rem_user(username):
    if not request.is_json or len(request.json) != 0:
        abort(400)
    users = []
    for i in user_list:
        users.append(i["username"])
    if(username in users):
        index = users.index(username)
        del(user_list[index])
        return jsonify({}),200
    else:
        abort(405)

# 3_final [List all categories]
@app.route('/api/v1/categories', methods=['GET'])
def list_categories():
    if not request.is_json:
         abort(405)
    if(len(categories) > 0):
        return jsonify(no_of_acts_categories_dict),200
    else:
        return jsonify({}),204

# 4_final  [Add a category]
@app.route('/api/v1/categories', methods=['POST'])
def add_category():
    if not request.is_json or len(request.json) != 1:
        abort(400)
    elif request.json[0] not in categories:
        category = request.json[0]
        no_of_acts_categories_dict[category] = 0
        acts_list_categories_dict[category] = []
        categories.add(category)
    else:
        abort(405)
    return jsonify({}), 201

# 5_final  [Remove a category]
@app.route('/api/v1/categories/<string:categoryName>', methods=['DELETE'])
def remove_category(categoryName):
    if not request.is_json or len(request.json) != 0:
        abort(400)
    elif categoryName in no_of_acts_categories_dict.keys() and categoryName in categories:
        no_of_acts_categories_dict.pop(categoryName)
        acts_list_categories_dict.pop(categoryName)
        categories.remove(categoryName)
        return jsonify({}), 200
    else:
        abort(405)

# 6_final  [List acts for a given category]
@app.route('/api/v1/categories/<string:categoryName>/acts', methods=['GET'])
def list_acts_for_category(categoryName):
    if not request.is_json or len(request.json) != 0:
        abort(400)
    elif categoryName in acts_list_categories_dict:
        acts_list = acts_list_categories_dict[categoryName]
        len_acts_list = len(acts_list)
        if(len_acts_list == 0):
            return jsonify([]), 204
        elif(len_acts_list > 500) :
            abort(413)
        else:
            return jsonify(acts_list), 200
    else:
        abort(405)


# 7_final [Number of acts in a category]
@app.route('/api/v1/categories/<string:categoryName>/acts/size', methods=['GET'])
def number_of_acts_for_category(categoryName):
    if not request.is_json or len(request.json) != 0:
        abort(400)
    elif categoryName not in no_of_acts_categories_dict.keys():
        return jsonify([]), 204
    elif categoryName in no_of_acts_categories_dict.keys():
        return jsonify([no_of_acts_categories_dict[categoryName]])
    else:
        abort(405)

# 8_final [Return acts for a given category in a given range]
@app.route('/api/v1/categories/<string:categoryName>/acts?start=<int:startRange>&end=<int:endRange>', methods=['GET'])
def acts_in_range(categoryName, startRange, endRange):
    if not request.is_json or len(request) != 0:
        abort(400)
    elif categoryName not in no_of_acts_categories_dict.keys():
        return jsonify([]), 204
    else:
        for i in acts_list_categories_dict[categoryName]:
            if((k >= startRange) and (k <= endRange)):
                range_list.append(i)
            k = k + 1
        if(len(range_list) > 100):
            abort(413)
        else:
            return jsonify(i), 200
    abort(405)



# 9_final [Upvote an act]
@app.route('/api/v1/acts/upvote', methods=['POST'])
def upvote_an_act():
	if not request.is_json or len(request.json) != 1:
	        abort(400)
	for i in acts_list_categories_dict.values():
		for j in i:
			if j["actId"]==request.json[0]:
				j["upvotes"] = j["upvotes"]+1
				return jsonify({}), 200
	abort(405)

# 10_final [Remove an act]
@app.route('/api/v1/acts/<int:task_id>',methods = ['DELETE'])
def delete_act(task_id):
    if not request.is_json or len(request.json) != 0:
            abort(400)
    # for i in acts_list_categories_dict.values():
    #     for j in range(len(i)):
    #         if j["actId"]==task_id:
    #             del(j)
    #             return jsonify({}), 200
    category_list = list(acts_list_categories_dict.keys())
    for i in (category_list):
        act_list = acts_list_categories_dict[i]
        flag = 0
        for j in range(len(act_list)):
            if(act_list[j]["actId"] == task_id):
                del(act_list[j])
                no_of_acts_categories_dict[i] = no_of_acts_categories_dict[i] - 1
                return jsonify({}),200
    abort(405)


# 11_final []
# @app.route('/api/v1/acts', methods=['POST'])
# def upload_an_act():
#     if not request.is_json or len(request.json) != 6:
#             abort(400)
#     #The ​actID​ in the request body must be globally unique(1,7)
#     for i in acts_list_categories_dict.values():
#         for j in i:
#             if j[actId]==request.json[0]:
#                 abort(400)
#     #The username must exist(3)
#     int flag = 0
#     for i in user_list:
#         if i["username"] == request.json[1]:
#             flag = 1
#             break
#     if flag==0:
#         abort(400)
#     #No upvotes field should be sent(5)
#     if "upvotes" in request.json.keys():
#         abort(400)
#     #The category name must exist(6)
#     if request.json[4] not in categories:
#         abort(400)
#     #Uploading the act
#     no_of_acts_categories_dict[json.request[4]] = no_of_acts_categories_dict[json.request[4]]+1
#     d = dict()
#     d["actId"] = json.request[0]
#     d["timestamp"] = json.request[2]
#     d["caption"] = json.request[3]
#     d["upvotes"] = 0
#     d["imgUrl"] = json.request[5]
#     acts_list_categories_dict[json.request[4]].append(d)
#     return jsonify({}), 200
# import base64
# import binascii
#
# try:
#     base64.decodestring("foo")
# except binascii.Error:
#     print "no correct base64"

@app.route('/api/v1/acts', methods=['POST'])
def upload_an_act():
    if not request.is_json or len(request.json) != 6:
        abort(400)
    #The ​actID​ in the request body must be globally unique(1,7)
    for i in acts_list_categories_dict.values():
        for j in i:
            if j["actId"]==request.json["actId"]:
                abort(405)

    #Validatin date and time (2)
    #if(request.json["timestamp"] != datetime.strptime(request.json["timestamp"], "%\d-%m-%y %S:%M:%H")):
    #    abort(400)
    flag = 0
    for i in user_list:
        if i["username"] == request.json["username"]:
            flag = 1
            break
    if flag==0:
        abort(405)


    #No upvotes field should be sent(5)
    if "upvotes" in request.json.keys():
        abort(400)

    #The category name must exist(6)
    if request.json["categoryName"] not in categories:
        abort(405)

    # Validating base_64 password
    # if( not re.match(r"^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$", json.request["imgB64"])):
    #      abort(400)

    #Uploading the act
    no_of_acts_categories_dict[request.json["categoryName"]] = no_of_acts_categories_dict[request.json["categoryName"]]+1
    d = dict()
    d["actId"] = request.json["actId"]
    d["timestamp"] = request.json["timestamp"]
    d["caption"] = request.json["caption"]
    d["upvotes"] = 0
    d["imgUrl"] = request.json["imgB64"]
    acts_list_categories_dict[request.json["categoryName"]].append(d)
    return jsonify({}), 201

if __name__ == '__main__':
    app.run(debug=True)
