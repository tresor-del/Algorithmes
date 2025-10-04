# Algorithmes

Un **algorithme** est une procédure permettant de résoudre un problème à l’aide d’une suite d’étapes logiques et finies.

Ce dépôt regroupe plusieurs exemples d’algorithmes fondamentaux, implémentés dans différents langages.

---

## Langages utilisés

[![Python](https://img.shields.io/badge/Python-3.11%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![C](https://img.shields.io/badge/Language-C-lightgrey?logo=c&logoColor=white)](https://en.wikipedia.org/wiki/C_(programming_language))
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow?logo=javascript&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

## Contenu du dépôt

- [Exemples de récursion](rec)
- [Algorithmes de recherche](search)
- [Algorithmes de tri](sort)

---

## Algorithmes de recherche

### Sur les graphes

Un **graphe** est une structure composée de **nœuds** (ou **sommets**) reliés entre eux par des **arêtes** (ou **vecteurs**).  
Les algorithmes de recherche sur les graphes permettent d’explorer ces connexions pour résoudre différents problèmes, notamment la recherche du **plus court chemin**.

Avant de commencer, consultez [creation_graphe](search/graphes/creation_graphe/) pour comprendre comment créer un graphe.

---

### 🔹 Recherche en profondeur (DFS)

- Utilise une structure de données de type **pile** ([pile (LIFO)](search/graphes/dfs/pile(LIFO).py)) pour parcourir le graphe.
- Explore le graphe **le plus profondément possible** avant de revenir en arrière.
- Voir l’implémentation : [recherche en profondeur](search/graphes/dfs/)

---

### 🔹 Recherche en largeur (BFS)

- Utilise une structure de données de type **file** ([file (FIFO)](search/graphes/bfs/file(FIFO).py)) pour parcourir le graphe.
- Explore d’abord les **voisins les plus proches** avant de passer aux niveaux suivants.
- Voir l’implémentation : [recherche en largeur](search/graphes/bfs/)

---

### 🔹 Algorithme de Dijkstra

- Algorithme plus **intelligent** que DFS et BFS car il prend en compte le **coût du chemin déjà parcouru** (fonction `g`).
- Il permet de trouver le **plus court chemin** entre un nœud de départ et les autres nœuds.
- Voir l’implémentation : [Dijkstra](search/graphes/djikstra/)

---

### 🔹 Algorithme A* (A star)

- C’est une amélioration de Dijkstra : il avance en choisissant le **plus petit coût total** défini par  
  \[
  f(n) = g(n) + h(n)
  \]
  où :
  - `g(n)` est le coût du chemin déjà parcouru ;
  - `h(n)` est une **fonction heuristique** estimant le coût restant jusqu’à la solution.
- Voir l’implémentation : [A*](search/graphes/A*/)

---

## Sur les tableaux


Les **algorithmes de recherche sur les tableaux** permettent de retrouver la position d’un élément dans une liste ou un tableau.  
Ce dossier contient deux méthodes fondamentales : **la recherche linéaire** et **la recherche binaire**.  
Chaque algorithme est implémenté en **Python**, **C** et **JavaScript**.

---

### 🔹 Recherche linéaire (Linear Search)

- Parcourt le tableau **élément par élément** jusqu’à trouver la valeur recherchée.  
- Fonctionne sur **tout type de tableau**, trié ou non.  

- Voir les fichiers : 
- [linear.py](search/tableau/linéaire/linear.py)  
- [linear.c](search/tableau/linéaire/linear.c)  
- [linear.js](search/tableau/linéaire/linear.js)

---

### 🔹 Recherche binaire (Binary Search)

- Fonctionne **uniquement sur un tableau trié**.  
- Divise le tableau en deux parties à chaque étape pour rechercher plus efficacement.  

- Voir les fichiers : 
- [binary.py](search/tableau/binaire/binary.py)  
- [binary.c](search/tableau/binaire/binary.c)  
- [binary.js](search/tableau/binaire/binary.js)


---

**Remarque :**  
Les deux recherches produisent le même résultat final (l’indice de l’élément recherché), mais diffèrent par leur vitesse selon le type de données et leur taille.



## Algorithmes de tri

Les **algorithmes de tri** permettent d’ordonner une liste ou un tableau de valeurs selon un critère (croissant ou décroissant).  
Chaque dossier contient une implémentation en **Python**, **C** et **JavaScript**.

---

### 🔹 Tri à bulles (Bubble Sort)

- Compare les éléments deux à deux et les échange s’ils sont dans le mauvais ordre.  
- Répète ce processus jusqu’à ce que la liste soit triée.  
- Voir les fichiers :
  - [bubble_or_recursion.py](sort/bulle/bubble_or_recursion.py)
  - [bulle.c](sort/bulle/bulle.c)
  - [bulle.js](sort/bulle/bulle.js)

---

### 🔹 Tri par insertion (Insertion Sort)

- Construit le tableau trié **élément par élément**,  
  en insérant chaque nouvel élément à sa position correcte dans la partie déjà triée.  
- Voir les fichiers :
  - [insertion.py](sort/insertion/insertion.py)
  - [insertion.c](sort/insertion/insertion.c)
  - [insertion.js](sort/insertion/insertion.js)

---

### 🔹 Tri par sélection (Selection Sort)

- Recherche le plus petit élément du tableau et le place à la première position.  
- Répète ensuite l’opération pour le reste du tableau jusqu’à ce qu’il soit entièrement trié.  
- Voir les fichiers :
  - [selection.py](sort/selection/selection.py)
  - [selection.c](sort/selection/selection.c)
  - [selection.js](sort/selection/selection.js)

---


 **Auteur :** [tresor-del](https://github.com/tresor-del) 
