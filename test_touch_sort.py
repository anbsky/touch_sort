import tempfile
import string
import random
import os
import datetime

import touch_sort


def test_sort():
    with tempfile.TemporaryDirectory() as base_dir:
        prefixes = []
        for pos in range(0, 22, 3):
            prefixes.append(string.ascii_lowercase[pos:pos + 3])
        random.shuffle(prefixes)
        for subdir_prefix in prefixes:
            subdir = tempfile.TemporaryDirectory(prefix=subdir_prefix, dir=base_dir)
            for file_prefix in prefixes:
                tempfile.TemporaryFile(prefix=file_prefix, dir=subdir.name)

        touch_sort.sort(base_dir)

        sorted_items = []
        for dirpath, dirnames, filenames in os.walk(base_dir):
            for dirname in dirnames:
                sorted_items.append(os.path.join(dirpath, dirname))
            for filename in filenames:
                sorted_items.append(os.path.join(dirpath, filename))

        assert sorted(sorted_items) == sorted(sorted_items, key=os.path.getatime)
