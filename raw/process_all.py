import os


def join_collection(directory: str):
    items = set()
    for filename in os.listdir(directory):
        if not filename.endswith('.processed'):
            continue
        with open(os.path.join(directory, filename), 'r') as f:
            items |= set(f)
    if len(items) == 0:
        return
    with open(directory + '.processed', 'w') as f:
        f.write('\n'.join(sorted(items)))


def main():
    for directory in os.listdir('.'):
        if not os.path.isdir(directory):
            continue
        join_collection(directory)

if __name__ == '__main__':
    main()

