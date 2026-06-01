import sys
sys.path.append('backend')
from services.nlp_ner_service import extract_exact_ingredients
print("TESTING NER:")
print(extract_exact_ingredients("Heat 2 tablespoons of olive oil and add sliced chicken"))
