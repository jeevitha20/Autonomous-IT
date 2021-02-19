from application import app
from flask import render_template, request, json, Response

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/second",methods=["GET","POST"])
def second():
    return render_template("second.html")

@app.route("/main",methods=["GET","POST"])
def main():
    
    id = request.form.get('numofusers')
    var=request.form.get('sname')
    
    return render_template("main.html",data={"id":id,"s":var})
