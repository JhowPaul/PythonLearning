#Write a Python program to calculate number of days between two dates.
from datetime import date

inicial=date(2077,12,30)
final=date(2077,12,2)
diferenca=inicial-final
print(f"diferença de {diferenca.days}")