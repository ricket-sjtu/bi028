import lxml.html

page = lxml.html.parse("http://www.blocket.se/stockholm?q=apple")
# ^ This is probably illegal. Blocket, please don't sue me!
items_data = []
for el in page.getroot().find_class("item_row"):
    links = el.find_class("item_link")
    images = el.find_class("item_image")
    if links and images:
        items_data.append({"name": links[0].text,
                           "image": images[0].attrib['src']})

print items_data