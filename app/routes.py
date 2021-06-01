from app import app
import os 
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import pdfplumber

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    print('--upload-file-------------')
    if request.method == 'POST':
        f = request.files['file']
        all_text =''
        with pdfplumber.open(f) as pdf:
            print("------------", f)
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                all_text = all_text + '\n' + single_page_text
    print(all_text)
    f.save(secure_filename(f.filename))
    return render_template('result.html', data = all_text)
		