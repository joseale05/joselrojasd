
import random

# 1. Asignar valores literales a las variables nombre del vendedor y el salario base
nombre_vendedor = "Juan Pérez"
salario_base = 1500 

# 2. Asignar valores aleatorios a las variables tarifa por hora y cantidad de horas trabajadas
cantidad_horas_trabajadas = random.randint(5, 40)  
tarifa_por_hora = random.randint(20, 50)  

# 3. Calcular el monto que percibe el vendedor por las horas trabajadas
monto_percibe_horas = cantidad_horas_trabajadas * tarifa_por_hora

# 4. Calcular el salario total del vendedor
salario_total = salario_base + monto_percibe_horas

# 5. Mostrar la información del vendedor en pantalla
print("Información del Vendedor:")
print("Nombre:", nombre_vendedor)
print("Salario Base:", salario_base)
print("Cantidad de Horas Trabajadas:", cantidad_horas_trabajadas)
print("Tarifa por Hora:", tarifa_por_hora)
print("Monto que Percibe por Horas Trabajadas:", monto_percibe_horas)
print("Salario Total:", salario_total)

