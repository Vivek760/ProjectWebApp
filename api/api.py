from flask import Flask, redirect, url_for,render_template, request
import os
import json
# from flask_jsglue import JSGlue
from werkzeug import secure_filename

app = Flask(__name__)
# jsglue = JSGlue(app)

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return  "Success!"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    ''' 
@app.route('/final')
def hello_admin():
    os.system("python3 dummy.py")
    f = open("labels.txt","r")
    st = f.read()
    data = st.split()

    return render_template("ListCategories.html",data=json.dumps(data))
    f.close()

#Read the output Images from the Output Folder
# @app.route('/output')
# def hello_guest():
#     st = ""
#     #Read the names of the Images.
#     f = open("ImageNames.txt","r")
#     st = f.read()
#     return 'files are: %s' % st
#     f.close()

@app.route('/reqjson',methods=['POST'])
def pass_val():
    name=request.form['canvas_data']
    print(name)
    f = open("./reqd_images.txt","w")
    f.write(name)
    f.close()
    return 'Success'



if __name__ == '__main__':
   app.run()