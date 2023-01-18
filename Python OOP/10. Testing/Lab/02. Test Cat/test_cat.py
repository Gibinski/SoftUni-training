from unittest import TestCase, main
from cat import Cat

class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Ancho")

    def test_correct_initializing(self):
        self.assertEqual("Ancho", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_valid_eating_cat(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_feding_alredy_fed_cat_raise_exeption(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_sleep_expect_to_by_fales(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_cat_sleep_when_cat_is_not_fed_raise_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

if __name__ == "__main__":
    main()