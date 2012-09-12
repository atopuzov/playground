# (c) Aleksandar Topuzovic <aleksandar.topuzovic(at)gmail.com>
# Simple tool to strip anoying table navigation from html files in CHM
# books. Also removes CSS formatting and adds some tweaks for
# generating books for Kindle

from HTMLParser import HTMLParser
import sys, re, os

def flatten(x):
    result = []
    for el in x:
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el))
        else:
            result.append(el)
    return result

cr = re.compile("\r\n")
nl = re.compile("\n+")

# ----------------------------------------------------------------------------------------
class MyBaseParser(HTMLParser):
    def __init__(self, *args, **kwargs):
        HTMLParser.__init__(self, *args, **kwargs)
        self.singular_tags = [ 'area', 'base', 'br', 'col', 'command', 'embed', 'hr',
                               'img', 'input', 'link', 'meta' , 'param' , 'source' ]
        self.stack = []
        self.out = []
        self.indent_level = 0
    def handle_starttag(self, tag, attrs):
        # if not tag in self.singular_tags:
        #     self.indent_level += 1
        attrs_str = ' '.join('%s="%s"' % (k, v) for k, v in attrs)
        # self.out.append( ' '*self.indent_level + '<%s%s>\n' % (tag, (' ' + attrs_str).rstrip()) )
        self.out.append( '<%s%s>' % (tag, (' ' + attrs_str).rstrip()) )
    def handle_endtag(self, tag):
        # self.indent_level -= 1
        # self.out.append( '\n' + ' '*self.indent_level + '</%s>\n' % tag )
        self.out.append( '</%s>' % tag )
    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
    def handle_data(self, data):
        data = cr.sub('\n', data)
        self.out.append( data )
    def handle_entityref(self, name):
        self.out.append( '&%s;' % name )
    def handle_charref(self, name):
        self.out.append( '&#%s' % name )
    def close(self):
        return nl.sub('\n',''.join(self.out))
    def push_tag_to_stack(self, tag):
        self.stack.append( (tag, len(self.out)) )
    def get_tag_at(self, pos):
        if self.stack:
            tag = self.stack[pos][0] if self.stack[pos] else None
            return tag
        return None
    def get_pos_at(self, pos):
        if self.stack:
            pos = self.stack[pos][1] if self.stack[pos] else None
            return pos
        return None
    def get_tags(self):
        return [t[0] for t in self.stack if t]
    def get_poss(self):
        return [t[1] for t in self.stack if t]
# ----------------------------------------------------------------------------------------
# Remove tags and do some cleanup
class RemoveTagsAndCleanup(MyBaseParser):
    def __init__(self, *args, **kwargs):
        MyBaseParser.__init__(self, *args, **kwargs)
        self.tags_to_remove = [ 'div', 'colgroup', 'col', 'link' ]
        self.attrs_to_remove = [ 'class' ]

    def handle_starttag(self, tag, attrs):
        if tag in self.tags_to_remove:
            return

        if not tag in self.singular_tags:
            #print "PUSH:", self.get_tags(), tag
            self.push_tag_to_stack(tag)

        new_attrs = []
        for (k,v) in attrs:
            if not k in self.attrs_to_remove:
                new_attrs.append((k,v))
        MyBaseParser.handle_starttag(self, tag, new_attrs)

    def handle_endtag(self, tag):
        if tag in self.tags_to_remove:
            return

        if self.stack and self.get_tag_at(-1) != tag:
            #print "Unexpected tag:", tag, ", stack:", self.get_tags()
            top_tag = self.get_tag_at(-1)
            if top_tag == "table":
                if tag in ['td', 'tr']:
                    return

            if top_tag == "td" and tag == "tr":
                #print "End tag:", self.get_tags(), tag
                self.handle_endtag(top_tag)
                self.handle_endtag(tag)
                return
                
            #print "No help for:", self.get_tags(), tag
            return
        
        assert(self.stack)
        #print "POP: ", self.get_tags(), tag
        self.stack.pop()
        MyBaseParser.handle_endtag(self, tag)
# ----------------------------------------------------------------------------------------
# Remove HTML in <pre>
class RemoveHTMLInPre(MyBaseParser):
    def __init__(self, *args, **kwargs):
        MyBaseParser.__init__(self, *args, **kwargs)
        self.inpre = False

    def handle_starttag(self, tag, attrs):
        if self.inpre:
            return
        if tag == "pre":
            self.inpre = True
        MyBaseParser.handle_starttag(self, tag, attrs)

    def handle_endtag(self, tag):
        if tag == "pre":
            self.inpre = False
        if self.inpre:
            return
        MyBaseParser.handle_endtag(self, tag)
