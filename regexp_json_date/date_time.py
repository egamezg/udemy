from datetime import datetime

dateandtime = datetime.now()

print(dateandtime)

año = dateandtime.year
mes = dateandtime.month
dia = dateandtime.day

hora = dateandtime.hour
minutes = dateandtime.minute
seconds = dateandtime.second
microseconds = dateandtime.microsecond

print(f"La hora es {hora}:{minutes}:{seconds}")
