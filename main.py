import platform
from datetime import datetime

print("Hello, world! Look at this info!:")

print("="*40, "System Information", "="*40)

uname = platform.uname()
print(f"Operativsystem: {uname.system}")
print(f"Node Navn: {uname.node}")
print(f"Utgave: {uname.release}")
print(f"Versjon: {uname.version}")
print(f"Arkitektur: {uname.machine}")
print(f"Prosessor: {uname.processor}")
