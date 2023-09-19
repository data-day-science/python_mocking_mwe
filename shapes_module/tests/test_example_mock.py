"""
Example tests to demonstrate the features of magic mock.
"""

from unittest.mock import MagicMock, Mock, patch
from ..bag_of_shapes import BagOfShapes
from ..shape import Shape
from ..circle import Circle
from ..rectangle import Rectangle
from unittest import TestCase

class TestMockFeatures(TestCase):
    def test_add_shape(self):
        bag = BagOfShapes()
        shape = Mock(spec=Shape)
        bag.add_shape(shape)
        self.assertEqual(bag.shapes, [shape])

        # Show that the mock is an instance of Shape
        self.assertIsInstance(shape, Shape)

        # Show that the mock has the methods of Shape
        self.assertTrue(hasattr(shape, "area"))
        self.assertTrue(hasattr(shape, "perimeter"))
        self.assertTrue(hasattr(shape, "__str__"))

    def test_total_area(self):
        bag = BagOfShapes()
        shape1 = Mock(spec=Shape)
        shape1.area.return_value = 10
        shape2 = Mock(spec=Shape)
        shape2.area.return_value = 20
        bag.add_shape(shape1)
        bag.add_shape(shape2)
        self.assertEqual(bag.total_area(), 30)

        # Show that when we call the area method on the mock, it returns the value we set
        self.assertEqual(shape1.area(), 10)
        self.assertEqual(shape2.area(), 20)

    def test_total_perimeter(self):
        """
        Using the side effect feature we can make the mock return different values each time the perimeter method is called.
        """
        bag = BagOfShapes()
        shape1 = Mock(spec=Shape)
        shape1.perimeter.side_effect = [10, 20]
        bag.add_shape(shape1)
        self.assertEqual(bag.total_perimeter(), 10)
        self.assertEqual(bag.total_perimeter(), 20)

        # Show that when we call the perimeter method on the mock, it returns the values we set
        shape1 = Mock(spec=Shape)
        shape1.perimeter.side_effect = [10, 20]
        self.assertEqual(shape1.perimeter(), 10)
        self.assertEqual(shape1.perimeter(), 20)

    def test_add_circle(self):
        """
        Demonstrates the wraps feature of mock. We can use this to wrap a mock around a real object.
        """
        bag = BagOfShapes()
        bag.add_circle = Mock(wraps=bag.add_circle)
        bag.add_circle(1, 2, 3)
        self.assertEqual(bag.shapes, [Circle(1, 2, 3)])

        # Show that the mock add_circle method behaves like a normal mock, and has attributes that a mock normally has
        self.assertTrue(hasattr(bag.add_circle, "called"))
        self.assertTrue(hasattr(bag.add_circle, "call_count"))
        self.assertTrue(hasattr(bag.add_circle, "call_args"))
        self.assertTrue(hasattr(bag.add_circle, "call_args_list"))

