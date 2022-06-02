from flask import render_template, request, redirect, url_for, flash
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    tasks = list(Task.query.order_by(Task.id).all())
    return render_template("tasks.html", tasks=tasks)


@app.route("/categories/")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category/", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        try:
            db.session.add(category)
            db.session.commit()
            return redirect(url_for("categories"))
        except Exception as error:
            db.session.rollback()
            return error
    return render_template("add_category.html")


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        updated_category_name = request.form.get("category_name")
        if category.category_name != updated_category_name:
            category.category_name = updated_category_name
            try:
                db.session.commit()
                return redirect(url_for("categories"))
            except Exception as error:
                db.session.rollback()
                return error
        else:
            flash("Name not changed")

    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    try:
        db.session.delete(category)
        db.session.commit()
        return redirect(url_for("categories"))
    except Exception as error:
        db.session.rollback()
        return error


@app.route("/add_task/", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id"),
        )
        try:
            db.session.add(task)
            db.session.commit()
            return redirect(url_for("home"))
        except Exception as error:
            db.session.rollback()
            return error
    return render_template("add_task.html", categories=categories)
