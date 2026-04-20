#!/usr/bin/env python3
import glob

DEFAULT_EXTENSION = 'wav'
NEWLINE = '<br/>'
RAW_ROOT = 'https://github.com/wieczorek1990/fonetyka/raw/refs/heads/main/wav/'


def get_links(extension=DEFAULT_EXTENSION):
    with open('letters.txt') as file:
        letters = file.read().splitlines()
        return [
            f"""<p>{letter}{NEWLINE}
            <audio controls>
            <source src="{RAW_ROOT}{letter}.{extension}" type="audio/wav">
            Your browser does not support the audio element.
            </audio></p>"""
            for letter in letters
        ]


def main():
    links = get_links()
    with open('readme-template.html') as file:
        content = file.read()
    with open('readme-end-template.html') as file:
        content_end = file.read()

    with open('readme.html', 'w') as file:
        file.write(content)

        if not links:
            file.write('Nic tu nie ma.')
        else:
            links_with_newlines = [f'{link}\n' for link in links]
            file.writelines(links_with_newlines)

        file.write(content_end)

if __name__ == '__main__':
    main()

