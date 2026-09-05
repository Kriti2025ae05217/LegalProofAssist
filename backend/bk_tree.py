def levenshtein(a, b):

    if len(a) < len(b):
        return levenshtein(b, a)

    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)

    for i, c1 in enumerate(a):
        current_row = [i + 1]

        for j, c2 in enumerate(b):

            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)

            current_row.append(
                min(insertions, deletions, substitutions)
            )

        previous_row = current_row

    return previous_row[-1]


class BKTree:

    def __init__(self):
        self.words = []

    def add(self, word):
        self.words.append(word)

    def search(self, word, threshold=2):

        results = []

        for w in self.words:

            dist = levenshtein(word, w)

            if dist <= threshold:
                results.append((w, dist))

        results.sort(key=lambda x: x[1])

        return results
