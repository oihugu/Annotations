# _3. FCI::Graph Theory

## Quais são os principais métodos de implementar grafos?
- Nós ligados por ponteiros (Lista de Adjacência)
- Matriz de ligações (Matriz de Adjacência)
- Matriz de incidência

## Qual a implementação mais performatica de grafos?
A lista de adjacência.

## Em um grafo |AG| = n qual a quantidade de elementos na lsita de adjacência?
2n

## Como é chamada uma aresta em um grafo orientado?
Ela é chamada de arco

## Quando um grafo H é um subgrafo de outro grafo G?
Quando H ⊆ G (lê-se H é um subconjunto de G), ou seja VH ⊆ VG e AH ⊆ AG

## Quando um grafo H pode ser chamado de subgrafo prórpio de G?
Quando H ⊆ G nas H != G ou seja quando H ⊂ G, assim dizemos que H está contido em G, ou que G contém H

## O que é um subgrafo induzido?
Se G é um grafo e X é não vazio tal que X⊆VG então o subgrafo H de G tal que VH=X e AH é o conjunto das arestas que têm ambos os extremos em X é chamado subgrafo induzido (ou gerado) por X. H é denotado por G[X]

## O que significam as notações G-X, G[VG\X]?
É o subgrafo induzido obtido de G uma vez que tiramos os vértices em X e todas arestas que incidem sobre eles.

## O que é um subgrafo aresta-induzido?
Um subgrafo com todas as arestas e vertices em que as mesmas incidem em um conjunto de arestas E e é denotado por G[E] em um grafo G.

## Como funciona uma lista de adjacência?
Cada vértice vai conter uma lista que guarda quais são as adjacências desse grafo.
https://prnt.sc/nID94F_bXfZU


