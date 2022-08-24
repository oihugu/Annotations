# _3. FCI::Distributed Computing

## O que é MPI?
MPI (Message Passing Interface for Parallel Programing) é uma biblioteca que pode ser utilizada em linguagens de alto nível como C, C++, Fortran e Python para computação paralela.

## Como é possivel identificar em qual computador um programa está rodando em MPI?
Cada computador possui um identificador único.

## Como fazer uma função do MPI em C?
Passamos um ponteiro que guarda o resultado da função e colocamos MPI_* como nome da função.

## Como pegar o rank intra comunicator no MPI?
MPI_COMM_rank(MPI_COMM_RANK, &my_rank)

## Qual o tipo de comunicação dentro do MPI?
A comunicação é do tipo Send/Recieve

## Como finalizar e por que finalizar um código com o MPI?
- MPI_FInalize()
- Para que não sobre nenhum socket consumindo recursos da máquina.

## QUal o ambiente para se rodar o MPI em C?
- Compilador: mpicc
- Executor: mpiexec -n <num_de_pocessadore> <exec>

## Quais são os componentes do MPI?
- MPI_Innit
- MPI_Finalize
- MPI_COMM_WORLD 