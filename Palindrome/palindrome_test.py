from palindrome_list import *

pali = Palindrome()

pali.read_dict('words.txt')
pali.find_palindromes()
pali.to_file('palindrome_en.txt')
