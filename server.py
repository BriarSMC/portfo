from flask import Flask, render_template, request, redirect, url_for
import os
from slugs import *
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return path('index')

@app.route('/<path>')
def path(path):
    print(f"Route: {path}")
    if not check_slug(path): return redirect('404')

    return  render_template(f"/{return_file(path)}")

@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            print(data)
            store_contact_csv(data["email"], data["subject"], data["message"])
            pass
            return redirect('thankyou')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong with POST.'


def store_contact_msg(email, subject, message):
    with open("database.txt", "a") as fd:
        fd.write(f"{email}, {subject}, {message}\n")

def store_contact_csv(email, subject, message):
    with open("database.csv", "a") as fd:
        csv_writer = csv.writer(fd, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])