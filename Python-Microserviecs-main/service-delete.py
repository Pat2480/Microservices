from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)
@app.route('/delete', methods=['DELETE'])
def delete():
    try:

        # Get the user's login information from the request
        username = request.form.get('username')
        _user = us.find_username(username)
        if _user:
            us.delete_user(username)
            return jsonify({'message': 'Delete Successful.'}), 200
        else:
            return jsonify({'message': 'Cannot Delete.'}), 401
    except:
        return jsonify({'message': 'Cannot found username.'}), 401
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1