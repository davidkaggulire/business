from flask import render_template, url_for, redirect, request

from app import app, forms
from app.forms import SignupForm, Loginform, Businessform
from app.models import db, Login, SignUp

@app.route('/')
@app.route('/base')
def home():
    return render_template('base.html')

@app.route('/details')
def details():
    return render_template('details.html')



@app.route('/login', methods=['GET', 'POST'])
def login():
    log = Loginform()
    if request.method == 'GET':
        return render_template('login.html', form = log)

    elif request.method == 'POST':
        username = log.Username.data
        password = log.Password.data
        messageFail = 'INVALID USERNAME OR PASSWORD'
        messagePass = 'You have successfully logged in'
        user = Login.query.filter_by(Username = username).first()
        if user:
            if(user.Password == password):
                # return redirect(url_for('details'))
                return render_template("login.html", form=log, message=messagePass)
            else:
                return render_template( "login.html", form = log, message = messageFail)
                print(messageFail)

        # if user and user.Password:
        #     # return redirect(url_for('details'))
        #     return render_template("login.html", form=log, message=messagePass)
        else:
            return render_template( "login.html", form = log,message= messageFail)
            print(messageFail)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    sign = SignupForm()
    if request.method == 'GET':
        return render_template('signup.html', form = sign)

    elif request.method == 'POST':
        firstname = sign.firstname.data
        lastname = sign.lastname.data
        username = sign.username.data
        password = sign.password.data
        email = sign.email.data
        gender = sign.gender.data
        phonenumber = sign.phonenumber.data

        user_Signup = SignUp(Firstname=firstname, Lastname= lastname, Username=username,
                             Password=password, Email=email,Gender=gender, Phonenumber=phonenumber )
        # adding user_insert to signup table                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        db.session.add(user_Signup)
        db.session.add(user_Signup)

        user_Login = Login(Username=username, Password=password)
        #adding to login table
        db.session.add(user_Login)
        db.session.commit()

        #messageSuccess = "You have successfully signed up"
        return render_template('index.html')

    else:
        messageFail = "Wrong request"
        return messageFail

@app.route('/regbusiness', methods=['GET', 'POST'])
def regBusiness():
    form = Businessform()
    if request.method == 'GET':
        return render_template('regbusiness.html', form = form)
    elif request.method == 'POST':
        businessname = form.Businessname.data
        business_category = form.Businesscategory.data
        business_location = form.Location.data

        user_business = Businessform(Businessname=businessname, Businesscategory = business_category,
                            Location=business_location)
        db.session.add(user_business)
        db.session.commit()

        return render_template('details.html')


@app.route('/user/<username>')
def show_user(username):
    user = Login.query.filter_by(Username=username).first()
    return render_template('index.html', user  = user)

