"""
Test class for demonstrating how to patch python modules
"""

from unittest.mock import patch
from unittest import TestCase
from ..bag_of_shapes import BagOfShapes
from ..shape import Shape
from ..circle import Circle
from ..rectangle import Rectangle

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