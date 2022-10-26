"""
Conceitos sobre Concorrência e Programação Assíncrona

Ao executar um programa Python, o que ocorre?

a) O interpretador Python cria um processo no OS;
b) O processo Python cria uma thread (linha de
execução) para executar o código.

Seria algo como:

- Código fonte escrito por você que...
- Entra no interpretador do Python que...
- Compila esse código...
- O transforma em bytecode...
- E a máquina virtual Python irá executar o código...
- Na máquina virtual temos: inputs e library modules...
- Agora com o código sendo executado na thread pelo processo
Python.

Segundo a Lei de Moore, o número de transistores
em um microprocessador iria dobrar a cada 18 meses,
e isso se mostrou verdade até 2015.

A Lei de Moore trouxe percepções sobre o futuro
da computação que realmente se concretizaram. Os
processadores ficaram:

- Menores;
- Mais baratos;
- Mais poderosos;
- Energicamente mais eficientes;
- E muito mais...

Desta forma, por exemplo, para uma aplicação que você
desenvolveu hoje ser executada mais rapidamente daqui
1 ano, bastaria trocar o hardware.

Com o "fim" da Lei de Moore em 2015, os circuitos
integrados (processadores) que formavam um único
"core" passaram a ter mais processadores, se tornando
"multi-cores".

É como se tivessemos multiprocessadores em um único
processador.

Desta forma, para que sua aplicação seja performática
hoje, amanhã e sempre, devemos tentar fazer uso de todos
os "cores" do computador/servidor no qual a aplicação
estiver sendo executada de forma concorrente.


MAS, o que é a concorrência?

Em Ciência da Computação, concorrência é a execução
de múltiplas instruções sequenciais ao mesmo tempo.

Existem dois tipos principais de concorrência:

- Programação Paralela;
- Programação Assíncrona.

Esta execução deve se atentar para alguns pontos
fundamentais:

- Ordem de execução;
- Recursos compartilhados.

A Ordem de execução seria a concorrência quebrando
instruções sequenciais em diversas partes, onde sua
ordem de execução não gere efeitos indesejados no
resultado final, mesmo que a "ultima" instrução
seja finalizada antes da primeira.

Os Recursos Compartilhados implicam que a execução
deve compartilhar o mínimo de recursos possível entre
as instruções. Quanto mais recursos forem compartilhados
entre as execuções concorrentes, mais coordenação entre
as execuções será necessária para garantir o resultado
final correto, dificultando o processo.

Nós podemos evitar muita complicação para realizar
concorrência escolhendo corretamente os padrões e
mecanismos concorrentes dependendo do que queremos
atingir.

Iremos ainda aprender os diversos padrões e mecanismos
da linguagem Python específicos para realizar a programação
concorrênte e assíncrona para que você saiba utilizar seus
programas fazendo sempre a melhor escolha.
"""
