#!/usr/bin/env python

def load(filename):
    with open(filename) as file:
        return file.read().splitlines()


def transform(letters, vowels):
    groups = []
    for letter in letters:
        group = []
        for vowel in vowels:
            if letter == vowel:
                group.append(vowel)
            group.append(f'{letter}{vowel}')
        group.append('')
        groups.append(group)
    return groups, sum(groups, [])


def main():
    letters = load('letters.txt')
    vowels = load('vowels.txt')
    _, lines = transform(letters, vowels)
    lines_with_newlines = [f'{line}\n' for line in lines]
    with open('list.txt', 'w') as file:
        file.writelines(lines_with_newlines)


if __name__ == '__main__':
    main()

