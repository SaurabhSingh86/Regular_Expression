"""# Assignment 1:"""

""" Take an email as input from user and check it is personal account or work account"""


from flask import Flask, request, render_template
import re

app = Flask(__name__)


@app.route('/')
def user_input():
    return render_template("user_input.html")


@app.route('/success', methods=['POST', 'GET'])
def validate_data():
    if request.method == 'POST':
        email = request.form['Email']
        res = ""
        personal_email = ['gmail', 'hotmail', 'rediff', 'yahoo']

        if re.findall('[\w.+-_%]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}', email):
            domain_ = email.split('@')[-1]
            domain = domain_.split('.')[0]
            if domain in personal_email:
                res = f'{email} => is a personal account.'
            else:
                res = f'{email} => is a work account.'
        else:
            res = f'{email} => is invalid email account.'

        return render_template("result.html", res=res)


if __name__ == '__main__':
    app.run(debug=True)
