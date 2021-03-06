# Projet_Analyse_Numérique
Visual Studio Code , Python
<img src='Project/entete.png'/>
## Sommaire: 
1. [Introduction](#Introduction)

2. [Méthodes d'intégration numérique](#Méthodes)

      2.1 [But](#but)
      
      2.2 [Motivations](#Motivation)
      
      2.3 [Principe](#principe)
      
      2.4 [Performances](#performances) 
      
      2.5 [Les 4 méthodes](#lesmethodes)
      
3. [Interpolation polynomiale](#interpolation)

     3.1 [Interpolation de Lagrange](#interpolation)
     
      3.1.1 [Phénomène de Runge](#phénomène)
      
      1) [Choix des points](#choix)
           
      2) [Segmentation](#segmentation)
       
4. [Conclusion](#Conclusion)


## Introduction:

Mon projet permet d'étuder une fonction f(x) , la modéliser avec les quatres méthodes d'intégration numériques. Aussi, il consiste à étuder l'interpolation polynomiale(phénomène de Runge). On obtient la représentation graphique de la fonction f(x) avec 3 interfaces graphiques réalisés par « Tkinter ». 

Les méthodes d’intégrations étudiées dans le projet sont:

- Méthode des Rectangles Gauches

- Méthode des Trapèzes

- Méthode des Points Milieux

- Méthode de Simpson

Interpolation polynomiale choisie est le phénomène de Runge.

Comme le montre le demo suivant : 

<img src='Project/demo_peek.gif'/>

## Méthodes d’intégration numérique:

#### But 
 
Le but de ce chapitre est d’aborder le calcul général de l’intégrale d’une fonction f(x) sur un domaine fini délimité par des bornes finies a et b ( les cas des bornes infinies n’est donc pas couvert ).

#### Motivations
 
Dans certains cas très limités, une telle intégrale peut être calculée analytiquement (à la main). Cependant, ce n’est que très rarement possible, et le plus souvent un des cas suivants se présente :

– Le calcul analytique est long, compliqué et rébarbatif

– Le résultat de l’intégrale est une fonction compliquée qui fait appel à d’autres fonctions elles-même longues à évaluer

– Cette intégrale n’a pas d’expression analytique (par exemple la fonction erreur : Er)
Dans tous ces cas, on préfèrera calculer numériquement la valeur de l’intégrale I.
 
 #### Principe
 
 L’idée principale est de trouver des méthodes qui permettent de calculer rapidement une valeur approchée I de l’intégrale à calculer.
 
 #### Performances
 
 La performance d’une méthode se juge en comparant:
 
• la précision du résultat : Celle-ci se caractérise en estimant l’erreur entre l’approximation et la valeur réelle de l’intégrale : E = I-I

La valeur de l’erreur ne peut pas être calculée exactement puisqu’en général, on ne connaît pas l’intégrale I que l’on cherche à calculer. Cependant, une majoration peut souvent être estimée en étudiant le développement en série de Taylor de la fonction f(x).

• La rapidité d’exécution nécessaire pour atteindre ce résultat. De manière générale, toutes les méthodes
peuvent atteindre de très grandes précisions. Cependant, le temps de calcul augmente avec la précision. Ce temps n’augmente pas de la même manière pour toutes les méthodes si bien que certaines s’avèrent plus efficaces que d’autres. En particulier, le temps de calcul des méthodes de quadrature est proportionnel au nombre de points où la fonction f(x) est évaluée.
 
#### Les 4 méthodes
 
##### 1) Méthode du rectangle
La méthode des rectangles est une méthode algorithmique permettant d’encadrer l’aire d’un domaine sous une courbe représentative de fonction et sur un intervalle donné.

<img src='Pictures/rect1.png'/>

<img src='Pictures/rec2.png'/>

Intuitivement, plus le nombre de rectangles grandit, plus les sommes des aires des rectangles vont se rapprocher vers l’intégrale de la fonction sur le même intervalle.

<img src='Pictures/rect6.gif'/>

##### 2) Méthode du point milieu
En analyse numérique, la méthode du point médian est une méthode permettant de réaliser le calcul numérique d'une intégrale.

Le principe est d'approcher l'intégrale de la fonction f par l'aire d'un rectangle de base le segment [a,b] et de hauteur f(a+b/2).

<img src='Pictures/pt_milieu.png'/>
 
##### 3) Méthode du trapèze
La méthode des trapèzes est une méthode pour le calcul numérique d'une intégrale I s'appuyant sur l'interpolation linéaire par intervalles.

Pour obtenir de meilleurs résultats, on découpe l'intervalle [a , b] en n intervalles plus petits et on applique la méthode sur chacun d'entre eux. Bien entendu, il suffit d'une seule évaluation de la fonction à chaque nœud :
<img src='Pictures/trapeze.png'/>
<img src='Pictures/Trapezium2.gif'/>
 
 ##### 4) Méthode de Simpson 
La méthode de Simpson est une technique de calcul numérique d'une intégrale.

Un polynôme étant une fonction très facile à intégrer, on approche l'intégrale de la fonction f sur l'intervalle [a, b], par l'intégrale de P sur ce même intervalle. On a ainsi, la simple formule : 

<img src='Pictures/simpson.png'/>

<img src='Pictures/simpson.gif'/>
 
 
## Interpolation polynomiale:
L'interpolation polynomiale est une technique d'interpolation d'un ensemble de données ou d'une fonction par un polynôme. En d'autres termes, étant donné un ensemble de points (obtenu, par exemple, à la suite d'une expérience), on cherche un polynôme qui passe par tous ces points, et éventuellement vérifie d'autres conditions, de degré si possible le plus bas.

Le résultat n'est toutefois pas toujours à la hauteur des espérances : dans le cas de l'interpolation lagrangienne, par exemple, le choix des points d'interpolation est critique. L'interpolation en des points régulièrement espacés peut fort bien diverger même pour des fonctions très régulières (phénomène de Runge).

<img src='Pictures/interpo.png'/>


#### Interpolation de Lagrange

##### Phénomène de Runge
Le phénomène de Runge met en lumière le fait que l'interpolation polynomiale n'est pas toujours bien adaptée à l'approximation de fonctions.

<img src='Pictures/runge.png'/>

###### i. Choix des points
On peut minimiser l'oscillation des polynômes interpolateurs en utilisant les abscisses de Tchebychev au lieu de points équirépartis pour interpoler. Dans ce cas, on peut montrer que l'erreur d'interpolation décroît lorsque n augmente (on peut le voir en étudiant la constante de Lebesgue des points de Tchebychev, à la croissance logarithmique).

###### ii. Segmentation
Pour approcher une fonction avec des polynômes, on peut préférer utiliser des splines par exemple (ce sont des polynômes par morceaux). Dans ce cas, pour améliorer l'approximation, on augmente le nombre de morceaux et non le degré des polynômes.
  
## Conclusion

On conclut que l'intégration numerique est une méthode pour calculer une valeur approximative d'une fonction qui est compliquée d'une autre coté l'intégration numérique permet d'estimé l'intégrale de cette fonction par la méthode d'interpolation avec certain erreur.
