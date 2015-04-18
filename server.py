import json, requests, os

from config import *
from libresearchdata import ResearchData
from data.User.models import PersonCollection, Person
from forms.User.forms import PersonForm
from flask import Flask, request, flash, render_template, session, redirect, Markup
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = SECRET_KEY

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if session.has_key('user'):
        return redirect(url_for('account'))
    else:
        person = None
        form = PersonForm()
        if request.method == 'POST':
            person = Person()
            person.select(email = request.form[form.expand_fn('Email')], password = request.form[form.expand_fn('Password')])
            form.fill(person)
        return render_template('login.html', form = Markup(form))

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
            json_data = data.to_json(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #This is temporary until we're saving to the database.
            session['data'] = json_data
            #Save data to a database table here.

            flash('File uploaded and processed successfully!')
    return render_template('file-upload.html')

@app.route('/research-data/', methods=['GET', 'POST'])
def research_data():
    data = session['data'] if session.has_key('data') else None
    return render_template('data-grid.html', data = data)

@app.route('/person/list/')
def person_list():
    person_collection = PersonCollection()
    person_collection.select(active = 'True')
    return render_template('person-list.html', person_collection = person_collection)

@app.route('/person/<guid>/')
def person(guid):
    person = Person()
    person.select(rs = guid)
    return render_template('person.html', person = person)

@app.route('/person/<guid>/edit/', methods=['GET', 'POST'])
def person_edit(guid):
    form = None
    if guid is not None:
        person = Person()
        form = PersonForm()
        if request.method == 'POST':
            form.fill(form.expand_fn(request.form, person))
        else:
            person.select(rs = guid)
            form.fill(person)
    else:
        flash('Error: No GUID present!')
    return render_template('person-edit.html', form = Markup(form))

if __name__ == '__main__':
    app.run()
