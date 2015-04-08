import json
import requests
import os
import csv

from config import * 
from flask import Flask, request, flash, render_template
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/file-upload/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            #You do not need to actually save the file
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), 'rb') as csvfile:
                rows = csv.reader(csvfile, delimiter=',')
                for column in rows:
                    print(', '.join(column))
                    #Process here
            flash('File uploaded and processed successfully!')
    return render_template('file-upload.html')

if __name__ == '__main__':
    app.run()
