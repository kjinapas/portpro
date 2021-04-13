from flask import Flask
from flask import render_template
app = Flask(__name__)



@app.route('/<name>')
def Hello(name):
   return render_template("index.html",text=name)





if __name__ =="__main__":
    app.run()
