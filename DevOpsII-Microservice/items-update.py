from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)
@app.route('/items_update', methods=['PUT'])
def update():
    # Get the user's login information from the request
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    _user = us.find_items_name(name)
    if _user:
        us.update_items(name,category,price,instock)
        return jsonify({'message': 'Update successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot update.'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True) #127.0.0.1