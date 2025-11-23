from bs4 import BeautifulSoup

# Milestone 4
"""
Test iteration of the simple HTML and XML document
"""

# Check total node count and the soup object itself is included
def test_html_root():
    html = "<html><body><b> bold </b><div> section 1 </div></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    nodes = list(iter(soup))
    assert len(nodes) == 7
    assert soup in nodes


# Check all tag nodes (including document root) are visited
# Verify specific tag <b id="3"> is included 
def test_html_tag():
    html = "<html><body><b> bold <b> bold </b><b id=\"3\"> bold </b></b><div> - section 1- </div><div> - section 2- </div></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    allTag = [n.name for n in soup if getattr(n, "name")] # 8 (7 tag + 1 document)
    b3 = soup.find("b", id="3") 
    assert len(allTag) == 8
    assert "a" not in allTag
    assert "div" in allTag
    assert b3 in list(iter(soup))


# Ckeck traversal finds all bold text nodes
def test_html_text():
    html = "<html><body><b>bold 1<b>bold 2<b>bold 3</b></b></b><div id=\"1\"> - section 1- </div><div id=\"2\"> - section 2- </div></body></html>"
    soup = BeautifulSoup(html, "html.parser")
    bolds = [n for n in soup if str(n) == "bold 1" or str(n) == "bold 2" or str(n) == "bold 3"]
    assert len(bolds) == 3
    assert "bold 2" in bolds
    assert " - section 1 - " not in bolds


# Check all XML tags nodes (including document root) are visited
# Verify specific tag is included or not
# Check the soup object itself and tag <p> are included
def test_xml_tagNroot():
    xml = '<?xml version="1.0" encoding="utf-8"?><post ID="a"><row Id="1" Date="2025/10/31"/><p>Holloween</p><row Id="2" Date="2025/12/25"/><p>Xmas</p><row Id="3" Date="2025/01/01"/><p>New Year</p><row Id="4" Date="2025/4/1"/><p>April Fool</p></post>'
    soup = BeautifulSoup(xml, "xml")
    allTag = [n.name for n in soup if getattr(n, "name")] # 10
    assert len(allTag) == 10
    assert "a" not in allTag
    assert "row" in allTag
    assert soup in list(iter(soup))
    assert soup.find("p") in list(iter(soup))

# Ckeck traversal finds all text nodes
def test_xml_text():
    xml = '<?xml version="1.0" encoding="utf-8"?><post ID="a"><row Id="1" Date="2025/10/31"/><p>Holloween</p><row Id="2" Date="2025/12/25"/><p>Xmas</p><row Id="3" Date="2025/01/01"/><p>New Year</p><row Id="4" Date="2025/4/1"/><p>April Fool</p></post>'
    soup = BeautifulSoup(xml, "xml")
    allText = [n for n in soup if "<" not in str(n) and ">" not in str(n)] # 4
    assert len(allText) == 4
    assert "Xmas" in allText

# pytest -v bs4/tests/test_iterationSoup.py