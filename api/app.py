from flask import Flask, json,jsonify,request
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import Serializer
from marshmallow import Schema,fields
from dotenv import load_dotenv
from flask_cors import CORS


import os

load_dotenv()
user=os.getenv('user')
password=os.getenv('password')

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://'+user+':'+password+'@db:3306/test_db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

###Models####
class Book(db.Model):

    __tablename__ = "Books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    autor = db.Column(db.String(100))

    def __repr__(self):
        return '' % self.id

    @classmethod
    def get_books(cls):
        return cls.query.all()

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

class BookSchema(Schema):
    id= fields.Integer()
    title= fields.String()
    autor= fields.String()

@app.route('/book',methods = ['GET'])
def listBooks():
    books = Book.get_books()
    serializer=BookSchema(many=True)
    data = serializer.dump(books)
    return jsonify(data),201

@app.route('/create',methods = ['POST'])
def create_book():
    data = request.get_json()
    new_book = Book(
        id=data.get('id'),
        title=data.get('title'),
        autor=data.get('autor')
    )
    new_book.create()
    serializer=BookSchema()
    data = serializer.dump(new_book)
    return jsonify(data),201

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)