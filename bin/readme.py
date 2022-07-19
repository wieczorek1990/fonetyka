#!/usr/bin/env python
import glob


def get_links(extension='ogg'):
    with open('letters.txt') as file:
        letters = file.read().splitlines()
    return [
        f'* [{letter}](</{extension}/{letter}.{extension}>)'
        for letter in letters
    ]


def main():
    links = get_links()
    with open('readme-template.md') as file:
        content = file.read()
    with open('readme.md', 'w') as file:
        file.write(content)
        if not links:
            file.write('Nic tu nie ma.\n\n')
        else:
            links_with_newlines = [f'{link}\n' for link in links]
            file.writelines(links_with_newlines)
            file.write('\n')


if __name__ == '__main__':
    main()

