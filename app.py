from flask import Flask, request, url_for, redirect, render_template, jsonify
import json

'''Key Learning Goals
1. Defining routes and navigation between routes
2. Jinjas2 templating
3. Processing data from forms
4. Simple data storage using json
5. Build a fully functional app

Overview:
- Backend for login
- Backend for signup
- Backend for home page
- Backend for task entry page
- Rendering for home page
- Rendering for index page
- 22 items to complete
'''

app=Flask(__name__)

'''Allows users to go to the index page'''
@app.route("/")
def index():
    return render_template("index.html") 

'''Allows users to choose whether to login or sign up'''
@app.route("/authenticate")
def authenticate():
    return render_template("authenticate.html")

'''Allows users to login'''
@app.route("/login")
def login():
    return render_template("login.html")

'''Allows users to sign up'''
@app.route("/signup")
def signup():
    return render_template("signup.html")

'''Allows entries into the Todo List'''
@app.route("/entry")
def entry():
    return render_template("entry.html")

@app.route("/home",methods=["GET","POST"])
def home():
    tasks = ["Cleaning the dishes", "Walking the dog", "Cooking dinner", "Playing basketball", "Practicing piano"]

    with open("tasks.json", "r") as f:
        tasks=json.load(f)


    if request.method=="POST":
        
        data=request.form
        
        username=data["username"]
        password=data["password"]
        
        with open("user.json","r") as f:
            db_data = json.load(f)
            db_username = db_data["username"]
            db_password = db_data["password"]
            
        if username==db_username and password==db_password:
            
            return render_template("home.html", tasks=tasks, name=username)

    return render_template("error.html")

@app.route("/confirm-entry",methods=["POST","GET"])
def confirm_entry():
    
    if request.method=="POST":
        tasks=request.form.getlist("task")
        print(tasks)
        
        with open("tasks.json","w") as f:
            json.dump(tasks,f)
    
    return render_template("confirm-entry.html")

@app.route("/confirm-signup", methods=["POST","GET"])
def confirm_signup(): # Do not save passwords as strings
    if request.method=="POST":
        
        data=request.form
        
        user={}
        user["username"] = data["username"]
        user["password"] = data["password"]
        user["email"] = data["email"]
        
        print(user)
        
        with open("user.json", "w") as f:
            json.dump(user,f)
        return redirect(url_for("login"))
        
    return render_template("confirm-signup.html")

if __name__=="__main__":
    app.run(debug=True) #Never run as debug=True in a production environment


