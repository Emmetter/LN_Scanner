import json
import csv


def exporter_json(donnees, fichier="resultats.json"):
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(donnees, f, ensure_ascii=False, indent=2)


def exporter_csv(donnees, fichier="resultats.csv"):
    lignes = []

    for hote in donnees:
        base = {
            "ip": hote.get("ip"),
            "mac": hote.get("mac"),
            "fabricant": hote.get("fabricant"),
            "hostname": hote.get("hostname"),
            "os": hote.get("os"),
        }

        ports = hote.get("ports") or [{}]

        for port in ports:
            ligne = dict(base)
            ligne["port"] = port.get("port")
            ligne["protocole"] = port.get("protocole")
            ligne["etat"] = port.get("etat")
            ligne["service"] = port.get("service")
            ligne["produit"] = port.get("produit")
            ligne["version"] = port.get("version")
            lignes.append(ligne)

    if not lignes:
        return

    with open(fichier, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=lignes[0].keys())
        writer.writeheader()
        writer.writerows(lignes)