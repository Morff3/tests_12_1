import runner
import unittest


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        item_walk = runner.Runner('Run1')
        for i in range(10):
            item_walk.walk()
        self.assertEqual(item_walk.distance, 50)

    def test_run(self):
        item_run = runner.Runner('Run2')
        for i in range(10):
            item_run.run()
        self.assertEqual(item_run.distance, 100)

    def test_challenge(self):
        item_1 = runner.Runner('Run3')
        item_2 = runner.Runner('Run4')
        for i in range(10):
            item_1.walk()
            item_2.run()
        self.assertNotEqual(item_1.distance, item_2.distance)


if __name__ == "__main__":
    unittest.main()