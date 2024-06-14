from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

engine=create_engine('sqlite:///database.db')
basee=declarative_base()



class Student(basee):
    __tablename__='student'
    _id=Column('id3',Integer,unique=True,primary_key=True)
    name=Column('name',String(50))




basee.metadata.create_all(engine)