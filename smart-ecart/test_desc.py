import re

text = '''
Eggs - 2
Bread slices - 2
Onion (finely chopped) - ~1/4 cup
Green chilli (chopped) - 1-2
Butter / Oil - 1-2 tbsp
'''
lines = text.split('\n')
for line in lines:
    line = line.strip()
    if not line: continue
    
    # Try to extract "Ingredient - Quantity" or "Ingredient : Quantity"
    # Matches letters/spaces/parentheses, then a separator, then numbers/units
    match = re.match(r'^([a-zA-Z\s\(\)]+?)\s*[-:–]\s*(.*?)$', line)
    if match:
        ing = match.group(1).strip()
        qty = match.group(2).strip()
        print(f"ING: {ing} | QTY: {qty}")
