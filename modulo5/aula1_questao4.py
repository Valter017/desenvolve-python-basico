import datetime
import pytz

brasilia_tz = pytz.timezone('America/Sao_Paulo')

now_utc = datetime.datetime.now(pytz.utc)

now_brasilia = now_utc.astimezone(brasilia_tz)

day = now_brasilia.day
month = now_brasilia.month
year = now_brasilia.year
hour = now_brasilia.hour
minute = now_brasilia.minute

print(f"Data: {day:02d}/{month:02d}/{year}")
print(f"Hora: {hour:02d}:{minute:02d}")
