import os


def process_file(filename: str):
    with open(filename, 'r') as in_, open(filename + '.processed', 'w') as out:
        items = {'group:' + l.split('\t')[1].strip() for l in in_}
        out.write('\n'.join(sorted(items)))


def main():
    for filename in os.listdir('.'):
        if not filename.endswith('.tsv'):
            continue
        process_file(filename)

if __name__ == '__main__':
    main()

