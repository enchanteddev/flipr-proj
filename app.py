from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from dbwrapper import get_data, get_close_data, get_stock_min_max, get_stock_open_close

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return send_from_directory('dist', 'index.html')

@app.route("/raw/<string:stockname>:<int:days>")
def get_raw_stock_info(stockname: str, days: int):
    return jsonify([x for x in get_data(stockname.upper(), days)])

@app.route("/close/<string:stockname>:<int:days>")
def get_close_stock_info(stockname: str, days: int):
    return jsonify([x for x in get_close_data(stockname.upper(), days)])

@app.route("/maxmin/<string:stockname>:<int:days>")
def get_max_min_stock_info(stockname: str, days: int):
    return jsonify(get_stock_min_max(stockname.upper(), days))

@app.route("/openclose/<string:stockname>:<int:date>")
def get_open_close_info(stockname: str, date: int):
    return jsonify(get_stock_open_close(stockname.upper(), date))

@app.route("/assets/<path:path>")
def get_static(path: str):
    return send_from_directory('dist/assets', path)