# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)
# configuration
DEBUG = True # CHANGE BEFORE UPLOADING TO PRODUCTION

@app.route('/', methods=['GET'])
def show_index():
    return render_template('index.html')

#@app.route('/blog', methods=['GET'])
#def show_blog():
#    return render_template('blog.html')


if __name__ == '__main__':
    app.run()
