#!/usr/bin/env python3

import os
import sys
import shutil
from datetime import datetime, timedelta


def sort(path):
    now = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    root_path, tail = os.path.split(path.rstrip('/'))

    sorted_items = []
    for dirpath, dirnames, filenames in os.walk(path):
        for dirname in dirnames:
            sorted_items.append(os.path.join(dirpath, dirname))
        for filename in filenames:
            sorted_items.append(os.path.join(dirpath, filename))
    sorted_items.sort()
    # dates = date_generator(now)
    temp_path = os.path.join(root_path, tail + '___/')
    os.makedirs(temp_path)
    for item in sorted_items:
        # date = dates.__next__().timestamp()
        # os.utime(item, (date, date))
        shutil.move(item, temp_path)
    shutil.rmtree(path)
    os.rename(temp_path, path)


def date_generator(now):
    while True:
        now = now + timedelta(minutes=1)
        yield now


if __name__ == '__main__':
    print('Sorting {}'.format(sys.argv[1]))
    sort(sys.argv[1])
