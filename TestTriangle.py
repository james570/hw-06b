# -*- coding: utf-8 -*-
"""
Updated Mar 14, 2025
Enhanced unit tests for triangle classification program

@author: James
"""

import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):

    # Right triangle
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,12,13),'Right','5,12,13 is a Right triangle')

    # Equilateral triangle
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral','10,10,10 should be equilateral')

    # Isosceles triangle
    def testIsoscelesTriangleA(self):
        self.assertEqual(classifyTriangle(5,5,8),'Isoceles','5,5,8 should be isosceles')

    def testIsoscelesTriangleB(self):
        self.assertEqual(classifyTriangle(8,5,5),'Isoceles','8,5,5 should be isosceles')

    # Illegal triangle
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,2,3),'NotATriangle','1,2,3 should be NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(10,1,1),'NotATriangle','10,1,1 should be NotATriangle')

    # Invalid input
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1,2,3),'InvalidInput','-1,2,3 should be InvalidInput')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201,100,100),'InvalidInput','201,100,100 should be InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(3.5,4,5),'InvalidInput','3.5,4,5 should be InvalidInput')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
