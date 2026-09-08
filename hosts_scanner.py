import nmap3
import xml.etree.ElementTree as ET

scanner = nmap3.Nmap()

resultat = scanner.scan_command(
    "192.168.1.0/24",
    arg="-sn"
)

print(ET.tostring(resultat, encoding="unicode"))