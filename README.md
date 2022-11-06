# imagnify

extract all the links from a website. see all the media link and download the media files from a site.

<h4>1.) Downloading images without link ;</h4>

for downloading images without link use the option '-a' and the statements will look like the following<br>
<code>python3 reciver.py -a keywords keywords1 keywords2.... -m</code> ( '-m' option is used to see only media files)
Here keywords denote the words you want to search, for an example you want to get photos of the beautiful mountains. then the command to get all the image files will be 
<code>python3 reciver.py -a beautiful mountains -m</code>

<h4> Extracting urls from the website link </h4>
if you just want to extract the links from the website or download media links then use the following command<br>
<code>python3 reciver.py [link] -m </code> (you can use the command without option '-m' also but it will print all the urls including media links)
