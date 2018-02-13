from app import db

class SignUp(db.Model):
    __tablename__ = "signup"
    ID = db.Column(db.Integer, primary_key=True)
    Firstname = db.Column(db.VARCHAR(200))
    Lastname = db.Column(db.VARCHAR(200))
    Username = db.Column(db.VARCHAR(200), unique=True)
    Password = db.Column(db.VARCHAR(200))
    Phonenumber = db.Column(db.VARCHAR(200))
    Email = db.Column(db.VARCHAR(200), unique=True)
    Gender = db.Column(db.String(10))

    def __init__(self, Firstname, Lastname, Username, Password, Phonenumber, Email, Gender):
        self.Firstname = Firstname
        self.Lastname = Lastname
        self.Username = Username
        self.Password = Password
        self.Phonenumber = Phonenumber
        self.Email = Email
        self.Gender = Gender

# db.create_all()


class Login(db.Model):
    __tablename__ = 'login'
    id = db.Column(db.Integer, primary_key=True)
    Username = db.Column(db.VARCHAR(200))
    Password = db.Column(db.VARCHAR(200))
    business = db.relationship('BusinessCategory', backref='owner', lazy ='dynamic')

    def __init__(self, Username, Password):
        self.Username = Username
        self.Password = Password

    def __repr__(self):
        return '<User %r>'%self.Username


class BusinessCategory(db.Model):
    __table__name = 'businesscategory'
    id = db.Column(db.Integer, primary_key=True)
    businessname = db.Column(db.VARCHAR(200))
    category = db.Column(db.VARCHAR(200))
    location = db.Column(db.VARCHAR(200))
    owner_id = db.Column(db.Integer, db.ForeignKey('login.id'))

    def __init__(self, businessname, category, location):
        self.businessname = businessname
        self.category = category
        self.location = location

db.create_all()