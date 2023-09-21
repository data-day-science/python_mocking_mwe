# Python Mocking and Patching Examples

Ive made this repo so that I stop making the same mistakes when writing unit tests using Mocks and Patching.

It uses a class called BagOfShapes stored in bag_of_shapes.py to demonstrate the following mocking techniques within unit tests:

* Using the Mock class wrap argument to turn an existing class/method into to a mock object (so that you can test for call count, call arguments etc) - test_example_mock.py::TestMockFeatures::test_add_circle
* Using the Mock class side_effect argument to return different values from a mock object function - test_example_mock.py::TestMockFeatures::test_total_perimiter
* Using the Mock class spec argument to create a mock object with the same attributes as a class - test_example_mock.py::TestMockFeatures::test_add_shape


And the following patching techniques:

* Patching a class within a with statement and then replacing a function return value (@patch) - test_example_patching.py::TestExamplePatching::test_add_circle
* Patching a class with a decorator and then replacing a function return value (@patch) - test_example_patching.py::TestExamplePatching::test_add_circle_2
* Patching a single function within a class with a decorator to return a different value (@patch) - test_example_patching.py::TestExamplePatching::test_add_circle_3
* Patching a class with a decorator and using the spec argument to create a mock object with the same attributes as the patched class(@patch) - test_example_patching.py::TestExamplePatching::test_add_circle_4
* Using the patch.object function to patch a class within a with statement and then replacing a function return value (@patch.object) - test_example_patching.py::TestExamplePatchingObject::test_add_circle
* Using the patch.object function to patch a class with a decorator and then replacing a function return value (@patch.object) - test_example_patching.py::TestExamplePatchingObject::test_add_circle_2



