from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
load_dotenv()
from db import obtener_productos, buscar_productos


# Configurar la clave de API
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


# Generar consulta para obtener productos de la base de datos
productos = buscar_productos("Monitor")
productos = buscar_productos("Lenovo")
productos = buscar_productos("Mouse")

#ingresar la consulta del cliente
consulta_cliente = input("Ingrese su consulta: ")
productos = buscar_productos(consulta_cliente)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"Estos son los productos disponibles: {productos}. Respondé al cliente utilizando únicamente la información proporcionada"    
    #contents=f"Productos:{productos} ¿Qué productos Lenovo tenemos?"
    #contents=f"Productos:{productos} ¿Qué mouse tenemos disponible?
    #contents=f"Productos:{productos} ¿Qué productos de la categoría 'Auriculares' tenemos?"
)
print(response.text)   