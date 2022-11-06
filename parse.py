import os, sys, time

class Parser():
    def __init__(self, fileContent):
        self.links = set()
        self.mlinks = set()
        self.fileContent = fileContent

    def extractLinksFromFile(self):
        buffer = ''
        stream = True
        for charno, char in enumerate(self.fileContent):
            if char == 'h' and self.fileContent[charno:charno+8] == 'https://': 
                stream = True
            if stream and char in (',', ' ', '\\', '"'):
                self.links.add(buffer)
                stream = False
                buffer = ''
            if stream: 
                buffer += char

        return self.links

    def printMediaLinks(self, links):
        for link in links:
            print(f"\033[01;94m {link}\033[00m")
            # print(link)
            time.sleep(0.025)
        print(f'Total {len(links)} media links found from the site')
        return self.mlinks

    def printAllLinks(self, links):
        for link in links:
            print(f"\033[01;92m {link}\033[00m")
            print(link)
            time.sleep(0.075)

        print(f'Total {len(links)} links found from the site')

    def parse(self):
        links = self.extractLinksFromFile()
        keywords = ('.png', '.jpg', '.jpeg', '.webp?', 
                '.gif', 'i.pinimg.com', '.mp4', '.mp3',
                'images?')

        for lino, link in enumerate(links, start=2):
            search = lambda word: word in link
            if any (map(search, keywords)):
                self.mlinks.add(link)

        return self.mlinks, self.links

if __name__ == '__main__':
    try:
        _file = sys.argv[1]
        myParser = Parser(_file)
        mlinks , links = myParser.parse()
        if sys.argv[2] == '-m': myParser.printMediaLinks(mlinks)
        else: myParser.printAllLinks(links)

    except IndexError: print("Usage: python3 parser.py <file>")
    except FileNotFoundError: print("file not found!")

    
