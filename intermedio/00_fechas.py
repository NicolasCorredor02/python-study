### FECHAS ###

from datetime import datetime, timedelta
import locale


# 1. Obtener una fecha y hora actual
now = datetime.now()
print(f"Fecha y hora actual: {now}")

# 2. Crear una fecha y hora especifica
specific_date = datetime(2023, 1, 1, 12, 0, 0) # año, mes, dia, hora, minuto, segundo
print(f"Fecha y hora especifica: {specific_date}")

# 3. Formatear fechas
# Para formatear una fecha, se utiliza el método strftime() de la clase datetime
# Se pasa el objeto datetime como argumento y se especifica el formato de la fecha deseada
locale.setlocale(locale.LC_TIME, 'es_CO.UTF-8') # Establece el locale para español de Colombia
# formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")
formatted_date = now.strftime("%A %B %Y %H:%M:%S")
print(f"Fecha formateada: {formatted_date}")

# 4. Operaciones con fechas
# Se pueden realizar operaciones como sumar o restar fechas
yesterday = now - timedelta(days=1)
print(f"Fecha de ayer: {yesterday}")

tomorrow = now + timedelta(days=1)
print(f"Fecha de mañana: {tomorrow}")

one_hour_after = now + timedelta(hours=1)
print(f"Fecha en una hora: {one_hour_after}")

# 5. Obtener componentes individuales de una fecha
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
second = now.second
print(f"Año: {year}, Mes: {month}, Día: {day}, Hora: {hour}, Minuto: {minute}, Segundo: {second}")

# 6. Calcular diferencia entre dos fechas
date_1 = datetime.now()
date_2 = datetime(2023, 1, 1, 12, 0, 0) # año, mes, dia, hora, minuto, segundo

difference = date_1 - date_2
print(f"Diferencia entre las fechas: {difference}")

# 7. Fechas en otros 
# Se pueden trabajar con fechas en otros formatos, como ISO 8601
iso_date = datetime.now().isoformat()
print(f"Fecha ISO 8601: {iso_date}")