from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/save-sign', methods=['POST'])
def save_sign():
    sign = request.form['sign']
    
    with open('sign.txt', 'w') as file:
        file.write(sign)
    
    return jsonify({'message': 'Sign saved successfully'})

if __name__ == '__main__':
    app.run()
