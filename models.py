# Load model directly
from transformers import AutoTokenizer, AutoModelForMaskedLM


#Embeddingsmoddels
tokenizer = AutoTokenizer.from_pretrained("AI-Sweden-Models/roberta-large-1160k")
model = AutoModelForMaskedLM.from_pretrained("AI-Sweden-Models/roberta-large-1160k")