# ----------------------------------------------------------------------------------------
class RmTopTable(MyBaseParser):
    def __init__(self, tables_to_remove = 1, *args, **kwargs):
        MyBaseParser.__init__(self, *args, **kwargs)
        self.table_tags = [ 'td', 'tr', 'th', 'thead', 'tbody', 'tfoot', 
                            'colgroup', 'col', 'caption' ]
        self.table = 0
        self.out = []
        self.tables_to_remove = tables_to_remove
        self.tables_to_remove = 1

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.table += 1

        if self.table <= self.tables_to_remove and tag in self.table_tags:
            # print "Removing tag:", tag
            return

        if tag == "table":
            # print "Starting: div"
            MyBaseParser.handle_starttag(self, 'div', '')
        MyBaseParser.handle_starttag(self, tag, attrs)

    def handle_endtag(self, tag):
        if tag == "table":
            # print self.table
            self.table -= 1

        if self.table >= self.tables_to_remove and tag in self.table_tags:
            if tag == 'tr':
                MyBaseParser.handle_starttag(self, 'br', '')
            return

        MyBaseParser.handle_endtag(self, tag)
        if tag == "table":
            # print "Ending: div"
            MyBaseParser.handle_endtag(self, 'div')
# ----------------------------------------------------------------------------------------
class MyHTMLParser(MyBaseParser):
    def __init__(self, *args, **kwargs):
        MyBaseParser.__init__(self, *args, **kwargs)
        self.stack_to_delete = []
        self.tags_to_ignore = []
        self.length = 0
        self.in_table = False
        self.delete = False

    def handle_starttag(self, tag, attrs):
        if self.in_table:
            self.length += 1

        new_attrs = []
        if tag == "img":
            for (k,v) in attrs:
                if k == "src":
                    l = v.split('/')
                    if l[-1] in ['ccc.gif', 'pixel.gif']:
                        return
                    v = 'images/' + l[-1]
                    l = v.split(';')
                    v = l[0]
                new_attrs.append((k,v))
            attrs = new_attrs

        new_attrs = []
        if tag == "a":
            for (k,v) in attrs:
                if k == "href":
                    l = v.split("/")
                    if l[0] == "images":
                        v = 'images/' + l[-1]
                        l = v.split(';')
                        v = l[0]
                new_attrs.append((k,v))
            attrs = new_attrs

        MyBaseParser.handle_starttag(self, tag, attrs)

        if tag == "table":
            self.in_table = True
            self.length = 0

        if self.in_table and tag == "img":
            a = flatten(attrs)
            if ( "images/next.gif" in a or "images/previous.gif" in a or
                 "Previous Page" in a or "Next Page" in a or 
                 "Previous Section" in a or "Next Section" in a ):
                self.delete = True

    def handle_endtag(self, tag):
        if tag == "table":
            self.in_table = False
            if self.delete:
                self.out = self.out[:-self.length-1]
                self.delete = False
                return

        if self.in_table:
            self.length += 1
        MyBaseParser.handle_endtag( self, tag)

    def handle_startendtag(self, tag, attrs):
        if self.in_table:
            self.length += 1
        MyBaseParser.handle_startendtag( self, data)
    def handle_data(self, data):
        if self.in_table:
            self.length += 1
        MyBaseParser.handle_data( self, data)
    def handle_entityref(self, name):
        if self.in_table:
            self.length += 1
        MyBaseParser.handle_entityref( self, name)
    def handle_charref(self, name):
        if self.in_table:
            self.length += 1
        MyBaseParser.handle_charref( self, name)
# ----------------------------------------------------------------------------------------

parser0 = RemoveTagsAndCleanup()
parser1 = RemoveHTMLInPre()

parser2 = MyHTMLParser()
parser3 = RmTopTable()

filename = sys.argv[1]
#print filename
f = open(filename, 'r')
out = f.read()
f.close()

parser0.feed(out)
out = parser0.close()

parser1.feed(out)
out = parser1.close()

parser2.feed(out)
out = parser2.close()

parser3.feed(out)
out = parser3.close()

f = open(filename, 'w')
f.write(out)
f.close()

#print out

