from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    reply=""
    if request.method=="POST":
        msg=request.form.get("message","")
        reply=f"You said: {msg}"
    return render_template("index.html", reply=reply)

if __name__=="__main__":
    app.run(debug=True)
