from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
            .error {{ color: red;}}
        </style>
    </head>
    <body>
    <form method="POST">
            <label><h1>UserSignup</h1></label>
            <label>Username:
            <input type="text" name="username" value="{username}"></label>
            <p class="error">{username_error}</p>
            <br><br>
            <label>Password:
            <input type="text" name="password" value="{password}"></label>
            <p class="error">{password_error}</p>
            <br><br>
            <label>Verify Password:
            <input type="text" name="vpassword" value="{vpassword}"></label>
            <p class="error">{vpassword_error}</p>
            <br><br>
            <label>Email (optional):
            <input type="text" name="email" value="{email}"></label>
            <p class="error">{email_error}</p>
            <br><br>
            <input type="submit" value="Validate" />
        </form>
    </body>
</html>"""

@app.route('/',  methods=['GET'])
def display_input_form():
    return form.format(username='', username_error='', password='', 
   password_error='', vpassword='', vpassword_error='', email='', email_error=''
     )


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

    if len(username) < minlength or len(username) > 20:
        username_error = "That's not a valid username"
        username = ""

    if len(password) < minlength or len(password) > 20:
        password_error = "That's not a valid password"
        password = ""

    if len(vpassword) < minlength or len(vpassword) > 20:
        vpassword_error = "Passwords don't match"
        vpassword = ""
    
    if vpassword != password:
        vpassword_error = "Passwords don't match"
        vpassword = ""

    if not username_error and not password_error and not vpassword_error:
        return welcomemsg
    else:
        return form.format(username_error=username_error, password_error
        =password_error, vpassword_error=vpassword_error, email_error=email_error,
        username=username, password=password, vpassword=vpassword, email=email)

    

app.run(host='0.0.0.0')