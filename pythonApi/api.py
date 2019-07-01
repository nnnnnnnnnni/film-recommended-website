# coding:utf-8
import sys
from flask import Flask, jsonify,request,make_response
sys.path.append('../')
from spider import poplist,search
from db import login,flim

app = Flask(__name__)
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,session_id')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,HEAD')
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/api/pop', methods=['GET'])
def get_pop():
    return jsonify(poplist.pop_list())

@app.route('/api/search',methods=['GET'])
def get_result():
    key=request.args.get('key')
    return jsonify(search.search(key))

@app.route('/api/login',methods=['POST'])
def get_login():
    username = request.args.get('username')
    password = request.args.get('password')
    return jsonify(login.login(username,password))
    
@app.route('/api/itemcf',methods=['GET'])
def get_itemcf():
    key=request.args.get('userid')
    return jsonify(flim.itemcf(key))

@app.route('/api/rmd',methods=['GET'])
def get_rmd():
    key=request.args.get('userid')
    return jsonify(flim.rmd(key))

@app.route('/api/tp',methods=['GET'])
def get_tp():
    key=request.args.get('userid')
    tp=request.args.get('cls').split('/')
    return jsonify(flim.tp(key,tp))

if __name__ == '__main__':
    app.run(debug=True)