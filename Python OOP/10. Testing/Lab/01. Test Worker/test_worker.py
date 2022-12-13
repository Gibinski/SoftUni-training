from unittest import TestCase, main
from worker import Worker


class WorkerTests(TestCase):

    def setUp(self):
        self.worker = Worker("TestGuy", 1000, 100)

    def test_correct_initializiong(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_increment_money_on_woeker(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_decreas_enerdy_on_worker_when_working(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_raise_exeprion_when_worker_is_working_with_negative_or_zero_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increase_energy_with_one_after_rest(self):
        self.worker.rest()
        self.assertEqual(101, self.worker.energy)

    def test_correct_get_info(self):
        get_info = self.worker.get_info()
        self.assertEqual(f'{self.worker.name} has saved {self.worker.money} money.', get_info)

if __name__ == "__main__":
    main()
