import os


def process_file(filename: str):
    items = set()
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if len(line) == 0:
                continue
            items.add('group:' + line.split('\t')[1])
    with open(filename + '.processed', 'w') as f:
        f.write('\n'.join(sorted(items)))


def main():
    for filename in os.listdir('.'):
        if not filename.endswith('.tsv'):
            continue
        process_file(filename)

if __name__ == '__main__':
    main()

