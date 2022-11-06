import os
import sys
import requests
from parse import Parser


if len(sys.argv) < 2:
    print("Usage: python3 linker.py <link>/-a [keywords] [options...]")
    sys.exit()

# 1. processing and connecting to a link .
# 2. writing and parsing html file.
# 3. presenting to user what he want to see.
is_only_media_link = True if '-m' in sys.argv else False

# removing file name from the arguments from the command line.
# so that we are only left with CLI-options and their values.
sys.argv.remove('reciver.py')
if is_only_media_link : sys.argv.remove('-m')

if '-a' in sys.argv:
    sys.argv.remove("-a") # as '-a' is not needed in arguments.
    # searchin on yandex image search engine, yandex search images on 
    # the basis of keys in the format http...../key1%20key2%20
    # for ex:- https://yandex.com/..../gautam%20kumar%20%thakur
    keys = '%20'.join(sys.argv[0:])
    link = 'https://yandex.com/images/search?text=' + keys
else:
    link = sys.argv[0]

# connecting to the server and retriving the links.
from_site = requests.get(link)
html_text = from_site.text
my_parser = Parser(html_text)
mlinks, links = my_parser.parse()


if is_only_media_link:
    # this means that user wants to see only media links.
    my_parser.printMediaLinks(mlinks)
else:
    my_parser.printAllLinks(links-mlinks)

input("press \033[01;92m[enter]\033[00m "
"to continue downloading media files...")

# since all the image files will going to be stored in images directory.
os.mkdir('images')
os.chdir('images')
for lino, link in enumerate(mlinks):
    os.system(f"wget '{link}' -O image{lino}")

os.system("open image1") # opening the first media file
input("press \033[01;04;92m[ENTER]\033[00m "
"to continue deleting the file...")
os.system("rm image*")


