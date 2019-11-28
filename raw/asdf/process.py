import os


def main():
    for filename in os.listdir('.'):
        if not filename.endswith('.txt'):
            continue
        with open(filename, 'r') as f_in, \
                open(filename + '.processed', 'w') as f_out:
            items = {'group:' + s.strip().split(' ', 1)[0] for s in f_in}
            f_out.write('\n'.join(sorted(items)))

if __name__ == '__main__':
    main()

