import json
import requests
import os

from config import *
from libresearchdata import ResearchData
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
            #Save file to filesystem.
            #Flask saves large files to a temporary file anyway,so no point in just using a stream.
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            #The ResearchData class/object will eventually house shortcut methods for processing.
            data = ResearchData('csv')
            data.to_xml(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #Save data to a database table here.

            flash('File uploaded and processed successfully!')
    return render_template('file-upload.html')

if __name__ == '__main__':
    app.run()
