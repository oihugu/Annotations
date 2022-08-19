# _3. FCI::Distributed Computing

## O que é concorrência?
Concorrência são dois processos competindo pelo mesmo recurso.

## O que é paralelismo? (Prova)
Paralelismo é sobre a execução de tarefas em mais de um core ao mesmo tempo, não necessitando de pausar uma tarefa ou desalocar algum recurso para que possa ser alocado em outro processo.

## O que é um processo?
Um processo pode ser visto como um container de recursos utilizados por uma ou mais tarefas. Processos são isolados entre si (inclusive, através de mecanismos de proteção a nível de hardware), não compartilham memória,

## O que é uma thread?
Uma thread é uma “linha” de execução dentro de um processo. Cada thread tem o seu próprio estado de processador e a sua própria pilha, mas compartilha a memória atribuída ao processo com as outras threads “irmãs” (filhas do mesmo processo).

## Uma aplicação paralalela é uma aplicação concorrente?
Uma vez que está rodando em apenas um computador multicore, sim uma aplicação paralela também é concorrente.

## A frase que descreve a diferença entre concorrência e paralelismo
Concurrency is about dealing with lots of things at once. Parallelism is about doing lots of things at once.

## Quais as vantagens do processamento paralelo?
- Tempo mais rápido para resolver um problema
- Resolver problemas mais complexos
- Superar restrições de memória
