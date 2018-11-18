from flask import Flask
from helper import is_isbn_or_key
app = Flask(__name__)
# 载入配置文件
app.config.from_object('config')

@app.route('/book/search/<q>/<page>')
def search(q,page):
    is_isbn_or_key(q)    
    return 'hello'
# open debug 
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)