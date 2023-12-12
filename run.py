from flask import Flask, render_template, request, session, g
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config.update(
    SECRET_KEY='hllhcs',  # ! password for
    SQLALCHEMY_DATABASE_URI='postgresql://postgres:hllhcs@localhost/loginTable_db',
    # SQLALCHEMY_DATABASE_URI='<dbName>://<username>:<password>@localhost/<dbName>',
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)


db = SQLAlchemy(app)


#! Before Request
@app.before_request
def someFunction():
    g.string = '<br>This Code ran before any request'


# ! BASIC ROUTE
@app.route('/')
@app.route('/login')
def loginPage():
    return render_template('loginPage.html', g.string)


# ! Route for Distance Based Conveyance Form
@app.route('/conveyanceForm/<name>/<empCode>')
@app.route('/conveyanceForm/<name>/<empCode>/')
def distanceBasedConveyanceEntry(name='Archin Deepak', empCode='THLL0001'):
    return render_template('distanceFormPage.html', name=name, empCode=empCode)


# ! Route for non-distance Based Conveyance Form
@app.route('/conveyanceForm/<name>/<empCode>/a')
@app.route('/conveyanceForm/<name>/<empCode>/a/')
def conveyanceEntry(name, empCode):
    return render_template('formPage.html', name=name, empCode=empCode)


# ! Route to select which records to view
@app.route('/records/<name>/<empCode>')
@app.route('/records/<name>/<empCode>/')
def recordView(name, empCode):
    return render_template('recordPage.html', name=name, empCode=empCode)


# ! Route to view records of selected month and year
@app.route('/records/<name>/<empCode>/<month>/<year>')
@app.route('/records/<name>/<empCode>/<month>/<year>/')
def individualRecordView(name, empCode, month, year):
    return render_template('recordViewPage.html', name=name, empCode=empCode, month=month, year=year)


#! session object
@app.route('/session')
@app.route('/session/')
def sessionData():
    if 'name' not in session:
        session['name'] = 'harry'
    return render_template('session.html', session=session, name=session['name'])


# ! For creating and working on a database named users
class User(db.Model):
    __tablename__ = 'users'

    ID = db.Column(db.String(10), primary_key=True, unique=True)
    name = db.Column(db.String(80), nullable=False)
    # userName = db.Column(db.String(80), nullable=False, unique=True)
    # password = db.Column(db.String(80), nullable=False)
    # privileges = db.Column(db.Boolean, nullable=False)

    def __init__(self, ID, name) -> None:
        self.ID = ID
        self.name = name

    def __repr__(self) -> str:
        return 'The ID is {}, Name is {}'.format(self.ID, self.name)


# ! For creating and working on a database named conveyance
class Conveyance(db.Model):
    __tablename__ = 'conveyance'

    ID = db.Column(db.Integer, primary_key=True)
    From = db.Column(db.String(80), nullable=False)
    To = db.Column(db.String(80), nullable=False)
    Distance = db.Column(db.String(5), nullable=False)
    Date = db.Column(db.DateTime, nullable=False, index=True)
    Day = db.Column(db.String(10), nullable=False)
    Amount = db.Column(db.Integer, nullable=False)

    #! Relationship
    empCode = db.Column(db.String(10), db.ForeignKey('users.ID'))

    def __init__(self, From, To, Distance, Date, Day, Amount, empCode) -> None:
        self.From = From
        self.To = To
        self.Date = Date
        self.Day = Day
        self.Distance = Distance
        self.Amount = Amount
        self.empCode = empCode

    def __repr__(self) -> str:
        return '{} to {} : Travel of {}km'.format(self.From, self.To, self.Distance)


# ! main function
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
