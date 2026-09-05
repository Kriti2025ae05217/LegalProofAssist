from flask import Flask, render_template, request, jsonify
from backend.spell_checker import check_spelling
from backend.grammar_checker import check_grammar

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/check', methods=['POST'])
def check():

    data = request.get_json()

    clause_id = data.get('clause_id', '')
    text = data.get('text', '')

    spelling_errors = check_spelling(text)
    grammar_errors = check_grammar(text)

    all_errors = spelling_errors + grammar_errors

    return jsonify({
        "clause_id": clause_id,
        "issues": all_errors
    })


if __name__ == '__main__':
    app.run(debug=True)
