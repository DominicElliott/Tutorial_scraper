
import scraperwiki
import lxml.html

# next line uses the scrape function from the scraperwiki  library, applies it to the url in "" and stores it as object in html
html = scraperwiki.scrape("http://uk.soccerway.com/teams/netherlands/fortuna-sittard/")
# print html
# next line takes the fromstring function from the lxml.html library and applies it the html variable and finally stores it in root
root = lxml.html.fromstring(html)
# use a selector function for html that helps to find markers: it grabs 'td' tags and puts  in  tds (plural of td)
tds = root.cssselect("td")
# print tds
# use for loop to go through each item & do something 
for td  in  tds:
  # attach to lxml or lxml object
  print lxml.html.tostring(td)
  print td.text
  

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
