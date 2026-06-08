# CyberShield IDS — Système de Détection d'Intrusions

Ce dépôt contient le code source complet et l'implémentation de l'interface web pour le projet de fin d'études (Master 2 en Sécurité Informatique) intitulé *CyberShield IDS*.

Le système est basé sur l'apprentissage automatique (Machine Learning) en utilisant l'algorithme *Random Forest* entraîné sur le dataset *NSL-KDD* pour la détection et l'analyse comportementale du trafic réseau.

## 📂 Structure du Projet
- app.py : Le script principal Flask gérant l'application web.
- model/ : Contient le modèle entraîné et sauvegardé pour les prédictions.
- templates/ & static/ : Les interfaces utilisateur (HTML/CSS/JS) du tableau de bord.
- enco.py & pp.py : Scripts de prétraitement des données et d'encodage des flux.

## 📊 Visualisation des Résultats
Les graphiques d'évaluation (Matrice de confusion, comparaison de précision et importance des caractéristiques) sont inclus directement à la racine pour valider les performances du modèle face aux anomalies réseau.

---
Développé par l'étudiant Mahdi — Master 2 Sécurité Informatique.
