from flask import Flask, jsonify, request, abort

app = Flask(__name__)

categories = set(["category1", "category2"]);

no_of_acts_categories_dict = {
    "category1" : 200,
    "category2" : 150,
}

user_list = []

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

# 1
@app.route('/api/category/list', methods=['GET'])
def list_categories():
    if not request.is_json:
        abort(405)
    elif(len(categories) > 0):
        return jsonify(no_of_acts_categories_dict), 200
    else:
        return jsonify({}), 204

# 2
@app.route('/api/category/add', methods=['POST'])
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

# 3
@app.route('/api/category/remove', methods=['DELETE'])
def remove_category():
    if not request.is_json or len(request.json) != 1:
        abort(400)
    elif request.json[0] in no_of_acts_categories_dict and request.json[0] in categories:
        category = request.json[0]
        no_of_acts_categories_dict.pop(category)
        acts_list_categories_dict.pop(category)
        categories.remove(category)
        return jsonify({}), 200
    else:
        abort(405)

# 4
@app.route('/api/acts/list', methods=['GET'])
def list_acts_for_category():
    if not request.is_json or len(request) != 1:
        abort(400)
    elif request.json[0] in acts_categories_dict:
        category = request.json[0]
        acts_list = acts_list_categories_dict[category]
        len_acts_list = len(acts_list)
        if(len_acts_list == 0):
            return jsonify([]), 204
        elif(len_acts_list > 500) :
            abort(413)
        else:
            return jsonify(len_acts_list), 200
    else:
        return abort(405)

# 5
@app.route('/api/category/size', methods=['GET'])
def number_of_acts_for_category():
    if not request.is_json:
        abort(400)
    elif len(request.json) == 1:
        return jsonify([]), 204
    elif request.json[0] in categories:
        return jsonify([categories[request.json[0]]])
    else:
        abort(405)
#10

@app.route('/api/v1/acts/<int:task_id>',methods = ['DELETE'])
def delete_act(task_id):
    categories = list(acts_list_categories_dict.keys());
    flag = 0
    for i in categories:
        acts = acts_list_categories_dict[i]
        for j in acts:
            if(j["actId"] == task_id):
                category = i
                flag = 1
                break
    if(flag == 0):
        abort(405)
    else:
        act_list = acts_list_categories_dict[category]
        for i in range(len(act_list)):
            if(act_list[i]["actId"] == task_id):
                break
        del(act_list[i])
        return jsonify({}),200
#1
@app.route('/api/v1/users',methods = ['POST'])
def add_user():
    if not request.is_json or len(request.json) != 2:
        abort(400)
    users = []
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
if __name__ == '__main__':
    app.run(debug=True)
