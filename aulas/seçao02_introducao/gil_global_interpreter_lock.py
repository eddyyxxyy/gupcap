"""
Global Interpreter Lock- GIL

O GIL é um recurso de bloqueio que previne
que múltiplas threads nativas executem um
código Python ao mesmo tempo.

Isso foi necessário para manter a thread de
execução segura, ou seja, não permitindo que
outras threads fizessem uso do código ainda
em execução, algo que desta forma poderia
causar efeitos indesejados no resultado final.

Ao mesmo tempo que este recurso fez com que a
execução do código Python em uma thread fosse
segura (thread safe), fez com que os programas
Python ficassem “presos” à execução em uma thread
única (simples) e consequentemente à 1 processo.

A razão inicial da criação do GIL em Python é que
o gerenciamento interno de memória do interpretador
Python não é thread-safe.

Thread-safe é um conceito aplicável no contexto de
programas multi-thread. Um código é considerado
thread-safe se ele apenas manipula estruturas de
dados compartilhadas de uma forma que garanta uma
execução segura através de várias threads ao mesmo tempo.


Como escapar do GIL?

A implementação padrão do Python é chamada de Cython mas
existem outras, inclusive algumas que não possuem este
recurso de GIL.

Por exemplo:

- Jython, uma implementação da linguagem Python escrita
em Java;
- IronPython, uma implementação da linguagem Python
escrita em C#;

Podemos também “escapar” do GIL fazendo uso de multiprocessos,
pois cada thread é executada em um processo em separado. Mas
iremos entrar em detalhes sobre isso em uma seção específica
das anotações.
"""
