#!/usr/bin/python3
"""Defines unittests for models/amenity.py.
Unittest classes:
    TestAmenity_instantiation
    TestAmenity_save
    TestAmenity_to_dict
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """
    Unittests for testing instantiation of the Amenity class.

    Attributes:
        N/A

    Methods:
        test_no_args_instantiates(self): Test instantiation of Amenity class without arguments.
        test_new_instance_stored_in_objects(self): Test if new instance is stored in __objects.
        test_id_is_public_str(self): Test if id attribute is a public string.
        test_created_at_is_public_datetime(self): Test if created_at attribute is a public datetime object.
        test_updated_at_is_public_datetime(self): Test if updated_at attribute is a public datetime object.
        test_name_is_public_class_attribute(self): Test if name attribute is a public class attribute.
        test_two_amenities_unique_ids(self): Test if two amenities have unique ids.
        test_two_amenities_different_created_at(self): Test if two amenities have different created_at values.
        test_two_amenities_different_updated_at(self): Test if two amenities have different updated_at values.
        test_str_representation(self): Test the string representation of Amenity class.
        test_args_unused(self): Test instantiation of Amenity class with unused arguments.
        test_instantiation_with_kwargs(self): Test instantiation of Amenity class with kwargs.
        test_instantiation_with_None_kwargs(self): Test instantiation of Amenity class with None kwargs.
    """

    def test_no_args_instantiates(self):
        """
        Test instantiation of Amenity class without arguments.
        """
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        """Test if new instance is stored in __objects."""
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_str(self):
        """Test if id attribute is a public string."""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        """Test if created_at attribute is a public datetime object."""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        """Test if updated_at attribute is a public datetime object."""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_name_is_public_class_attribute(self):
        """Test if name attribute is a public class attribute."""
        am = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", am.__dict__)

    def test_two_amenities_unique_ids(self):
        """Test if two amenities have unique ids."""
        am1 = Amenity()
        am2 = Amenity()
        self.assertNotEqual(am1.id, am2.id)

    def test_two_amenities_different_created_at(self):
        """Test if two amenities have different created_at values."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.created_at, am2.created_at)

    def test_two_amenities_different_updated_at(self):
        """Test if two amenities have different updated_at values."""
        am1 = Amenity()
        sleep(0.05)
        am2 = Amenity()
        self.assertLess(am1.updated_at, am2.updated_at)

    def test_str_representation(self):
        """Test str representation of the model."""
        dt = datetime.today()
        dt_repr = repr(dt)
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        amstr = am.__str__()
        self.assertIn("[Amenity] (123456)", amstr)
        self.assertIn("'id': '123456'", amstr)
        self.assertIn("'created_at': " + dt_repr, amstr)
        self.assertIn("'updated_at': " + dt_repr, amstr)

    def test_args_unused(self):
        """Test that __init__ method doesn't use *args or **kwargs."""
        am = Amenity(None)
        self.assertNotIn(None, am.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        dt = datetime.today()
        dt_iso = dt.isoformat()
        am = Amenity(id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(am.id, "345")
        self.assertEqual(am.created_at, dt)
        self.assertEqual(am.updated_at, dt)

    def test_instantiation_with_None_kwargs(self):
        """instantiation with None kwarg value should be handled correctly"""
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


class TestAmenity_save(unittest.TestCase):
    """
    Unittests for testing save method of the Amenity class.

    Attributes:
        N/A

    Methods:
        setUp(self): Set up the test environment.
        tearDown(self): Tear down the test environment.
        test_one_save(self): Test if save method updates the updated_at attribute.
        test_two_saves(self): Test if multiple saves update the updated_at attribute.
        test_save_with_arg(self): Test save method with arguments.
        test_save_updates_file(self): Test if save method updates the file.
    """

    @classmethod
    def setUp(self):
        """
        Sets up a temporary directory and an amenity object to work on.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        """Tears down the test environment by deleting tmp files."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        """Save method should update the updated_at attribute when called once."""
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        self.assertLess(first_updated_at, am.updated_at)

    def test_two_saves(self):
        """
        Test if multiple saves update the updated_at attribute.
        """
        am = Amenity()
        sleep(0.05)
        first_updated_at = am.updated_at
        am.save()
        second_updated_at = am.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        am.save()
        self.assertLess(second_updated_at, am.updated_at)

    def test_save_with_arg(self):
        """Test save method with arguments."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.save(None)

    def test_save_updates_file(self):
        """Test if save method updates the file."""
        am = Amenity()
        am.save()
        amid = "Amenity." + am.id
        with open("file.json", "r") as f:
            self.assertIn(amid, f.read())


class TestAmenity_to_dict(unittest.TestCase):
    """
    Unittests for testing to_dict method of the Amenity class.

    Attributes:
        N/A

    Methods:
        test_to_dict_type(self): Test if to_dict method returns a dictionary.
        test_to_dict_contains_correct_keys(self): Test if the returned dictionary contains correct keys.
        test_to_dict_contains_added_attributes(self): Test if the returned dictionary contains added attributes.
        test_to_dict_datetime_attributes_are_strs(self): Test if datetime attributes in the dictionary are strings.
        test_to_dict_output(self): Test the output of to_dict method.
        test_contrast_to_dict_dunder_dict(self): Test if to_dict method differs from the dunder dict.
        test_to_dict_with_arg(self): Test to_dict method with arguments.
    """

    def test_to_dict_type(self):
        """Test if to_dict method returns a dictionary."""
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the returned dictionary contains correct keys."""
        am = Amenity()
        self.assertIn("id", am.to_dict())
        self.assertIn("created_at", am.to_dict())
        self.assertIn("updated_at", am.to_dict())
        self.assertIn("__class__", am.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the returned dictionary contains added attributes."""
        am = Amenity()
        am.middle_name = "Holberton"
        am.my_number = 98
        self.assertEqual("Holberton", am.middle_name)
        self.assertIn("my_number", am.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if datetime attributes in the dictionary are strings."""
        am = Amenity()
        am_dict = am.to_dict()
        self.assertEqual(str, type(am_dict["id"]))
        self.assertEqual(str, type(am_dict["created_at"]))
        self.assertEqual(str, type(am_dict["updated_at"]))

    def test_to_dict_output(self):
        """Test the output of to_dict method."""
        dt = datetime.today()
        am = Amenity()
        am.id = "123456"
        am.created_at = am.updated_at = dt
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': dt.isoformat(),
            'updated_at': dt.isoformat(),
        }
        self.assertDictEqual(am.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        """Test if to_dict method differs from the dunder dict."""
        am = Amenity()
        self.assertNotEqual(am.to_dict(), am.__dict__)

    def test_to_dict_with_arg(self):
        """Test to_dict method with arguments."""
        am = Amenity()
        with self.assertRaises(TypeError):
            am.to_dict(None)


if __name__ == "__main__":
    unittest.main()
