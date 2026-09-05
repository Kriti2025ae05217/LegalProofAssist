from spellchecker import SpellChecker
from backend.legal_dictionary import LEGAL_TERMS
from backend.bk_tree import BKTree

spell = SpellChecker()

tree = BKTree()

for word in LEGAL_TERMS:
    tree.add(word)


def check_spelling(text):

    words = text.split()

    errors = []

    for word in words:

        clean_word = word.lower().strip(".,;:")

        if clean_word in LEGAL_TERMS:
            continue

        if clean_word not in spell:

            suggestion = spell.correction(clean_word)

            confidence = 0.95

            legal_match = tree.search(clean_word)

            if legal_match:
                suggestion = legal_match[0][0]
                confidence = 0.98

            errors.append({
                "word": word,
                "suggestion": suggestion,
                "error_type": "Spelling",
                "confidence": confidence
            })

    return errors
