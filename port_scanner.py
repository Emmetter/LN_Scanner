import nmap3

scanner = nmap3.Nmap()


def scanner_ports(ip, top_ports=100):
    resultat = scanner.scan_command(
        ip,
        arg=f"-sV -O --top-ports {top_ports}"
    )

    hote = resultat.find("host")

    if hote is None:
        return {"ports": [], "os": None}

    ports_info = []

    for port in hote.findall("ports/port"):
        etat = port.find("state")
        service = port.find("service")

        info = {
            "port": port.get("portid"),
            "protocole": port.get("protocol"),
            "etat": etat.get("state") if etat is not None else None,
            "service": service.get("name") if service is not None else None,
            "produit": service.get("product") if service is not None else None,
            "version": service.get("version") if service is not None else None,
        }

        ports_info.append(info)

    os_probable = None
    osmatch = hote.find("os/osmatch")

    if osmatch is not None:
        os_probable = osmatch.get("name")

    return {"ports": ports_info, "os": os_probable}