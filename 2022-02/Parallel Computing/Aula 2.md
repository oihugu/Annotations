# _3. FCI::Parallel Computing

## O que precisamos para executar um programa em paralelo?
- Oportunidade de execução concorrente
- Hardware Paralelo
- Desenvolver o software para ser paralelo

## O que significa respeitar a ordem de execução?
Garantir a corretude lógica (respeitar a ordem lógica das execuções)

## Como é medido o speedup?
Tempo de execução paralela sobre tempo de execução serial

## Quais são as barreiras que o desenvolvimento de novos processadores enfrentam?
- Barreira de energia
- Limite físico dos transistores

## Quais as categorias da taxonomia de Flyn?
- SISD
- SIMD
- MISD
- MIMD

## O que significa SISD na taxonomia de Flyn? E exemplos de onde é utilizada
SISD (Single Instruction Single Data): Fluxo único de instruções sobre um único conjunto de dados.

Exemplo: Máquina de Von Neumann

## O que significa SIMD na taxonomia de Flyn? E exemplos de onde é utilizada
SIMD (Single Instruction Multiple Data): Fluxo único de instruções em múltiplos conjuntos de dados.

Exemplos: 
- Os processadores vetoriais e matriciais.
- Placas de Vídeo (GPU)
- Processadores atuais

## O que significa MISD na taxonomia de Flyn? E exemplos de onde é utilizada
MISD (Multiple Instruction Single Data): Fluxo múltiplo de instruções em um único conjunto de dados.

Nunca foi implementada.

## O que significa MIMD na taxonomia de Flyn? E exemplos de onde é utilizada
MIMD (Multiple Instruction Multiple Data): Fluxo múltiplo de instruções sobre múltiplos conjuntos de dados.

Exemplo: Arquiteturas paralelas atuais