#!/usr/bin/python3
"""
A unittest for the Base class

Unittest Classes:

"""

import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase_init_method(unittest.TestCase):
    """
    Tests the instantiation of the Base class
    """
    def test_no_arg(self):
        id1 = Base()
        id2 = Base()
        self.assertEqual(id1.id, id2.id - 1)

    def test_three_init(self):
        id1 = Base()
        id2 = Base()
        id3 = Base()
        self.assertEqual(id1.id, id3.id - 2)

    def test_None(self):
        id1 = Base(None)
        id2 = Base(None)
        self.assertEqual(id1.id, id2.id - 1)

    def test_id_parameter(self):
        self.assertEqual(45, Base(45).id)

    def test_auto_id_after_unique(self):
        id1 = Base()
        id2 = Base(45)
        id3 = Base()
        self.assertEqual(id1.id, id3.id - 1)

    def test_change_id(self):
        id1 = Base(45)
        id1.id = 69
        self.assertEqual(id1.id, 69)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(69).__nb_instances)

    def test_id_str(self):
        self.assertEqual("Lennox", Base("Lennox").id)

    def test_id_float(self):
        self.assertEqual(Base(69.69).id, 69.69)

    def test_complex_id(self):
        self.assertEqual(Base(complex(2)).id, complex(2))

    def test_dict_id(self):
        self.assertEqual(Base({"name": "Lennox"}).id, {"name": "Lennox"})

    def test_id_bool(self):
        self.assertEqual(Base(False).id, False)

    def test_id_list(self):
        self.assertEqual(Base([1, 2]).id, [1, 2])

    def test_id_tuple(self):
        self.assertEqual(Base((1, 2)).id, (1, 2))

    def test_id_sets(self):
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_id_NaN(self):
        self.assertNotEqual(Base(float('nan')).id, float('nan'))

    def test_id_infinite(self):
        self.assertEqual(Base(float('inf')).id, float('inf'))

    def test_id_bytes(self):
        self.assertEqual(Base(b'abc').id, b'abc')

    def test_id_memoryview(self):
        self.assertEqual(Base(memoryview(b'abc')).id, memoryview(b'abc'))

    def test_id_bytearray(self):
        self.assertEqual(Base(bytearray(b'abc')).id, bytearray(b'abc'))

    def test_id_range(self):
        self.assertEqual(Base(range(10)).id, range(10))

    def test_id_frozenset(self):
        self.assertEqual(Base(frozenset({1, 2})).id, frozenset({1, 2}))


