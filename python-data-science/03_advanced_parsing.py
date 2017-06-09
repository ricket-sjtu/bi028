import lxml.html

page = lxml.html.parse("http://www.blocket.se/stockholm?q=apple")

print len(page.xpath('//a')) # number of links in the page
print page.xpath('//img[@class = "item_image"]/@src') # products' images