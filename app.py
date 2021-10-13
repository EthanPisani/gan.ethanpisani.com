import sys
from random import randint
from flask import Flask, render_template, request
from numpy.lib.function_base import append
app = Flask(__name__)
import glob
import random
import json
files=[]
for name in glob.glob("./static/gan/*"):
    files.append(name)

print(len(files))
@app.route("/", methods=['GET', 'POST'])
def index():
    img=random.choice(files)
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Random') == 'Random':
            print("BUTTON")
            img=random.choice(files)
            
    return render_template("html/index.html", name=img)
@app.route("/grid", methods=['GET', 'POST'])
def grid():
    return render_template("html/grid.html", test=files)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4545)