class TestBase_to_json_string_method(unittest.TestCase):
    """
    Unittest for testing the method to_json_string
    """
    def test_convert_rectangle(self):
        r1 = Rectangle(8, 6, 8, 4, 2)
        self.assertEqual(str, type(Base.to_json_string([r1.to_dictionary()])))

    def test_convert_square(self):
        s1 = Square(8, 6, 4, 2)
        self.assertEqual(str, type(Base.to_json_string([s1.to_dictionary()])))

    def test_length_one_dict_rectangle(self):
        r1 = Rectangle(10, 7, 2, 8, 6)
        self.assertTrue(len(Base.to_json_string([r1.to_dictionary()])) == 53)

    def test_length_two_dicts_rectangle(self):
        r1 = Rectangle(2, 3, 5, 19, 2)
        r2 = Rectangle(4, 2, 4, 1, 12)
        dictionary = [r1.to_dictionary(), r2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(dictionary)) == 106)

    def test_length_one_dict_square(self):
        s1 = Square(10, 2, 3, 4)
        self.assertTrue(len(Base.to_json_string([s1.to_dictionary()])) == 39)

    def test_length_two_dicts_square(self):
        s1 = Square(10, 2, 3, 4)
        s2 = Square(4, 5, 21, 2)
        list_dicts = [s1.to_dictionary(), s2.to_dictionary()]
        self.assertTrue(len(Base.to_json_string(list_dicts)) == 78)

    def test_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_None(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([1, 2], 3)


class TestBase_save_to_file_method(unittest.TestCase):
    """
    Unittest to test the method save_to_file method
    """
    @classmethod
    def tearDown(self):
        """
        Deletes all created files
        """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_file_rectangle(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r", encoding="utf-8") as file_open:
            self.assertTrue(len(file_open.read()) == 53)

    def test_save_file_square(self):
        s1 = Square(10, 8, 5, 9)
        Square.save_to_file([s1])
        with open("Square.json", "r", encoding="utf-8") as file_open:
            self.assertTrue(len(file_open.read()) == 39)

    def test_save_file_two_rectangles(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r", encoding="utf-8") as file_open:
            self.assertTrue(len(file_open.read()) == 105)

    def test_save_file_two_squares(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file([s1, s2])
        with open("Square.json", "r", encoding="utf-8") as file_open:
            self.assertTrue(len(file_open.read()) == 77)

    def test_with_class_name(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        Base.save_to_file([r1])
        with open("Base.json", "r", encoding="utf-8") as file_open:
            self.assertTrue(len(file_open.read()) == 53)

    def test_overwrite(self):
        r1 = Rectangle(2, 28, 8, 8, 3)
        Rectangle.save_to_file([r1])
        r1 = Rectangle(10, 2, 8, 5, 9)
        Rectangle.save_to_file([r1])
        with open("Rectangle.json", "r", encoding="utf-8") as file_open:
            self.assertTrue(len(file_open.read()) == 53)

    def test_save_None(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r", encoding="utf-8") as file_open:
            self.assertEqual(file_open.read(), "[]")

    def test_save_empty(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r", encoding="utf-8") as file_open:
            self.assertEqual(file_open.read(), "[]")

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])


class TestBase_from_json_string_method(unittest.TestCase):
    """
    Unittest to test the from_json_string method
    """
    def test_type_is_list(self):
        list_1 = [{"id": 20}]
        json_string = Rectangle.to_json_string(list_1)
        output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_1, output)

    def test_type_rectangle(self):
        list_1 = [{"id": 20, "width": 17, "height": 13, "x": 7, "y": 3}]
        json_string = Rectangle.to_json_string(list_1)
        output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_1, output)

    def test_type_square(self):
        list_1 = [{"id": 20, "size": 17, "x": 7, "y": 3}]
        json_string = Square.to_json_string(list_1)
        output = Square.from_json_string(json_string)
        self.assertEqual(list_1, output)

    def test_case_two_rectangle(self):
        list_1 = [
            {"id": 20, "width": 17, "height": 13, "x": 7, "y": 3},
            {"id": 2, "width": 7, "height": 3, "x": 8, "y": 13}
        ]
        json_string = Rectangle.to_json_string(list_1)
        output = Rectangle.from_json_string(json_string)
        self.assertEqual(list_1, output)

    def test_type_multiple_squares(self):
        list_1 = [
            {"id": 20, "size": 17, "x": 7, "y": 3},
            {"id": 9, "size": 85, "x": 8, "y": 5}
        ]
        json_string = Square.to_json_string(list_1)
        output = Square.from_json_string(json_string)
        self.assertEqual(list_1, output)

    def test_type_None(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_empty_list(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], [])


class TestBase_create_method(unittest.TestCase):
    """
    Unittest for testing the create method
    """

    # tests for Rectangle
    def test_original_rect(self):
        r1 = Rectangle(9, 2, 7, 3, 5)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual("[Rectangle] (5) 7/3 - 9/2", str(r1))

    def test_created_new(self):
        r1 = Rectangle(9, 2, 7, 3, 5)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertEqual("[Rectangle] (5) 7/3 - 9/2", str(r2))

    def test_different_objects(self):
        r1 = Rectangle(9, 2, 7, 3, 5)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertIsNot(r1, r2)

    def test_equality_rect(self):
        r1 = Rectangle(9, 2, 7, 3, 5)
        dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**dictionary)
        self.assertNotEqual(r1, r2)

    # tests for Square
    def test_original_sq(self):
        s1 = Square(9, 7, 3, 5)
        dictionary = s1.to_dictionary()
        s2 = Square.create(**dictionary)
        self.assertEqual("[Square] (5) 7/3 - 9", str(s1))

    def test_new_square(self):
        s1 = Square(9, 7, 3, 5)
        dictionary = s1.to_dictionary()
        s2 = Square.create(**dictionary)
        self.assertEqual("[Square] (5) 7/3 - 9", str(s2))

    def test_same_object(self):
        s1 = Square(9, 7, 3, 5)
        dictionary = s1.to_dictionary()
        s2 = Square.create(**dictionary)
        self.assertIsNot(s1, s2)

    def test_equality_sq(self):
        s1 = Square(9, 7, 3, 5)
        dictionary = s1.to_dictionary()
        s2 = Square.create(**dictionary)
        self.assertNotEqual(s1, s2)


class TestBase_load_from_file_method(unittest.TestCase):
    """
    Unittest to test the method load_from_file
    """

    @classmethod
    def tearDown(self):
        """
        Deletes any created files after module executes
        """
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass

        try:
            os.remove("Square.json")
        except IOError:
            pass

    # tests for Rectangle
    def test_read_first_rect(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r1), str(output[0]))

    def test_read_other_items(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertEqual(str(r2), str(output[1]))

    def test_type_rectangle(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file([r1, r2])
        output = Rectangle.load_from_file()
        self.assertTrue(all(type(item) == Rectangle for item in output))

    # tests for square object
    def test_first_square(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(str(s1), str(output[0]))

    def test_rest_squares(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertEqual(str(s2), str(output[1]))

    def test_type_squares(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file([s1, s2])
        output = Square.load_from_file()
        self.assertTrue(all(type(item) == Square for item in output))

    def test_no_file(self):
        output = Square.load_from_file()
        self.assertEqual([], output)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file([], [])


class TestBase_save_to_file_csv_method(unittest.TestCase):
    """
    Tests the save_to_file_csv method
    """

    @classmethod
    def tearDown(self):
        """
        Deletes any files created when done
        """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass

        try:
            os.remove("Square.csv")
        except IOError:
            pass
        try:
            os.remove("Base.csv")
        except IOError:
            pass

    def test_save_one_rectangle(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        Rectangle.save_to_file_csv([r1])
        with open("Rectangle.csv", "r", encoding="utf-8") as file_open:
            self.assertTrue("10,2,8,5,9", file_open.read())

    def test_save_multiple_rectangles(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r", encoding="utf-8") as file_open:
            self.assertTrue("10,2,8,5,9\n1,2,8,5,9", file_open.read())

    def test_save_one_square(self):
        s1 = Square(10, 8, 5, 9)
        Square.save_to_file_csv([s1])
        with open("Square.csv", "r", encoding="utf-8") as file_open:
            self.assertTrue("10,8,5,9", file_open.read())

    def test_save_multiple_square(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file_csv([s1, s2])
        with open("Square.csv", "r", encoding="utf-8") as file_open:
            self.assertTrue("10,8,5,9\n2,8,5,9", file_open.read())

    def test_save_class_name(self):
        s1 = Square(10, 8, 5, 9)
        Base.save_to_file_csv([s1])
        with open("Base.csv", encoding="utf-8") as file_open:
            self.assertTrue("10,8,5,9", file_open.read())

    def test_csv_overwrite(self):
        s1 = Square(10, 8, 5, 9)
        Square.save_to_file_csv([s1])
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file_csv([s2])
        with open("Square.csv", encoding="utf-8") as file_open:
            self.assertTrue("2,8,5,9", file_open.read())

    def test_save_None(self):
        Square.save_to_file_csv(None)
        with open("Square.csv", encoding="utf-8") as file_open:
            self.assertEqual("[]", file_open.read())

    def test_save_empty_list(self):
        Square.save_to_file_csv([])
        with open("Square.csv", encoding="utf-8") as file_open:
            self.assertEqual("[]", file_open.read())

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([], [])


class TestBase_load_from_file_csv_method(unittest.TestCase):
    """
    Unittest to test the load_from_file_csv method
    """
    @classmethod
    def tearDown(self):
        """
        Deletes all created files on exit
        """
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    # tests for rectangle
    def test_load_first_rect(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r1), str(output[0]))

    def test_load_other_rect(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertEqual(str(r2), str(output[1]))

    def test_rectangle_types(self):
        r1 = Rectangle(10, 2, 8, 5, 9)
        r2 = Rectangle(1, 2, 4, 5, 3)
        Rectangle.save_to_file_csv([r1, r2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(item) == Rectangle for item in output))

    # test for square
    def test_first_square(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertEqual(str(s1), str(output[0]))

    def test_other_square(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertEqual(str(s2), str(output[1]))

    def test_square_types(self):
        s1 = Square(10, 8, 5, 9)
        s2 = Square(2, 8, 5, 9)
        Square.save_to_file_csv([s1, s2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(item) == Square for item in output))

    def test_no_file(self):
        output = Square.load_from_file_csv()
        self.assertEqual([], output)

    def test_multiple_args(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], [])


if __name__ == "__main__":
    unittest.main()
