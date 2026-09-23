import sys
import ipaddress
from hosts_scanner import decouvrir_hotes
from port_scanner import scanner_ports
from exporter import exporter_json, exporter_csv

def analyser_reseau(reseau):
    print(f"Reseau analyse : {reseau}")
    print("Recherche des hotes actifs...")

    try:
        hotes = decouvrir_hotes(reseau)
    except Exception as erreur:
        print(f"Erreur lors du scan du reseau : {erreur}")
        return []

    print(f"Nombre d'hotes trouves : {len(hotes)}")

    for hote in hotes:
        print()
        print(f"Analyse de {hote['ip']}...")

        try:
            details = scanner_ports(hote["ip"])
        except Exception as erreur:
            print(f"Erreur lors de l'analyse de {hote['ip']} : {erreur}")
            details = {"ports": [], "os": None}

        hote["os"] = details["os"]
        hote["ports"] = details["ports"]

    return hotes

def afficher_resultats(hotes):
    for hote in hotes:
        print()
        print(f"Hote : {hote['ip']}")
        print(f"Nom d'hote : {hote['hostname']}")
        print(f"Adresse MAC : {hote['mac']}")
        print(f"Fabricant : {hote['fabricant']}")
        print(f"OS probable : {hote['os']}")

        if hote["ports"]:
            print("Ports :")
            for port in hote["ports"]:
                print(f"  {port['port']}/{port['protocole']} "
                      f"{port['etat']} - {port['service']} "
                      f"{port['produit'] or ''} {port['version'] or ''}")
        else:
            print("Aucun port ouvert detecte.")


if __name__ == "__main__":
    try:
        ip_parse = ipaddress.ip_network(sys.argv[1], strict=False)
        reseau = str(ip_parse)
    except IndexError:
        reseau = "192.168.1.0/24"

    resultats = analyser_reseau(reseau)
    afficher_resultats(resultats)

    exporter_json(resultats)
    exporter_csv(resultats)

    print()
    print("Export termine : resultats.json / resultats.csv")