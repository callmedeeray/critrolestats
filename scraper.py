# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
from lxml import html
# import lxml.html
import requests
#
# # Read in a page
# html = scraperwiki.scrape("https://www.critrolestats.com/dmcrits-wm")  
## need everything in the <ol> elements with class c6
page = requests.get('https://docs.google.com/document/d/e/2PACX-1vS_MbMz0aCPYwVv2xYKRkpM1rqP2tolnIg7wk47Vacdb-HFdeW_Wh7ZJMyEI9M3V3FEHRjClgZCGP9c/pub?embedded=true')
tree = html.fromstring(page.content)

##nat20s = tree.xpath('/html/body/table/tbody/tr[2]/td[1]')
##nat1s = tree.xpath('/html/body/table/tbody/tr[2]/td[2]')
nat20s = tree.xpath('/html/body/table/tbody/tr[2]/td[1]/ol/li[1]/span[1]/text()')
print nat20s
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
