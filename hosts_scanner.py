import nmap3

scanner = nmap3.Nmap()


def decouvrir_hotes(reseau):
    resultat = scanner.scan_command(
        reseau,
        arg="-sn"
    )

    hotes = []

    for host in resultat.findall("host"):
        status = host.find("status")

        if status is None or status.get("state") != "up":
            continue

        adresse_ip = host.find("address[@addrtype='ipv4']")

        if adresse_ip is None:
            continue

        informations = {
            "ip": adresse_ip.get("addr"),
            "mac": None,
            "fabricant": None,
            "hostname": None
        }

        adresse_mac = host.find("address[@addrtype='mac']")

        if adresse_mac is not None:
            informations["mac"] = adresse_mac.get("addr")
            informations["fabricant"] = adresse_mac.get("vendor")

        hostname = host.find("hostnames/hostname")

        if hostname is not None:
            informations["hostname"] = hostname.get("name")

        hotes.append(informations)

    return hotes