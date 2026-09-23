# LN Scanner

## Description

LN Scanner est un outil de découverte réseau développé en Python. Il utilise Nmap afin d'identifier les hôtes actifs sur un réseau donné.

Le script effectue une analyse de découverte sans analyser les ports. Il envoie les sondes nécessaires à Nmap et récupère les résultats afin de déterminer quelles adresses IP sont actuellement accessibles.

## Fonctionnement

Le script utilise la bibliothèque `python3-nmap` pour communiquer avec Nmap et effectuer une analyse avec l'option `-sn`.

Cette option permet de réaliser une découverte d'hôtes sans effectuer de scan des ports.

Les résultats sont retournés sous forme de XML par Nmap. Le script peut ensuite analyser ces données afin d'identifier les hôtes dont l'état est `up`.

## Utilisation

Après avoir activé l'environnement virtuel :

```bash
python hosts_scanner.py
```

Le réseau analysé est défini dans le script. Il doit correspondre au réseau auquel la machine est connectée.

Par exemple :

```text
192.168.1.0/24
```

Un réseau en `/24` contient 256 adresses IP, allant généralement de `192.168.1.0` à `192.168.1.255`.

## Prérequis

* Python 3
* Nmap
* `python3-nmap`

Installation de la dépendance Python :

```bash
pip install python3-nmap
```

Nmap doit également être installé et accessible depuis le terminal.

## Environnement virtuel

Le projet utilise un environnement virtuel Python afin d'isoler ses dépendances.

Création :

```bash
py -m venv .venv
```

Activation avec Git Bash :

```bash
source .venv/Scripts/activate
```

Installation des dépendances :

```bash
pip install -r requirements.txt
```

## Objectif du projet

Ce projet a pour objectif de comprendre le fonctionnement d'un outil de découverte réseau et les principes utilisés par des scanners comme Nmap.

Il constitue la première étape du développement d'un scanner réseau minimaliste pouvant éventuellement être étendu avec d'autres fonctionnalités, comme la détection des adresses MAC ou l'analyse des ports.

## Utilisation responsable

Le scanner doit être utilisé uniquement sur des réseaux et des appareils pour lesquels vous avez l'autorisation d'effectuer des analyses.
