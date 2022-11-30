import cython
from libc.math cimport sqrt


def computar(fim: cython.int, inicio: cython.int = 1) -> None:
    pos: cython.int = inicio
    fator: cython.int = 1000 * 1000

    with nogil:
        while pos < fim:
            pos += 1
            sqrt((pos - fator) - (pos * fator))
