from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

from backend.spell_checker import check_spelling
from backend.grammar_checker import check_grammar

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():

    data = request.get_json()

    clause_id = data["clause_id"]
    text = data["text"]

    spell_errors = check_spelling(text)

    grammar_errors = check_grammar(text)

    results = spell_errors + grammar_errors

    return jsonify({
        "clause_id": clause_id,
        "results": results
    })


if __name__ == "__main__":
    app.run(debug=True)
