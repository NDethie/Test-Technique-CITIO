import intersection   # The code to test
import unittest   # The test framework
from shapely.geometry import LineString


class Test_TestIntersection(unittest.TestCase):

    def test_Stations(self):
        r = intersection.intersectionn(LineString([(3,4), (5,5), (1,2), (8,4), (5,7)]) , LineString( [(2,3), (3,4), (5,8), (5,7), (8,9)]) )
        self.assertEqual(r, True)

    def test_OneStation(self):
        r = intersection.intersectionn(LineString([(3,4), (5,5), (1,2), (8,4), (5,7)]) , LineString([(2,3), (3,5), (5,7), (5,8), (8,9)]) )
        self.assertEqual(r, True)
    
    def test_NoItineraire1(self):
        r = intersection.intersectionn(LineString() , LineString([(2,3), (3,5), (5,7), (5,8), (8,9)]) )
        self.assertEqual(r, True)
    
    def test_NoItineraire2(self):
        r = intersection.intersectionn(LineString([(3,4), (5,5), (1,2), (8,4), (5,7)]) , LineString() )
        self.assertEqual(r, True)
    
    def test_NoItineraire(self):
        r = intersection.intersectionn(LineString() , LineString() )
        self.assertEqual(r, True)
    
    def test_NoStation(self):
        r = intersection.intersectionn(LineString([(3,4), (5,5), (1,2), (8,4), (5,3)]) , LineString([(2,3), (3,5), (5,7), (5,8), (8,9)]) )
        self.assertEqual(r, True)

    

if __name__ == '__main__':
    unittest.main() 