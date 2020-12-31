# Projet_Analyse_Numérique
Visual Studio Code , Python
<img src='Project/entete.png'/>
## Sommaire: 
1. [Introduction](#Introduction)
2. [Méthodes d’intégration numérique](#Méthodes d’intégration numérique)
3. [Interpolation polynomiale:](#Interpolation polynomiale:)
4. [Conclusion](#Conclusion)


## Introduction:
<img src='Project/demo_peek.gif'/>
## Méthodes d’intégration numérique

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
 
 #### Méthode du rectangle
 
 #### Méthode du point milieu
 
 #### Méthode du trapèze
 
 #### Méthode de Simpson
 
## Interpolation polynomiale:

  #### Interpolation de Lagrange
  
  #### Phénomène de Runge
## Conclusion

