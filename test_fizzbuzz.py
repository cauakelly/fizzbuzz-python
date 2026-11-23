import unittest

from fizzbuzz import converter_n, fizzbuzz, fizzbuzz_ate


class TestFizzBuzz(unittest.TestCase):
    def test_multiplos_de_3_e_5(self):
        for numero in (15, 30, 45, 90):
            self.assertEqual(fizzbuzz(numero), "FizzBuzz")

    def test_multiplos_de_3(self):
        for numero in (3, 6, 9, 12, 99):
            self.assertEqual(fizzbuzz(numero), "Fizz")

    def test_multiplos_de_5(self):
        for numero in (5, 10, 20, 100):
            self.assertEqual(fizzbuzz(numero), "Buzz")

    def test_demais_numeros(self):
        for numero in (1, 2, 4, 7, 8, 11, 98):
            self.assertEqual(fizzbuzz(numero), str(numero))

    def test_sequencia_ate_15(self):
        esperado = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8",
            "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz",
        ]
        self.assertEqual(fizzbuzz_ate(15), esperado)

    def test_sequencia_ate_1(self):
        self.assertEqual(fizzbuzz_ate(1), ["1"])

    def test_converter_n_valido(self):
        self.assertEqual(converter_n(" 15\n"), 15)
        self.assertEqual(converter_n("﻿7"), 7)

    def test_converter_n_invalido(self):
        for texto in ("abc", "", "3.5", "0", "-4"):
            with self.assertRaises(ValueError):
                converter_n(texto)


if __name__ == "__main__":
    unittest.main()
