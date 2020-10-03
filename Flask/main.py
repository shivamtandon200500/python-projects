from flask import Flask,render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import json,os,math
from werkzeug.utils import secure_filename
with open('config.json','r') as c:
    params=json.load(c)["params"]

local_server= True
x=Flask(__name__)
x.secret_key = 'super-secret-key'
x.config['UPLOAD_FOLDER']=params['upload_location']
x.config.update(
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = params['gmail-user'],
    MAIL_PASSWORD=  params['gmail-password']
)
mail = Mail(x)
if(local_server):
    x.config['SQLALCHEMY_DATABASE_URI']=params['local_uri']
else:
    x.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(x)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(12), nullable=False)
    phone_num = db.Column(db.String(120), nullable=False)
    mes = db.Column(db.String(12), nullable=False)
    date = db.Column(db.String(20), nullable=True)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    slug = db.Column(db.String(21), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(12), nullable=True)
    img_file = db.Column(db.String(12), nullable=True)
    subtitle=db.Column(db.String(22), nullable=True)

@x.route("/")
def home():
    posts = Posts.query.filter_by().all()
    last=math.ceil(len(posts)/int(params['number_of_post']))
    page=request.args.get('page')
    if(not str(page).isnumeric()):
        page=1
    page=int(page)
    posts=posts[(page-1)*int(params['number_of_post']):(page-1)*int(params['number_of_post'])+int(params['number_of_post'])]
    if page==1:
        prev="#"
        next="/?page="+str(page+1)
    elif page==last:
        prev="/?page="+str(page-1)
        next="#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)


    return render_template('index.html',params=params,posts=posts,prev=prev,next=next)
@x.route("/support")
def support():
    return render_template('support.html',params=params)


@x.route("/about")
def about():
    return render_template('about.html',params=params)

@x.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if 'user' in session and session['user']==params['admin_user']:
        posts = Posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)
    if request.method=='POST':
        username=request.form.get('uname')
        useerpass=request.form.get('pass')
        if username==params['admin_user'] and useerpass==params['admin_password']:
            session['user']=username
            posts=Posts.query.all()
            return render_template('dashboard.html',params=params,posts=posts)

    return render_template('login.html',params=params)

@x.route("/edit/<string:sno>",methods=["GET","POST"])
def edit(sno):
    if 'user' in session and session['user']==params['admin_user']:
        if request.method=='POST':
            box_title=request.form.get('title')
            tline=request.form.get('tline')
            slug=request.form.get('slug')
            content=request.form.get('content')
            img_file=request.form.get('img_file')
            date=datetime.now()
            if sno=='0':
                post=Posts(title=box_title,slug=slug,content=content,img_file=img_file,date=date,subtitle=tline)
                db.session.add(post)
                db.session.commit()
            else:
                post=Posts.query.filter_by(sno=sno).first()
                post.title=box_title
                post.slug=slug
                post.content=content
                post.img_file=img_file
                post.date=date
                post.subtitle=tline
                db.session.commit()
                return redirect('/edit/'+sno)
        post = Posts.query.filter_by(sno=sno).first()
        return render_template('edit.html',params=params,post=post,sno=sno)

@x.route("/uploader", methods=["GET","POST"])
def uploader():
    if 'user' in session and session['user']==params['admin_user']:
        if request.method == 'POST':
            f=request.files['file1']
            f.save(os.path.join(x.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
            return "Uploaded Successfully"
@x.route("/logout")
def logout():
    session.pop('user')
    return  redirect('/dashboard')
@x.route("/delete/<string:sno>",methods=["GET","POST"])
def delete(sno):
    if 'user' in session and session['user'] == params['admin_user']:
        post=Posts.query.filter_by(sno=sno).first()
        db.session.delete(post)
        db.session.commit()
    return redirect('/dashboard')

@x.route("/contact", methods=["GET","POST"])
def contact():
    if request.method=='POST':
        '''Add entries'''
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        message=request.form.get('message')
        entry=Contacts(name=name,email=email,phone_num=phone,date=datetime.now(),mes=message)
        db.session.add(entry)
        db.session.commit()
        mail.send_message('New message from ' + name,
                          sender=email,
                          recipients=[params['gmail-user']],
                          body=message + "\n" + phone
                          )
    return render_template('contact.html',params=params)

@x.route("/post/<string:post_slug>", methods=["GET"])
def post_route(post_slug):
    post =Posts.query.filter_by(slug=post_slug).first()

    return render_template('post.html',params=params,post=post)

x.run(debug=True)