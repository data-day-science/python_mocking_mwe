"""
Test class for demonstrating how to patch python modules
"""

from unittest.mock import patch
from unittest import TestCase
from ..bag_of_shapes import BagOfShapes
from ..shape import Shape
from ..circle import Circle
from ..rectangle import Rectangle
import shapes_module.bag_of_shapes


# Dummy function  to use for patching
def area():
    return 10

class TestExamplePatchingModules(TestCase):
    def test_add_circle(self):
        """
        Demonstrates how to patch a module (Circle). As the BagOfShapes module has already been imported (and it has imported the Circle module), we need to patch the Circle module inside the BagOfShapes module.
        """
        # Patching the circle module that is imported inside bag_of_shapes
        with patch('shapes_module.bag_of_shapes.Circle') as mock_circle:
            bag = BagOfShapes()
            bag.add_circle(1, 2, 3)
            mock_circle.assert_called_once_with(1, 2, 3)
            mock_circle.return_value.area.return_value = 10
            self.assertEqual(bag.total_area(), 10)

    @patch('shapes_module.bag_of_shapes.Circle')
    def test_add_circle_2(self, mock_circle):
        """
        Demonstrates how to patch a module (Circle) using a decorator.
        """
        bag = BagOfShapes()
        bag.add_circle(1, 2, 3)
        mock_circle.assert_called_once_with(1, 2, 3)
        mock_circle.return_value.area.return_value = 10
        self.assertEqual(bag.total_area(), 10)

    @patch('shapes_module.bag_of_shapes.Circle.area')
    def test_add_circle_3(self, mock_area):
        """
        In this example I show that we can patch the function directly rather than the entire class
        """
        bag = BagOfShapes()
        bag.add_circle(1, 2, 3)
        mock_area.return_value = 10
        self.assertEqual(bag.total_area(), 10)
        mock_area.assert_called_once()
        
        # Showing tha the mock is active
        circle = Circle(1, 2, 3)
        self.assertEqual(circle.area(), 10)
        
        
    @patch('shapes_module.bag_of_shapes.Circle', autospec=True)
    def test_add_circle_4(self, mock_circle):
        """
        Demonstrates how to patch a module using the autospec feature. This ensures that the mock has the same attributes as the original object.
        """
        bag = BagOfShapes()
        bag.add_circle(1, 2, 3)
        bag.total_area()
        mock_circle.assert_called_once()
        
        # With autospec, the mock has the same attributes as the original object
        self.assertTrue(hasattr(mock_circle, "perimeter"))
        
        # All the functions of the mock have the same signature as the original object
        self.assertRaises(TypeError, mock_circle.area, 1, 2)



class TestExamplePatchingObjects(TestCase):
    def test_add_circle(self):
        """
        This shows how we can 
        """
        # Patching the circle module that is imported inside bag_of_shapes
        with patch.object(Circle, 'area') as mock_area:
            bag = BagOfShapes()
            circle = Circle(1, 2, 3)
            bag.add_shape(circle)
            mock_area.return_value = 10
            self.assertEqual(bag.total_area(), 10)
            mock_area.assert_called_once()
            
            # Showing tha the mock is active
            self.assertEqual(circle.area(), 10)
        
        # Now that the patching is over, the mock is no longer active
        circle = Circle(1, 2, 3)
        self.assertNotEqual(circle.area(), 10)
            

    @patch.object(Circle, 'area')
    def test_add_circle_2(self, mock_area):
        """
        
        """
        bag = BagOfShapes()
        circle = Circle(1, 2, 3)
        bag.add_shape(circle)
        mock_area.return_value = 10
        self.assertEqual(bag.total_area(), 10)
        mock_area.assert_called_once()
        
        # Showing tha the mock is active
        self.assertEqual(circle.area(), 10)
        
    
        
        
