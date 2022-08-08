# _3. FCI::Graph Theory

## Qual a tripla que define um grafo e o que significam seus componentes?
*G* = (V,A,ψ)
*V* é um conjunto de elementos chamado de *Vértices*
*A* é um conjunto de elementos chamado de *Arestas* (seus simbolos)
*ψ* é uma função que *associa cada elemento de A com um par de elementos de V* (ie. {a:[u,v]})

## Quais são as convenções utilizadas para se tratar dos conjuntos de vértices e arestas?
O conjunto de vertices de um grafo G é denotado por VG
O conjunto de arestas de um grafo G é denotado por AG

## Como chamomos uma aresta *a* de um grafo *G* tal que ψ(a) = [u,v]
Dizemos que u e v são extremos de a

## O que é a ordem de um grafo?
A ordem é o número de vertices nesse grafo (ie. A ordem de um grafo G é dada por |VG|)

## O que é o tamanho de um grafo?
O tamanho de um grafo é a soma do número de vértiecs com o número de arestas (ie. O tamanho de um grafo G é dado por $(|VG| + |AG|)$)

## O que é o grau de um vértice v em um grafo G?
O grau de um vértice é o número de arestas que incidem nesse vérice (Laços são contados duas vezes)

## O que é denotado por δ(G)?
δ(G) é o mínimo dos graus dos vértices de G

## O que é denotado por Δ(G)?
Δ(G) é o máximo dos graus dos vértices de G

## O que é uma função bijetora?
Função bijetora é um tipo especifico de função que é tanto injetora como sobrejetora.

## O que é uma função sobrejetora?
Quando sua imagem for igual ao seu contra-domínio
https://prnt.sc/F8ya7yDNyvfS

## O que é uma função injetora?
Uma função é injetora quando cada elemento do conjunto imagem, possue apenas um elemento do conjunto de domínio.
f(a) != f(b) para todo a,b

## O que é um grafo isomórfico?
Sejam G e H dois grafos. Dizemos que G e H são
isomorfos, denotado por G != H, se existem bijeções
 $α : VG -> VH$
 $β : AG -> AH$
tais que:
 $α = (u,v) ∈ AG <-> β(a) = (α(u), α(v)) ∈ AH$
O par $(α,β)$ é chamado de isomorfismo entre G e H.
(Basicamente diz que são semelhantes, se desconsiderarmos os nomes das arestas e dos vértices)

## Quando um grafo G é denominado como vazio?
Um grafo G é vazio se $VG = AG = Ø$

## Como é chamado um grafo com apenas uma vértice?
Um grafo com apenas uma vértice é chamado de *trivial*

## O que é um grafo simples?
Um grafo que não possue laços nem arestas múltiplas.

## O que é um grafo finito?
Um grafo G é *finito* se VG e AG são ambos finitos

## O que é um grafo completo?
Um grafo completo é um simples grafo em que quisquer dos dois vértices distintos são adjacentes. A menos de isomorfismo, existe um único grafo completo com n vértices; Este grafo é denotado por $K_n$

## O que é um grafo bipartido?
Um grafo G é bipartido se VG pode ser particionado em dois conjuntos, X e Y, tais que daca aresta de AG tem um elemento extremo em X e outro em Y. Uma tal partição (X, Y), é chamada de bipartição do grafo.

## O que é um grafo bipartido completo?
Um grafo bipartido completo é um grafo simples com bipartição (X,Y) no qual todo vértive de X é adjacente de todos os vértices de Y. $Se |X| = m$ e $|Y| = n$, então tal grafo é denotado por $K_{nm}$

## O que é o complemento de um grafo G?
O complemento de um grafo G, ou $G^C$ de G é um grafo simples com $VG^C = VG$, sendo que dois vértices são adjacentes em $G^C$ se eles não são adjacentes em G.

## Quando {X, Y} é uma partição de VG?
{X, Y} é uma partição de VG se $X∪Y = VG e X∩Y = Ø$

