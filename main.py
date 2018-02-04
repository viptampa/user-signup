from flask import Flask, request
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True



@app.route('/')
def index():
    template = jinja_env.get_template('home.html')
    return template.render(username='', username_error='', password='', 
   password_error='', vpassword='', vpassword_error='', email='', email_error='')



@app.route('/',  methods=['POST'])
def validateinput():
    username = str(request.form['username'])
    password = str(request.form['password'])
    vpassword = str(request.form['vpassword'])
    email = str(request.form['email'])
    minlength = 3
    maxlength = 20

    username_error = ''
    password_error = ''
    vpassword_error = ''
    email_error = ''
    welcomemsg = "Welcome, " + username + "!"
    periodtoomuch = 0
    atsigntoomuch = 0
    spacetoomuch = 0

    if len(username) < minlength or len(username) > maxlength:
        username_error = "That's not a valid username"
        username = ""

    if len(password) < minlength or len(password) > maxlength:
        password_error = "That's not a valid password"
        password = ""

    if len(vpassword) < minlength or len(vpassword) > maxlength:
        vpassword_error = "Passwords don't match"
        vpassword = ""
    
    if vpassword != password:
        vpassword_error = "Passwords don't match"
        vpassword = ""

    if len(email) > 0:
        if len(email) < minlength or len(email) > maxlength:
            email_error = "That's not a valid email"
            email = ""
        for letter in email:
            if letter == ".":
                periodtoomuch += 1 
            if letter == "@":
                atsigntoomuch += 1
            if letter == " ":
                spacetoomuch += 1
        if periodtoomuch > 1 or atsigntoomuch > 1 or spacetoomuch > 0:
            email_error = "That's not a valid email"
            email = ""

    if not username_error and not password_error and not vpassword_error and not email_error:
        template = jinja_env.get_template('success.html')
        return template.render(username=username)
    else:
        template = jinja_env.get_template('home.html')
        return template.render(username_error=username_error, password_error
        =password_error, vpassword_error=vpassword_error, email_error=email_error,
        username=username, password="", vpassword="", email=email)

    

app.run(host='0.0.0.0')