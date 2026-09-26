# LN Scanner

Scanner réseau minimaliste développé en Python avec Nmap.

## Fonctionnalités

* Découverte des hôtes actifs sur un réseau
* Récupération de l'adresse IP, MAC, du fabricant et du nom d'hôte
* Détection des ports ouverts
* Détection des services et de leurs versions
* Détection du système d'exploitation probable
* Export des résultats en JSON et CSV

## Utilisation

Lancer une analyse avec le réseau souhaité :

```bash
python informant.py 192.168.1.0/24
```

Si aucun réseau n'est fourni, `192.168.1.0/24` est utilisé par défaut.

Les résultats sont affichés dans le terminal et exportés dans :

```text
resultats.json
resultats.csv
```

## Prérequis

* Python 3
* Nmap
* `python3-nmap`

Installation de la dépendance :

```bash
pip install python3-nmap
```

Nmap doit être installé séparément et accessible depuis le terminal.

## Utilisation responsable

Utiliser ce scanner uniquement sur des réseaux pour lesquels vous disposez d'une autorisation d'analyse.
