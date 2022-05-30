from enum import unique
from sqlalchemy import Column, ForeignKey
from taskmanager import db
from sqlalchemy_utils import generic_repr


@generic_repr
class Category(db.Model):
    # Schema for Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True
    )

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.category.name


@generic_repr
class Task(db.Model):
    # Schema for Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    dur_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("category.id", ondelete="CASCADE"),
        nullable=False,
    )

    # def __repr__(self):
    #     # __repr__ to represent itself in the form of a string
    #     return "#{0} - Task: {1} | Urgent: {2}".format(
    #         self.id, self.task_name, self.is_urgent
    #     )
