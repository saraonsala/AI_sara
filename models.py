import transformers
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

URL:http://127.0.0.1:1234

model_id = "AI-Sweden-Models/Llama-3-8B-instruct-Q4_K_M-gguf"

pipeline = transformers.pipeline(
    task="text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto"
)

pipeline(
    text_inputs="Sommar och sol är det bästa jag vet",
    max_length=128,
    repetition_penalty=1.03
)




#Embeddingsmoddels
tokenizer = AutoTokenizer.from_pretrained("AI-Sweden-Models/roberta-large-1160k")
model = AutoModelForMaskedLM.from_pretrained("AI-Sweden-Models/roberta-large-1160k")
