import cv2
import pytesseract
#Ejecutable de Tesseract OCR
#https://github.com/UB-Mannheim/tesseract/wiki

# Ubicación de Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
imagen = cv2.imread("prueba.png")

print(type(imagen))
print(imagen.shape)

texto = pytesseract.image_to_string(imagen)

print(texto)