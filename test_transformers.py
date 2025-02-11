from transformers import AutoTokenizer, AutoModelForMaskedLM

# Testmodell
tokenizer = AutoTokenizer.from_pretrained("AI-Sweden-Models/roberta-large-1160k")
print("Transformers-modulen fungerar!")
