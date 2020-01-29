import pytest
from arabic_to_roman import int_to_Roman

def test_c():
  val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  syb = ["I", "II", "III", "IV","V", "VI","VII", "VIII","IX","X"]
  
  for i in range(0, 10):
    assert int_to_Roman(val[i]) == syb[i]

def test_c():
  val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
  syb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
  
  for i in range(0, 13):
    assert int_to_Roman(val[i]) == syb[i]
