import os
from flask import Flask, request, redirect, url_for,render_template
from werkzeug.utils import secure_filename
from flask import flash
from flask import Session
from dominant_color import*
#from detect_dress import *
from flask import Markup

UPLOAD_FOLDER = 'flaskr/static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
sess = Session()
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = '1001rs'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])

def upload_file():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
       
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            
            a=colorz(file.filename)
            print a
            #a=Markup(a)
            #flash("rashmi")
            filename = secure_filename(file.filename)
            
            #print colorz(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            return redirect(url_for('upload_file',filename=filename))

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
   
    app.config['SESSION_TYPE'] = 'filesystem'

    sess.init_app(app)

    app.debug = True
    app.run()