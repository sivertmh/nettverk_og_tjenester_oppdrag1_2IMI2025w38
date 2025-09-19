import platform
from datetime import datetime

print("="*40, "Systeminformasjon", "="*40)

uname = platform.uname()
print(f"Operativsystem: {uname.system}")
print(f"Navn: {uname.node}")
print(f"Utgave: {uname.release}")
print(f"Versjon: {uname.version}")
print(f"Prosessor: {uname.processor}")
print(f"Arkitektur: {uname.machine}")
