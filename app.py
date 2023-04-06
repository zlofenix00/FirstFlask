from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

@app.route("/")
def index():
    colors = ['red', 'blue', 'green', 'black']
    return render_template("index.html", colors = colors)
    # return redirect(url_for("about"))
  
@app.route("/about")
def about():
    return render_template("about.html")
  
if __name__ == "__main__":
    app.run(debug=True, port=5001)
    
