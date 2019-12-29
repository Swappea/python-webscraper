from bs4 import BeautifulSoup

html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <div id="section-1">
        <h3 data-hello="hi">Hello</h3>
    </div>
    <div id="section-2">
        <ul class="items">
            <li class="item">T</li>
            <li class="item">A</li>
            <li class="item">B</li>
        </ul>
        <h3>aAAA</h3>
        <p>T</p>
    </div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# Direct
# print(soup.div)

# find
# el = soup.find('div')
# print(el)

# find all  returns list
# el = soup.findAll('div')
# print(el)

# find by id
# el = soup.find(id='section-2')
# el = soup.find(class_='items')
# el = soup.find(attrs={"data-hello": "hi"})

# select (by css selectors) returns list
# el = soup.select('#section-1')

# get_text
# el = soup.find(class_='item').getText()

# for item in soup.select('.item'):
#     print(item.getText())

# Navigation
# el = soup.body.contents[3].contents[1].find_next_sibling()

# el = soup.find(id='section-2').find_previous_sibling()

# el = soup.find(class_='items').find_parent()

# el = soup.body.contents[3].contents[1].find_next_sibling('p')

# print(el)
