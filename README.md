[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Inz35ky5)
# Apache Spark i Dask

Apache Spark to framework do wykonywania obliczeń rozproszonych. Zapoznać z nim można się [tutaj](https://spark.apache.org/docs/latest/quick-start.html).

Inną biblioteką do rozpraszania obliczeń jest [dask](https://dask.org/) z którym można zapoznać się [tutaj](https://docs.dask.org/en/latest/10-minutes-to-dask.html). 

## Zadania
1. Należy napisać z użyciem Apache Spark aplikację służącą do zliczania wystąpień słów w tekście
   * aplikacja ma być być umieszczona w podkatalogu `spark-wordcount`
   * aplikacja ma być napisana w Pythonie
   * aplikacja ma zliczać słowa w pliku do którego ścieżka podana jest jako argument uruchomienia programu
   * wynikiem działania programu ma być lista par `(słowo, liczba wystąpień)`
   * wynik ma być wyświetlony wg malejącej liczby wystąpień słów
   * zliczane powinny być słowa o długości co najmniej 3 znaków
   * zliczane powinny być tylko słowa występujące w [tym słowniku](https://github.com/dwyl/english-words)
   * aplikacja ma być stworzona jako obraz Dockera

2. Należy zaimplementować wcześniejsze zadanie z użyciem daska
   * aplikacja ma być umieszczona w podkatalogu `dask-wordcount`
   * aplikacja ma być stworzona jako osobny obraz Dockera