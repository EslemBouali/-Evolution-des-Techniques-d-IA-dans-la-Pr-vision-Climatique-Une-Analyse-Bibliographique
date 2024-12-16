# -Evolution-des-Techniques-d-IA-dans-la-Prévision-Climatique:-Une-Analyse-Bibliographique

## Description du Projet
Ce projet explore l'utilisation de diverses techniques d'intelligence artificielle (IA) pour prédire les changements climatiques. Nous avons étudié et implémenté quatre méthodes principales :

1. **Random Forest**
2. **SVM (Support Vector Machine)**
3. **CNN (Convolutional Neural Network)**
4. **LSTM (Long Short-Term Memory)**

Chaque méthode est appliquée à des données climatiques pour évaluer son potentiel prédictif et sa pertinence dans la prévision climatique.

## Structure du Projet

### 1. **Random Forest**
- Implémentation sur Google Earth Engine (GEE).
- Utilisé pour la classification des données satellitaires (par exemple, occupation du sol, évaluation des risques climatiques).
- Environnement : Google Earth Engine (JavaScript ).
- Lien du code : [Script Random Forest](https://github.com/EslemBouali/-volution-des-Techniques-d-IA-dans-la-Pr-vision-Climatique-Une-Analyse-Bibliographique/blob/Master/Random_Forest.js)

### 2. **SVM (Support Vector Machine)**
- Implémentation sur Google Earth Engine (GEE).
- Idéal pour les classifications climatiques binaires ou multiclasses.
- Environnement : Google Earth Engine (JavaScript ).
- Lien du code : [Script SVM](https://github.com/EslemBouali/-volution-des-Techniques-d-IA-dans-la-Pr-vision-Climatique-Une-Analyse-Bibliographique/blob/Master/SVM.js)

### 3. **CNN (Convolutional Neural Network)**
- Conçu pour analyser des images climatiques ou satellitaires afin de prédire des variables comme la température ou les précipitations.
- Environnement : Python avec TensorFlow/Keras.
- Lien du code : [Script CNN](https://github.com/EslemBouali/-volution-des-Techniques-d-IA-dans-la-Pr-vision-Climatique-Une-Analyse-Bibliographique/blob/Master/CNN.py)

### 4. **LSTM (Long Short-Term Memory)**
- Utilisé pour analyser des séries temporelles climatiques (par exemple, températures sur plusieurs décennies).
- Environnement : Python avec TensorFlow/Keras.
- Lien du code : [Script LSTM](https://github.com/EslemBouali/-volution-des-Techniques-d-IA-dans-la-Pr-vision-Climatique-Une-Analyse-Bibliographique/blob/Master/LSTM.py)

## Prérequis

### Outils et Bibliothèques
- **Google Earth Engine** : Pour les méthodes Random Forest et SVM.
- Python: Pour les modèles CNN et LSTM.
- ***Bibliothèques Python***:
  - TensorFlow / Keras
  - NumPy
  - Matplotlib (pour la visualisation des résultats)

### Données
- **Données satellitaires** : Sentinel-2, Landsat (pour Random Forest et SVM).
- **Données climatiques** : Séries temporelles ou images (éventuellement issues de Copernicus ou d'autres bases de données climatiques).

## Installation et Configuration

### Google Earth Engine
1. Créer un compte sur Google Earth Engine.
2. Accéder à l'éditeur de code GEE pour écrire les scripts Random Forest et SVM.

### Environnement Python
1. Installer Python 3.8+.
2. Installer les bibliothèques requises .
3. Configurer Jupyter Notebook ou utiliser Google Colab pour exécuter les scripts CNN et LSTM.

## Scripts Implémentés

### Random Forest
Un modèle de classification supervisé basé sur des données satellitaires (par exemple, Sentinel-2). Implémenté sur Google Earth Engine.

### SVM
Un modèle supervisé adapté à des classifications climatiques binaires ou multiclasses. Implémenté sur Google Earth Engine.

### CNN
Un réseau neuronal convolutif pour analyser des images climatiques. Implémenté en Python.

### LSTM
Un réseau neuronal récurrent pour prédire des séries temporelles climatiques.


## Exécution des Scripts

### 1. Google Earth Engine (Random Forest & SVM)
- Ouvre l'éditeur de code sur Google Earth Engine.
- Copie-colle le script correspondant.
- Exécute le script et visualise les résultats sur la carte.

### 2. Python (CNN & LSTM)
- Exécute les scripts Python sur un environnement configuré (localement ou sur Google Colab).

## Résultats Attendus
- **Random Forest et SVM** : Cartes classifiées (par exemple, régions à risques climatiques).
- **CNN** : Prédictions de variables climatiques basées sur des images.
- **LSTM** : Prédictions de valeurs futures pour des séries temporelles climatiques.

## Conclusion
Ce projet montre comment les techniques d'IA peuvent être appliquées aux problèmes de prévision climatique. Chaque méthode apporte ses avantages, selon la nature des données et les besoins du projet.

## Ressources Bibliographiques
- Breiman, L. (2001). Random Forests. Machine Learning, 45(1), 5-32.
- Vapnik, V. (1995). The Nature of Statistical Learning Theory. Springer.
- LeCun, Y., Bengio, Y., & Hinton, G. (2015). Deep Learning. Nature, 521(7553), 436-444.
- Hochreiter, S., & Schmidhuber, J. (1997). Long Short-Term Memory. Neural Computation, 9(8), 1735-1780.
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). Deep Learning. MIT Press.



