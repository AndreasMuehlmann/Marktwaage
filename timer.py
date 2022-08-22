import numpy as np
import time
import os


class Timer:
    def __init__(self, file_name):
        self.times = []
        self.file_path = os.path.join('timer', file_name)
        with open(self.file_path, 'w') as file:
            file.write('n, mikro_s\n')

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()
        self.times.append(self.end_time - self.start_time)

    def average(self, range_average):
        to_average = self.times[-range_average:]
        self.times = self.times[:-range_average]
        self.times.append(np.mean(to_average))

    def write_file(self):
        with open(self.file_path, 'a') as file:
            for count, delta_time in enumerate(self.times):
                file.write(f'{count},{round(delta_time * 10**6, 5)}\n')

    def write_std_out(self):
        print(self.end_time - self.start_time)
