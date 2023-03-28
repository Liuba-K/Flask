from sqlalchemy import Column, Integer, ForeignKey, String, Text, DateTime, func
from sqlalchemy.orm import relationship
#from blog.models.database import db
from datetime import datetime
from blog.models.database import db


class Article(db.Model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('authors.id'))

    author = relationship('Author', back_populates='articles')
