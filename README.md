# FizzBuzz em Python

Dada uma entrada numérica **N**, para os números de 1 a N o programa imprime:

- `FizzBuzz` se o número for múltiplo de 3 e de 5;
- `Fizz` se for múltiplo de 3;
- `Buzz` se for múltiplo de 5;
- caso contrário, o próprio número.

## Como executar

```
python fizzbuzz.py        # pergunta o valor de N
python fizzbuzz.py 15     # ou passe N direto como argumento
```

(No Windows, use `py` no lugar de `python` se necessário.)

Exemplo com N = 15:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```

## Testes

```
python -m unittest -v
```
