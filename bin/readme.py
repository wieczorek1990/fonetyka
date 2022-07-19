#!/usr/bin/env python
import glob


def get_links():
    files = glob.glob('ogg/*.ogg')
    names = [file.lstrip('ogg/').rstrip('.ogg') for file in files]
    return [
        f'* [{name}](</{file}>)' for name, file in zip(names, files)
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

