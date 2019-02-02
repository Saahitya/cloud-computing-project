from flask import Flask, jsonify, request, abort

app = Flask(__name__)

categories = {
    "category name 1": 200,
    "category name 2":150,
}
#1
@app.route('/api/category/list', methods=['GET'])
def list_categories():
    return jsonify(categories)
#2
@app.route('/api/category/add', methods=['POST'])
def add_category():
    if not request.is_json or len(request.json)!=1:
        abort(400)
    if request.json[0] not in categories:
        categories[request.json[0]] = 0
    else:
        abort(405)
    return jsonify({}), 201
#3
@app.route('/api/category/remove', methods=['DELETE'])
def remove_category():
    print("Hallelujah in remove")
    if not request.is_json or len(request.json) != 1:
        abort(400)
    if request.json[0] in categories:
        categories.pop(request.json[0])
        return jsonify({}), 201
    else:
        abort(405)
#5
@app.route('/api/category/size', methods=['GET'])
def list_categories():
    print("Hallelujah in size")
    if not request.is_json or len(request.json) != 1:
        abort(400)
    if request.json[0] in categories:
        return jsonify([categories[request.json[0]]])
    else:
        abort(405)

if __name__ == '__main__':
    app.run(debug=True)