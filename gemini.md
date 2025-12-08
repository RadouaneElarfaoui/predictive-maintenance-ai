# Projet de Maintenance Prédictive

Ce projet a pour objectif de développer un système de maintenance prédictive pour anticiper les pannes de machines industrielles en utilisant l'intelligence artificielle.

## Technologies

*   **Modélisation IA :** MATLAB avec la Neural Network Toolbox a été utilisé pour créer et entraîner un réseau de neurones de classification.
*   **Rapport :** Le rapport de projet est rédigé en LaTeX et se trouve dans le répertoire `rapport/`. Le document final est `rapport/main.pdf`.

## Données

Le modèle est entraîné sur un jeu de données (`machine failure.csv`) qui contient des informations de capteurs d'une machine-outil, telles que :
*   Température de l'air et du processus
*   Vitesse de rotation
*   Couple
*   Usure de l'outil

## Objectif du Modèle

Le réseau de neurones est un classifieur binaire qui prédit si une machine va tomber en panne (`Machine Failure` = 1) ou continuer de fonctionner normalement (`Machine Failure` = 0) en se basant sur les données des capteurs.
