# test_matn.py
import pytest
from matn import eng_ko_p_qatnashgan_harf

def test_matn():
    assert eng_ko_p_qatnashgan_harf("Hello, World!") == "l"
    assert eng_ko_p_qatnashgan_harf("Python") == "o"
    assert eng_ko_p_qatnashgan_harf("a") == "a"
    assert eng_ko_p_qatnashgan_harf("") == ""

def test_matn_empty():
    assert eng_ko_p_qatnashgan_harf("") == ""

def test_matn_single_harf():
    assert eng_ko_p_qatnashgan_harf("a") == "a"

def test_matn_multiple_harf():
    assert eng_ko_p_qatnashgan_harf("Hello, World!") == "l"
