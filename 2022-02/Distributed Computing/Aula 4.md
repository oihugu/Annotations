# _3. FCI::Distributed Computing

## Quais são os níveis de virtualização?
- Application Level
- Library Level
- OS Level
- Hardware Abstraction Layer
- Instruction Ser Architecture

## Um exemplo de virtualização em Application level
- Citrix
- Windows APP-V 

## Um exemplo de virtualização em OS level
- Docker
- chroot
- Linux-VServer

## Qual a diferença de um Hypervisor do tipo 1(Bare Metal) ou tipo 2(Hosted)?
No hypervisor do tipo 1 todos os sistemas operacionais serão guest no sistema, enquanto os do tipo 2 terão um OS dominante e o restante como guest.

## Qual a diferença de virtualização full para paravirtualização e virtualização em hardware?
- O full todas as chamadas do guest OS serão interpretadas e traduzidas.
- Na paravirtualização o Hypervisor disponibiliza uma API que será chamada pelo guest OS.
- Na virtualização em hardware o hypervisor executa em modo de root as chamadas feitas pelo guest OS.

## Exemplos de hypervisor do tipo 1 e suas aplicações:
O tipo 1 é o tipo mais seguro de hypervisor, tem menor latência e normalmente utilizado por provedores de computação em nuvem por exemplo.
Exemplos:
- Hyper-v
- KVM

## Exemplos de hypervisor do tipo 2 e suas aplicações:
Normalmente são utilizados por usuários finais.
Exemplos:
- VMWare
- Virtual Box
