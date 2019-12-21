import unittest
import numpy as np
from singular import Matrix

class Test_Validator(unittest.TestCase):
	
	def test_matrix(self):
		
		matrix = Matrix()
		a = np.array([(3,8),(9,24)])
		determine = np.linalg.det(a)
		
		result = matrix.determine_singular(determine)
		
		self.assertTrue(result)

if __name__ == "__main__":
	unittest.main()
