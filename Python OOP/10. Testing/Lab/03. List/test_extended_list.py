from unittest import TestCase, main


class TestIntegerList(TestCase):
    
    def setUp(self):
        self.integer_list = IntegerList("50", 1, False, 3.5, (2, 4), 2, 3)

    def test_correct_initializing(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)
        
    def test_correct_get_data(self):    
        self.assertEqual([1, 2, 3], self.integer_list.get_data())
        
    def test_adding_with_not_integer_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("100")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_correct(self):
        result = self.integer_list.add(4)

        self.assertEqual([1, 2, 3, 4], result)   
        self.assertEqual([1, 2, 3, 4], self.integer_list._IntegerList__data)

    def test_remove_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(5)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_romove_index_correct(self):
        self.integer_list.remove_index(1)

        self.assertNotIn(2, self.integer_list._IntegerList__data)

    def test_get_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(7)

        self.assertEqual("Index is out of range", str(ie.exception))

    def test_get_correct_index(self):
        self.assertEqual(1, self.integer_list.get(0))

    def test_insert_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(5, 2)

        self.assertEqual("Index is out of range", str(ie.exception))


    def test_index_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, "0")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_index_correct(self):
        self.integer_list.insert(2, 4)
        self.assertEqual([1, 2, 4, 3], self.integer_list._IntegerList__data)

    def test_get_biggest_correct(self):
        self.assertEqual(3, self.integer_list.get_biggest())

    def test_get_index_correct(self):
        self.assertEqual(0, self.integer_list.get_index(1))


if __name__ == "__main__":
    main()