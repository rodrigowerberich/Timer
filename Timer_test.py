import unittest
import time
from typing import AnyStr

from IPrinter import IPrinter
from Timer import Timer


class StringPrinter(IPrinter):
    def __init__(self):
        self._str = ''

    def print(self, string: AnyStr, end='\n'):
        self._str += string+end

    def content(self):
        return self._str


class TimerTestCase(unittest.TestCase):
    def test_time_once(self):
        wait_time = 1
        timer = Timer()
        timer.start()
        time.sleep(wait_time)
        timer.mark()
        time_elapsed = timer.latest_time_measured()
        self.assertAlmostEqual(time_elapsed, wait_time, 1)

    def test_time_many(self):
        wait_times = [1, 1.3, 0.5, 0.3]
        timer = Timer()

        timer.start()
        for wait_time in wait_times:
            time.sleep(wait_time)
            timer.mark()

        times_elapsed = timer.times_measured()

        for time_elapsed, expected_time in zip(times_elapsed, wait_times):
            self.assertAlmostEqual(time_elapsed, expected_time, 1)

    def test_time_pause(self):
        wait_times = [0.1, 0.2]
        timer = Timer()

        timer.start()
        time.sleep(0.1)
        timer.pause()
        time.sleep(0.1)
        timer.resume()
        time.sleep(0.2)
        timer.pause()

        times_elapsed = timer.times_measured()

        for time_elapsed, expected_time in zip(times_elapsed, wait_times):
            self.assertAlmostEqual(time_elapsed, expected_time, 1)

    def test_time_many_and_get_default_labels(self):
        wait_times = [('Time 1', 0.1), ('Time 2', 0.3)]

        timer = Timer()

        timer.start()
        for wait_time in wait_times:
            time.sleep(wait_time[1])
            timer.mark()

        times_elapsed = timer.times_measured_with_labels()

        for time_elapsed_with_label, expected_time_with_label in zip(times_elapsed, wait_times):
            self.assertEqual(time_elapsed_with_label[0], expected_time_with_label[0])
            self.assertAlmostEqual(time_elapsed_with_label[1], expected_time_with_label[1], 1)

    def test_time_many_and_get_labels(self):
        wait_times = [('Calculated prices', 0.5), ('Danced with a liop', 0.1)]

        timer = Timer()

        timer.start()
        for wait_time in wait_times:
            time.sleep(wait_time[1])
            timer.mark(wait_time[0])

        times_elapsed = timer.times_measured_with_labels()
        for time_elapsed_with_label, expected_time_with_label in zip(times_elapsed, wait_times):
            self.assertEqual(time_elapsed_with_label[0], expected_time_with_label[0])
            self.assertAlmostEqual(time_elapsed_with_label[1], expected_time_with_label[1], 1)

    def test_time_and_retime_many(self):
        group_of_wait_times = [
            [0.1, 0.4, 0.5],
            [0.2, 0.3],
        ]
        timer = Timer()

        for wait_times in group_of_wait_times:
            timer.start()
            for wait_time in wait_times:
                time.sleep(wait_time)
                timer.mark()

            times_elapsed = timer.times_measured()
            for time_elapsed, expected_time in zip(times_elapsed, wait_times):
                self.assertAlmostEqual(time_elapsed, expected_time, 1)

    def test_time_many_and_print(self):
        wait_times = [('Calculated prices', 0.5), ('Danced with a lion', 0.1)]

        printer = StringPrinter()
        timer = Timer()
        timer.set_printer(printer)

        timer.start()
        for wait_time in wait_times:
            time.sleep(wait_time[1])
            timer.mark(wait_time[0])

        timer.print(digits=1)

        self.assertEqual(printer.content(), "Calculated prices: 0.5s\nDanced with a lion: 0.1s\n")


if __name__ == '__main__':
    unittest.main()
