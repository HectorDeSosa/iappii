from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()

# Configurar la clave de API
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Generar contenido simple
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explicá qué es una computadora"
    #contents="¿Cómo está el clima en Madrid?"
    #contents="Explica la teoría de la relatividad en una frase."
    #¿Cómo está el clima en Madrid?
    #¿Cuánto es 12 × 12?
    #Explicá qué es una computadora
    #¿Que es Ngrok y para que sirve?
    
)
print(response.text)   