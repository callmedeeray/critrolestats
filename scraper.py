# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
from lxml import html
import requests
from lxml.html.soupparser import fromstring
from lxml import etree
from io import StringIO
import re



#
# # Read in a page
# html = scraperwiki.scrape("https://www.critrolestats.com/dmcrits-wm")  
## need everything in the <ol> elements with class c6
page = requests.get('https://docs.google.com/document/d/e/2PACX-1vS_MbMz0aCPYwVv2xYKRkpM1rqP2tolnIg7wk47Vacdb-HFdeW_Wh7ZJMyEI9M3V3FEHRjClgZCGP9c/pub?embedded=true')
tree = html.fromstring(page.content)

##root = fromstring(page.content)
##print [child.tag for child in root.iterdescendants()]

nat20s = tree.xpath('//td[1]/ol//span/text()')
nat1s = tree.xpath('//td[2]/ol//span/text()')

nat20s[0] += nat20s[1]
del nat20s[1]

#tbl = []
for chk in nat20s:
    if chk = 'Otyugh (2:17, 2:54:56) Tentacle against Beau':
        chk = chk.replace('2:17', '2-17')
    ep = re.findall(r'2-\d{2}', chk)
    try:
        dat = {"roll": "nat20", "episode": ep[0], "details": chk}
    except:
        dat = {"roll": "nat20", "episode": ep, "details": chk}
    scraperwiki.sqlite.save(unique_keys=['details'], data = dat)
    #tbl.append(dat)

for chk in nat1s: 
    ep = re.findall(r'2-\d{2}', chk)
    try:
        dat = {"roll": "nat1", "episode": ep[0], "details": chk}
    except:
        dat = {"roll": "nat1", "episode": 'unknown', "details": chk}
    scraperwiki.sqlite.save(unique_keys=['details'], data = dat)
    # tbl.append(dat)


#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("ol[class='c6']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
