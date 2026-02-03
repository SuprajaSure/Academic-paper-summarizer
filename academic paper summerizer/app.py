from flask import Flask, render_template, request
from summarizer import summarize_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    summary = ""
    if request.method == "POST":
        paper_text = request.form["paper"]
        summary = summarize_text(paper_text)
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)
