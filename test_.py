import unittest
from caesar import encrypt_caesar
from caesar import decrypt_caesar
from vigenere import encrypt_vigenere
from vigenere import decrypt_vigenere
from rsa import is_prime
from rsa import gcd
from rsa import multiplicative_inverse

class TestFirstNumber(unittest.TestCase):
    def test_encrypt_caesar_0(self):
        self.assertEqual(encrypt_caesar("APPLE"),"DSSOH")
        self.assertEqual(encrypt_caesar("ApPlE"), "DsSoH")
        self.assertEqual(encrypt_caesar("A!p?P#l$E"), "D!s?S#o$H")
        self.assertEqual(encrypt_caesar("APPLE",10), "KZZVO")
        self.assertEqual(encrypt_caesar("ApPlE",10), "KzZvO")
        self.assertEqual(encrypt_caesar("A!p?P#l$E",10), "K!z?Z#v$O")
    def test_encrypt_caesar_1(self):
        self.assertEqual(encrypt_caesar("HUMANITY"), "KXPDQLWB")
        self.assertEqual(encrypt_caesar("HuMaNiTy"), "KxPdQlWb")
        self.assertEqual(encrypt_caesar("H!u?M#a$N@i%T^y"), "K!x?P#d$Q@l%W^b")
        self.assertEqual(encrypt_caesar("HUMANITY", 10), "REWKXSDI")
        self.assertEqual(encrypt_caesar("HuMaNiTy", 10), "ReWkXsDi")
        self.assertEqual(encrypt_caesar("H!u?M#a$N@i%T^y", 10), "R!e?W#k$X@s%D^i")
    def test_decrypt_caesar_0(self):
        self.assertEqual(decrypt_caesar("DSSOH"), "APPLE")
        self.assertEqual(decrypt_caesar("DsSoH"), "ApPlE")
        self.assertEqual(decrypt_caesar("D!s?S#o$H"), "A!p?P#l$E")
        self.assertEqual(decrypt_caesar("KZZVO",10), "APPLE")
        self.assertEqual(decrypt_caesar("KzZvO",10), "ApPlE")
        self.assertEqual(decrypt_caesar("K!z?Z#v$O",10), "A!p?P#l$E")
    def test_decrypt_caesar_1(self):
        self.assertEqual(decrypt_caesar("KXPDQLWB"), "HUMANITY")
        self.assertEqual(decrypt_caesar("KxPdQlWb"), "HuMaNiTy")
        self.assertEqual(decrypt_caesar("K!x?P#d$Q@l%W^b"), "H!u?M#a$N@i%T^y")
        self.assertEqual(decrypt_caesar("REWKXSDI", 10), "HUMANITY")
        self.assertEqual(decrypt_caesar("ReWkXsDi", 10), "HuMaNiTy")
        self.assertEqual(decrypt_caesar("R!e?W#k$X@s%D^i", 10), "H!u?M#a$N@i%T^y")
    def test_encrypt_vigenere(self):
        self.assertEqual(encrypt_vigenere("APPLE","LEMON"), "LTBZR")
        self.assertEqual(encrypt_vigenere("ApPlE", "LEMON"), "LtBzR")
        self.assertEqual(encrypt_vigenere("APPLE", "LeMoN"), "LTBZR")
        self.assertEqual(encrypt_vigenere("APPLE", "PUT"), "PJIAY")
        self.assertEqual(encrypt_vigenere("ApPlE", "PUT"), "PjIaY")
        self.assertEqual(encrypt_vigenere("APPLE", "PuT"), "PJIAY")
    def test_decrypt_vigenere(self):
        self.assertEqual(decrypt_vigenere("LTBZR","LEMON"), "APPLE")
        self.assertEqual(decrypt_vigenere("LtBzR", "LEMON"), "ApPlE")
        self.assertEqual(decrypt_vigenere("LTBZR", "LeMoN"), "APPLE")
        self.assertEqual(decrypt_vigenere("PJIAY", "PUT"), "APPLE")
        self.assertEqual(decrypt_vigenere("PjIaY", "PUT"), "ApPlE")
        self.assertEqual(decrypt_vigenere("PJIAY", "PuT"), "APPLE")
    def test_rsa_is_prime(self):
        self.assertEqual(is_prime(-1), False)
        self.assertEqual(is_prime(0), False)
        self.assertEqual(is_prime(1), False)
        self.assertEqual(is_prime(2), True)
        self.assertEqual(is_prime(5), True)
        self.assertEqual(is_prime(10), False)
        self.assertEqual(is_prime(1018081), False)
    def test_rsa_gcd(self):
        self.assertEqual(gcd(3, 5), 1)
        self.assertEqual(gcd(15, 5), 5)
        self.assertEqual(gcd(33, 18), 3)
        self.assertEqual(gcd(129, 101), 1)
    def test_rsa_multiplicative_inverse(self):
        self.assertEqual(multiplicative_inverse(3, 16), 11)
        self.assertEqual(multiplicative_inverse(5, 28), 17)
        self.assertEqual(multiplicative_inverse(9, 56), 25)
        self.assertEqual(multiplicative_inverse(11, 74), 27)
        self.assertEqual(multiplicative_inverse(13, 88), 61)
        self.assertEqual(multiplicative_inverse(28, 209), 112)

if __name__ == '__main__':
    unittest.main()