from bs4 import BeautifulSoup, SoupReplacer

def test_html_replacement():
    html = "<html><body><b><b>bold</b></b></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer = replacer)
    assert soup.find("b") is None
    assert soup.find("blockquote") is not None
    assert len(soup.find_all("blockquote")) == 2

def test_xml_replacements():
    xml = '<post><row Id="1" Date="2025/10/31"/><p>Holloween</p><row Id="2" Date="2025/12/25"/><p>Xmas</p><row Id="3" Date="2025/01/01"/><p>New Year</p><post/>'
    replacer = SoupReplacer("row", "holiday")
    soup = BeautifulSoup(xml, "xml", replacer = replacer)
    assert soup.find("row") is None
    assert soup.find("holiday") is not None
    assert len(soup.find_all("holiday")) == 3