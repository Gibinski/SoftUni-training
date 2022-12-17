from unittest import  TestCase, main
from extended_list import IntegerList


class TestIntegerList(TestCase):
    
    def setUp(self):
        self.integer_list = IntegerList("50", 1, False, 3.5, (2, 4), 2, 3)

    def test_correct_initializing(self):
        self.assertEqual([1, 2, 3], self.integer_list._IntegerList__data)
        
    def test_correct_get_data(self):    
        self.assertEqual([1, 2, 3], self.integer_list.get_data())
        
        
        
        # self.assertEqual()

        # self.assertEqual()







if __name__ == "__main__":
    main()