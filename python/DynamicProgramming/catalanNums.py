'''
Catalan numbers
Catalan numbers are a sequence of natural numbers that occurs in many interesting counting problems like following.

Count the number of expressions containing n pairs of parentheses which are correctly matched. For n = 3, possible expressions are ((())), ()(()), ()()(), (())(), (()()).
Count the number of possible Binary Search Trees with n keys (See this)
Count the number of full binary trees (A rooted binary tree is full if every vertex has either two children or no children) with n+1 leaves.
Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.


Formula
Cn = (1/2n+1)2nCn
'''
from BinomialCoefficient import *;
class CatalinaNum:
    def findCatalinaNum(self, n):
        obj = BinomialCoefficient()
        ncr = obj.binomialCoefficient(2*n, n)
        print(ncr)
        return (1/(n +1))*ncr

if __name__ == '__main__':
    obj = CatalinaNum()
    print(int(obj.findCatalinaNum(6)))
