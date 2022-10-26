"""
Tipos de Concorrência

Podemos dividir a Concorrência em diversos
tipos, dois deles foram abordados na anotação
anterior (conceitos_concorrencia_assincrono.py).

Além da Programação Paralela e Assíncrona, temos
tamém a Programação Distribuída, mas iremos focar
nossos estudos na execução de programas em um
mesmo computador/servidor.


Como funciona a Programação Paralela:

- "Pega" uma tarefa computacional...
- Divide essa tarefa em pequenas sub-tarefas...
- E executa as sub-tarefas simultaneamente em
múltiplos cores.

Sem o uso da Programação Paralela, mesmo que
seu computador tenha múltiplos cores, a tarefa,
por padrão, irá ser executada por inteiro em um
único core, fazendo com que este tenha sua execução
elevada até 100% enquanto outros cores ficam sem uso.

A Programação Paralela tem sua melhor utilização em
tarefas que fazem uso exclusivo da CPU. Que são, por
exemplo:

- Operações com strings;
- Algoritmos de busca;
- Processamento gráfico;
- Algoritmos de processamento numérico;
- Etc...


Como funciona a Programação Assíncrona:

A programação assíncrona é utilizada em operações de
leitura ou escrita em dispositivos IO-Input/Output.

Ou seja, em operações que podem ser lentas e dependem
de um retorno de execução, que pode ser sucesso ou falho.

Em um programa, podemos ter “partes” que precisem ser
executadas de forma assíncrona

Quando a instrução assíncrona é executada, ao invés do
processador ficar esperando sua conclusão ele delega a
execução desta sub-tarefa a alguma outra thread ou
dispositivo e continua fazendo algum outro trabalho ao
invés de esperar a execução destas tarefas.

Quando a sub-tarefa assíncrona finaliza a execução, a
thread principal é notificada e faz uso dos resultados.
Isso é chamado de funções de call-back.

Em algumas linguagens de programação, ao invés de utilizar
funções call-back são utilizados outros objetos com operações
incompletas conhecidos como promisses, futures ou simplesmente
tarefa (task).

A programação assíncrona é melhor utilizada em tarefas que
exigem uso intensivo de IO como:

- Leitura ou escrita em bancos de dados;
- Chamadas à Web Services (APIs);
- Cópia, upload ou download de dados;
- Etc;
"""
