import re
UNITS_PATTERN = r"(?:cup|cups|tablespoon|tbsp|teaspoon|tsp|gram|g|kg|ml|l|pinch|dash|clove|cloves|slice|slices)"
QTY_PATTERN = rf"(\d+(?:/\d+|\.\d+)?\s*{UNITS_PATTERN}?|\bto taste\b|some|a little|a pinch of|a dash of|half a)"
text = "heat 2 tablespoons of olive oil and add sliced chicken".lower()
word = "olive oil"
safe_word_regex = re.escape(word)
pattern = rf"\b({QTY_PATTERN}(?:\s+of)?\s+)?{safe_word_regex}\b"
print("PATTERN:", pattern)
match = re.search(pattern, text)
print("MATCH:", match.groups() if match else "None")
