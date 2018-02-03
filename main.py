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
        </style>
    </head>
    <body>
    <form action="" method="POST">
            <label><h1>UserSignup</h1></label>
            <label>Username:
            <input type="text" name="username" value="0"></label><br><br>
            <label>Password:
            <input type="text" name="password" value="0"></label><br><br>
            <label>Verify Password:
            <input type="text" name="vpassword" value="0"></label><br><br>
            <label>Email (optional):
            <input type="text" name="email" value="0"></label><br><br>
            <input type="submit" />
        </form>
    </body>
</html>"""

@app.route("/")
def index():
    return form.format("")
@app.route("/",  methods=['POST'])
def encrypt():
    oldtext = str(request.form['text'])
    int_rot = int(request.form['rot'])
    encryptedtext = rotate_string(oldtext, int_rot)
    encryptedtext = "<h1>" + encryptedtext + "</h1>"
    return encryptedtext

app.run(host='0.0.0.0')