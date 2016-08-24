from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey, Boolean, Unicode, Date
from sqlalchemy.orm import relationship
from todoapp import app

db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = "todo"
    id = Column('id', Integer, primary_key=True)
    category_id = Column('category_id', Integer, ForeignKey('category.id'))
    priority_id = Column('priority_id', Integer, ForeignKey('priority.id'))
    description = Column('description', Unicode)
    creation_date = Column('creation_date', Date, default=datetime.utcnow)
    is_done = Column('is_done', Boolean, default=False)

    priority = relationship('Priority', foreign_keys=priority_id, backref="todos")
    category = relationship('Category', foreign_keys=category_id, backref="todos")


class Priority(db.Model):
    __tablename__ = "priority"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode)
    value = Column('value', Integer)

    def __repr__(self):
        return "<id: %r, name: %r, value: %r>" %(self.id, self.name, self.value)


class Category(db.Model):
    __tablename__ = "category"
    id = Column('id', Integer, primary_key=True)
    name = Column('name', Unicode)

    def __repr__(self):
        return "<id: %r, name: %r>" %(self.id, self.name)
