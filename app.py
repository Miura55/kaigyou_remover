from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def split():
    html = render_template("index.html")
    return html

@app.route('/process',methods= ['POST'])
def process():
    before = request.form['before']
    after = before.replace("\n", " ")
    return jsonify({'output':after})


if __name__ == "__main__":
    app.run()
