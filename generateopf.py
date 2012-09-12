#!/usr/bin/python
import os
import sys
import glob
import re

numbers = re.compile("(\d+|\D+)")

def create_ncx():
    f = open('toc.ncx', 'w')
    con = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN"
	"http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">

<!--
	For a detailed description of NCX usage please refer to:
	http://www.idpf.org/2007/opf/OPF_2.0_final_spec.html#Section2.4.1
-->

<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1" xml:lang="en-US">
<head>
<meta name="dtb:uid" content="BookId"/>
<meta name="dtb:depth" content="2"/>
<meta name="dtb:totalPageCount" content="0"/>
<meta name="dtb:maxPageNumber" content="0"/>
</head>
<docTitle><text>Genaric TOC</text></docTitle>
<docAuthor><text>Barkley Press</text></docAuthor>
  <navMap>

  </navMap>
</ncx>
"""
    f.write(con)

def create_opf(meta) : #creates the opf file for compiling
    f = open('book.opf', 'w')
    f.write('<?xml version="1.0" encoding="utf-8"?>\n')
    f.write('\t<package xmlns="http://www.idpf.org/2007/opf" version="2.0" unique-identifier="BookId">\n')
    f.write('\t<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">\n')
    f.write('\t\t<dc:title>' + meta['title'] + '</dc:title>\n')
    f.write('\t\t<dc:language>' + meta['lang'] + '</dc:language>\n')
    f.write('\t\t<meta name="cover" content="My_Cover" />\n')
    f.write('\t\t<dc:identifier id="BookId" opf:scheme="ISBN">' + str(meta['ISBN']) + '</dc:identifier>\n')
    if type(meta['author']) == list :#Lists all authors if there are more than one, unfortunalty moot since there is no method for multiple author entry, but hey, it's beta not everything is meant to be implemented
        for author in meta['author'] :
            f.write('\t\t<dc:creator>' + author + '</dc:creator>')
    else :
        f.write('\t\t<dc:creator>' + meta['author'] + '</dc:creator>\n')
        
    f.write('\t\t<dc:publisher>' + meta['publisher'] + '</dc:publisher>\n')
    f.write('\t\t<dc:subject>' + meta['subject'] + '</dc:subject>\n')
    f.write('\t</metadata>\n')
    f.write('<manifest>\n')

    for file in meta['filelist']:
        fileExtension = os.path.splitext(file)[1].lower()
        fileId = os.path.basename(file)
        if fileExtension == '':
            continue
        mediaType = { ".html": "application/xhtml+xml", ".gif": "image/gif", ".jpg": "image/jpeg", ".css": "text/css" }
        f.write('\t<item href="%s" id="%s" media-type="%s" />\n' % (file, fileId, mediaType.get(fileExtension, "application/xhtml+xml")) )

    f.write('\t<item id="My_Table_of_Contents" media-type="application/x-dtbncx+xml" href="toc.ncx" />\n')
    f.write('\t<item id="My_Cover" media-type="image/gif" href="images/cover.jpg"/>\n')
    f.write('</manifest>\n')
    
    f.write('<spine toc="My_Table_of_Contents">\n')

    for file in meta['filelist']:
        fileExtension = os.path.splitext(file)[1]
        fileId = os.path.basename(file)
        if fileExtension == ".html":
            f.write('\t<itemref idref="%s" />"\n' % (fileId))

    f.write('</spine>\n')
    f.write('<guide>\n')
    f.write('\t<reference type="toc" title="Table of Contents" href="' + os.path.basename(meta['filelist'][0]) + '"></reference>\n')
    f.write('\t<reference type="text" title="Welcome" href="' + os.path.basename(meta['filelist'][0]) + '"></reference>\n')
    f.write('</guide>\n')
    f.write('</package>\n')
    return 0

def chunkify(str):
    chunks = numbers.findall(str)
    chunks = [re.match('\d',x) and int(x) or x for x in chunks] #convert numeric strings to numbers
    return chunks

def alphanum(a,b):
	aChunks = chunkify(a)
	bChunks = chunkify(b)
	return cmp(aChunks,bChunks)

if __name__ == '__main__' :
    meta = {}
    meta['author'] = 'Anonymous'
    meta['title'] = 'Untitled'
    meta['lang'] = 'en-us'
    meta['ISBN'] = 7777777777777
    meta['publisher'] = 'Home Press'
    meta['subject'] = 'Unknown'
    
    outputfilename = "book.opf"

    files = []
    for _path, _dirs, _files in os.walk(sys.argv[1]):
        if _files:
            for _file in _files:
                fileExtension = os.path.splitext(_file)[1]
                if fileExtension:
                    files.append(os.path.join(_path,_file))
    files.sort(alphanum)
    
    meta['filelist'] = files

    create_opf(meta)
    create_ncx()
