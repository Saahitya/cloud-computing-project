from flask import Flask, jsonify, request, abort

app = Flask(__name__)

categories = set(["category1", "category2"]);

no_of_acts_categories_dict = {
    "category1" : 200,
    "category2" : 150,
}

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

# 6
# @app.route('/api/act/list-in-range')

# 7
@app.route('/api/act/upvote', methods=['POST'])
def upvote_act
if __name__ == '__main__':
    app.run(debug=True)