from transformers import pipeline
try:
    ner_pipeline = pipeline("ner", model="Dizex/InstaFoodRoBERTa-NER", aggregation_strategy="simple")
    print(ner_pipeline("Heat 2 tablespoons of olive oil and add sliced chicken"))
except Exception as e:
    print("ERROR:", e)
