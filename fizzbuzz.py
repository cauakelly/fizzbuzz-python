"""FizzBuzz: para os números de 1 a N, imprime Fizz, Buzz, FizzBuzz ou o próprio número."""

import sys


def fizzbuzz(numero: int) -> str:
    """Retorna o texto correspondente a um único número."""
    if numero % 15 == 0:  # múltiplo de 3 e de 5
        return "FizzBuzz"
    if numero % 3 == 0:
        return "Fizz"
    if numero % 5 == 0:
        return "Buzz"
    return str(numero)


def fizzbuzz_ate(n: int) -> list[str]:
    """Retorna a sequência FizzBuzz de 1 até n (inclusive)."""
    return [fizzbuzz(i) for i in range(1, n + 1)]


def converter_n(texto: str) -> int:
    """Converte o texto em N; lança ValueError se não for um inteiro >= 1."""
    texto = texto.strip().lstrip("﻿")  # remove BOM que alguns terminais inserem
    try:
        n = int(texto)
    except ValueError:
        raise ValueError(f"'{texto}' não é um número inteiro.") from None
    if n < 1:
        raise ValueError("N precisa ser maior ou igual a 1.")
    return n


def ler_n() -> int:
    """Lê N da entrada, repetindo até receber um inteiro positivo."""
    while True:
        try:
            entrada = input("Digite um número inteiro positivo N: ")
        except EOFError:
            sys.exit("\nEntrada encerrada sem um valor para N.")
        try:
            return converter_n(entrada)
        except ValueError as erro:
            print(f"{erro} Tente novamente.")


def main() -> None:
    if len(sys.argv) > 1:  # permite: python fizzbuzz.py 15
        try:
            n = converter_n(sys.argv[1])
        except ValueError as erro:
            sys.exit(str(erro))
    else:
        n = ler_n()
    for linha in fizzbuzz_ate(n):
        print(linha)


if __name__ == "__main__":
    main()
