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
            for pdf_page in pdf.pages:
                single_page_text = pdf_page.extract_text()
                all_text = all_text + '\n' + single_page_text
    print(all_text)
    f.save(secure_filename(f.filename))
    all_text = {
            "company_worked_at": "9X IT solutions", 
            "company_worked_at_yr": "from July-2013 to till date.", 
            "degree": "master of Degree (M.Tech", 
            "designation": "a Android Application Developer", 
            "email": "bellam.phani@gmail.com", 
            "name": "B.Phani kuamr", 
            "phone": "+91-9491702580", 
            "professional_summary": "d abilities in information technology Industry that offers professional growth and gain professional excellence while being resourceful, innovative and flexible. Involved in Coding and Development of business applications. Having 2 years of experience in developing applications using Android, Java. Good Experience on OOPs concepts and SQLite Database. Ability to work in a team as well as independently and quick at mastering new concepts and applications.", "roles_responsibilities": ") Involved in designing user interfaces using xml. Utilized Eclipse to build and deploy the application. Involved in Coding and Development of business applications.", "school_college": "SRM University in", "skills": " Ability to grasp new technologies quickly. Worked on common Android framework APIs. Employment Summary Working as in Education from Chennai during 2011-2013. Technical skills Programming languages : Core Java,HTML5,CSS3 Database Operating System : Windows IDE : Eclipse, Android Studio Key Skills HTML5,CSS3,Phonega : SQLite : JSON, MAPs, Custom views, Multithreding, Mobile Technologies: It is infra company application. Customers seek to plots, In this application shows Knowledge on Architecture, Android SDK, Application Lifecycle, Layouts, Views, Intents, Receivers, Audio, Video, SMS, Telephony, Data Storage and Locations, JSON, Maps, Custom views. Project #1: Title : Skanda Infra Projects Technologies : Android, Java, SQLite. Description: plots, plot area, facing and customer requirements. Sellers are updates available plots and it\u2019s details with this application. https://play.google.com/store/apps/details?id=skanda.skanda Project #2: Title : Vasavi Clubs International Technologies : Android, Java. Description: This community group application. It is hav e flash logo, navigation Drawer, List view item clickable licensers. It have communicate group members, Sharing ideas and Events everyone intimate in this application. https://play.google.com/store/apps/details?id=vasavi.clubs Project #3: Title Technologies : Android, Java, JSON Parsing, XML Description: Computer Society of India is the first and largest body of computer professionals in India. We create a CSI mobile application. It has a developed li ke CSI website. In this application will be upload button images, themes and links same as CSI website. It has been updates with server Responsibilities : Computer Society of India(CSI Date:", "stream": "(I.T))"}

    return render_template('result.html', data = all_text)
		