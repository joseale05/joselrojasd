import pytesseract
from PIL import Image

# Configurar el path de Tesseract (si no está en el PATH)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Reemplaza con tu path

# Cargar la imagen de la factura
image_path = 'ruta/de/tu/factura.jpg'
img = Image.open(image_path)

# Extraer el texto con Tesseract
text = pytesseract.image_to_string(img)

# Procesar el texto (ejemplo)
lines = text.split('\n')
precios = []
for line in lines:
    if 'precio' in line.lower() or 'total' in line.lower():
        try:
            # Extraer el precio (ejemplo con regex)
            precio = float(line.split(' ')[-1].replace(',', '.'))  # Reemplaza el separador decimal según la factura
            precios.append(precio)
        except ValueError:
            pass

# Mostrar los precios
print("Precios encontrados:")
for precio in precios:
    print(precio)