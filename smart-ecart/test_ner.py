from transformers import pipeline
try:
    ner_pipeline = pipeline("ner", model="rgonzale/recipe-ner-model", aggregation_strategy="simple")
    print(ner_pipeline("Heat 2 tablespoons of olive oil and add sliced chicken"))
except Exception as e:
    print("ERROR:", e)
