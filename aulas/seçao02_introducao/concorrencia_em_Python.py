"""
Concorrência em Python

Python não nasceu “concorrente”.

A linguagem Python, que já tem cerca de 30 anos,
vem se mordenizando com o passar do tempo e de
acordo com as necessidades.


Então, desde a versão 1.5 foi implementado o
threading:

Com threading permitiu que pudéssemos usar a
linguagem Python para criar threads nativas no
sistema operacional podendo executar código de
forma concorrente.

Um detalhe aqui é que na implementação padrão da
linguagem Python, conhecida como Cpython, as
threads estão limitadas com um dispositivo chamado
GIL - Global Interpreter Lock, fazendo com que o
códigos e ja executado em série e não em paralelo.


Então, desde a versão 2.6 foi implementado o
multiprocessing:

Com multiprocessing permitiu que pudéssemos usar a
linguagem Python para criar subprocessos nativos no
sistema operacional ao invés de threads, podendo
executar código de forma concorrente e paralela
evitando o problema com o GIL.


Então, desde a versão 3.2 foi implementado o
concurrent.futures:

Com concurrent.futures passamos a ter uma
implementação abstrada de concorrência
permitindo de forma fácil fazer uso (ou alternar)
de concorrência usando threads ou multiprocessos.


Então, desde a versão 3.4 foi implementado o
asyncio:

Com asyncio passamos finalmente a ter suporte á
programação assíncrona.
"""
