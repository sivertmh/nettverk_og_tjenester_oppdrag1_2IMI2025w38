# Nettverk og Tjenester - Oppdrag 1, 2IMI uke 38 2025

I dette oppdraget skal jeg koble en Raspberry Pi, som skal tilby ulike tjenester, med min skole-PC via klassens nettverk. Serveren skal ha statisk IP-adresse, mens skole-pc-ens skal være dynamisk. Dokumentasjon skal legges ut på Github på [https://github.com/sivertmh/nettverk_og_tjenester_oppdrag1_2IMI2025w38](https://github.com/sivertmh/nettverk_og_tjenester_oppdrag1_2IMI2025w38).

## IP-adresser og Annen Nettverksinfo

**SMHIMI2-15 (skole-laptop):**

* dynamisk IP-addresse: 10.2.1.253

**sivertskolepi (Raspberry Pi):**

* statisk IP-addresse: 10.200.14.19
* nettmaske (subnet mask): 255.0.0.0
* default gateway: 10.0.0.1 
* DNS: 10.0.0.10 eller 8.8.8.8

**Slik ser min .yaml-configfil ut i /etc/netplan for sivertskolepi:**

```
network:
  version: 2
  renderer: networkd
  wifis:
    wlan0:
      dhcp4: no
      addresses:
        - 10.200.14.19/8
      gateway4: 10.0.0.1
      nameservers:
        addresses:
          - 10.0.0.10
          - 8.8.8.8
          - 1.1.1.1
      access-points:
        "Kuben.it":
          password: "IMKuben1337!"
```



