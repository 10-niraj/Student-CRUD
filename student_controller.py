from flask import render_template,request,redirect,url_for
from app import app,db
from models.student import Student


@app.route("/")
def index():
    students = Student.query.all()
    return render_template("index.html", students=students)

@app.route("/add",methods=["POST"])
def add():
        id=request.form['id']
        name=request.form["name"]
        email=request.form["email"]
        contact=request.form["contact"]
        course=request.form["course"]
        s= Student (id=id,name=name,email=email,contact=contact,course=course)

        db.session.add(s)
        db.session.commit()
        return redirect("/")

@app.route('/delete/<int:id>')
def delete(id):
    student = Student.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect("/")

@app.route('/edit/<int:id>')
def edit(id):
    students = Student.query.get(id)
    return render_template("edit.html",student=students)

@app.route('/upadte/<int:id>',methods=["POST"])
def update(id):
    students= Student.query.get(id)
    
    Student.id =request.form["id"]
    Student.name =request.form["name"]
    Student.email =request.form["email"]
    Student.contact =request.form["contact"]
    Student.course =request.form["course"]
    
    db.session.commit()
    return redirect("/")