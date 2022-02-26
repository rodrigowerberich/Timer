import time
from typing import AnyStr

from IPrinter import IPrinter


class StdPrinter(IPrinter):

    def print(self, string: AnyStr, end='\n'):
        print(string, end)


class Timer:
    def __init__(self):
        self._initial_time = time.perf_counter()
        self.__last_used_time = self._initial_time
        self._elapsed_times = []
        self._stop_times = []
        self._stop_times_labels = []
        self._printer = StdPrinter()

    def __check_if_stop_called(self):
        if len(self._stop_times) == 0:
            raise Exception('Stop has never been called')

    def start(self):
        self._initial_time = time.perf_counter()
        self.__last_used_time = self._initial_time
        self._elapsed_times = []
        self._stop_times = []
        self._stop_times_labels = []

    def mark(self, label=''):
        current_time = time.perf_counter()
        if label == '':
            label = 'Time ' + str(len(self._stop_times) + 1)
        self._stop_times.append(current_time)
        self._stop_times_labels.append(label)
        self._elapsed_times.append(current_time - self.__last_used_time)
        self.__last_used_time = current_time

    def pause(self, label=''):
        self.mark(label)

    def resume(self):
        current_time = time.perf_counter()
        self.__last_used_time = current_time

    def latest_time_measured(self):
        self.__check_if_stop_called()
        return self._elapsed_times[-1]

    def times_measured(self):
        return self._elapsed_times

    def times_measured_with_labels(self):
        return zip(self._stop_times_labels, self._elapsed_times)

    def set_printer(self, printer: IPrinter):
        self._printer = printer

    def print(self, digits=5):
        for label, time_elapsed in zip(self._stop_times_labels, self._elapsed_times):
            self._printer.print('{label}: {time_elapsed:0.{digits}f}s'.format(label=label, time_elapsed=time_elapsed, digits=digits))
