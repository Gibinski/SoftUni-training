from unittest import TestCase, main
from car_manager import Car

class TestCar(TestCase):

    def setUp(self):
        self.car = Car("Nissan", "Qashqai", 6, 60)


    def test_correct_initializing(self):
        self.assertEqual("Nissan", self.car.make)
        self.assertEqual("Qashqai", self.car.model)
        self.assertEqual(6, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_no_make_raise_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""

        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_no_model_raise_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""

        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_zero_fuel_consumption_raise_exeptions(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_zero_fuel_capacity_raise_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_negative_furl_amount_raise_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_zero_refuel_raise_exeption(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_amount_after_refuel(self):
        self.car.fuel_amount = 0
        self.car.refuel(10)

        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_more_refuel_then_capacity(self):
        self.car.refuel(self.car.fuel_capacity + 1)
        self.assertEqual(60, self.car.fuel_amount)

    def test_drive_more_then_posible(self):
        self.car.fuel_amount = 6
        distance = 100 * 6 / 6
        with self.assertRaises(Exception) as ex:
            self.car.drive(distance + 1)

        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_fuel_amount_reduce(self):
        self.car.fuel_amount = 16
        self.car.drive(100)

        self.assertEqual(10, self.car.fuel_amount)

if __name__ == "__main__":
    main()