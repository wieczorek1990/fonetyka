#!/usr/bin/env python

def main():
    links = []
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

