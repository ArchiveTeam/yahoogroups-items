import os
import sys
import typing

SIZE = 500000


def main(filepaths: typing.Union[str, typing.List[str]]):
    added = set()
    for filename in os.listdir('ADDED'):
        with open(os.path.join('ADDED', filename), 'r') as f:
            added |= {s.strip() for s in f}
    for filepath in filepaths:
        filename = filepath.rsplit('/', 1)[1]
        with open(filepath, 'r') as f_in:
            items = {s.strip() for s in f_in}
            unique = sorted(items-added)
            for i in range(0, len(unique), SIZE):
                with open('{}.{}'.format(filename, str(int(i/SIZE)).zfill(3)), 'w') as f_out:
                    f_out.write('\n'.join(unique[i:i+SIZE]))
            added |= items
        os.rename(filepath, os.path.join('ADDED_RAW', filename))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise ValueError('Please give list as argument.')
    main(sys.argv[1:])

