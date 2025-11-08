from bs4 import BeautifulSoup
from bs4.soupReplacer import SoupReplacer

# Milestone 2
def test_html_replacement():
    html = "<html><body><b><b>bold</b></b></body></html>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, "html.parser", replacer = replacer)
    assert soup.find("b") is None
    assert soup.find("blockquote") is not None
    assert len(soup.find_all("blockquote")) == 2

def test_xml_replacements():
    xml = '<post><row Id="1" Date="2025/10/31"/><p>Holloween</p><row Id="2" Date="2025/12/25"/><p>Xmas</p><row Id="3" Date="2025/01/01"/><p>New Year</p></post>'
    replacer = SoupReplacer("row", "holiday")
    soup = BeautifulSoup(xml, "xml", replacer = replacer)
    assert soup.find("row") is None
    assert soup.find("holiday") is not None
    assert len(soup.find_all("holiday")) == 3

# Milestone 3
## Change tag's name through name_xformer (html)
def test_html_name_xformer():
    html = "<html><body><b><b>bold</b><i>MSWE</i></b></body></html>"
    b_to_blockquote = SoupReplacer(name_xformer = lambda tag: "blockquote" if tag.name == "b" else tag.name)
    soup = BeautifulSoup(html, "html.parser", replacer = b_to_blockquote)
    assert soup.find("b") is None
    assert soup.find("blockquote") is not None
    assert soup.find("i") is not None

## Change tag's name through name_xformer (xml)
def test_xml_name_xformer():
    xml = '<?xml version="1.0" encoding="utf-8"?><post><row Id="1" Date="2025/10/31"/><p>Holloween</p><row Id="2" Date="2025/12/25"/><p>Xmas</p><row Id="3" Date="2025/01/01"/><p>New Year</p></post>'
    row_to_holiday = SoupReplacer(name_xformer = lambda tag: "holiday" if tag.name == "row" else tag.name)
    soup = BeautifulSoup(xml, "xml", replacer = row_to_holiday)
    assert soup.find("row") is None
    assert soup.find("holiday") is not None
    assert soup.find("p") is not None

## Add and change attributes through attrs_xformer (html)
def test_html_attrs_xformer():
    html = '<html><body><b><i id="2025 Summer">bold</i><i>MSWE</i></b></body></html>'
    def add_id(tag):
        attrs = dict(tag.attrs)
        if tag.name == "i":
            attrs["id"] = "2026 Fall"
        return attrs

    replacer = SoupReplacer(attrs_xformer = add_id)
    soup = BeautifulSoup(html, "html.parser", replacer = replacer)
    assert soup.find(id = True) is not None
    assert len(soup.find_all(id = "2026 Fall")) == 2

## Rename attributes through attrs_xformer (xml: Id -> id)
def test_xml_attrs_xformer():
    xml = '<?xml version="1.0" encoding="utf-8"?><post ID="a"><row Id="1" Date="2025/10/31"/><p>Holloween</p><row Id="2" Date="2025/12/25"/><p>Xmas</p><row Id="3" Date="2025/01/01"/><p>New Year</p></post>'
    def rename_rowId(tag):
        attrs = dict(tag.attrs)
        if "Id" in attrs:
            attrs["id"] = attrs.pop("Id")
        return attrs

    replacer = SoupReplacer(attrs_xformer = rename_rowId)
    soup = BeautifulSoup(xml, "xml", replacer = replacer)
    assert soup.find(ID = True) is not None
    assert soup.find("row", Id = True) is None
    assert len(soup.find_all(id = True)) == 3

## Modify id attributes through xformer (html)
def test_html_xformer():
    html = '<html><body><b><i id="2025 Summer">bold</i><i>MSWE</i></b></body></html>'
    def modify(tag):
        if "id" in tag.attrs:
            tag.attrs["id"] = "UCI " + tag.attrs["id"]

    replacer = SoupReplacer(xformer = modify)
    soup = BeautifulSoup(html, "html.parser", replacer = replacer)
    assert soup.find("i")["id"].startswith("UCI ")

## Remove all "id" attributes through xformer (xml)
def test_xml_xformer():
    xml = '<?xml version="1.0" encoding="utf-8"?><post ID="a"><row Id="1" Date="2025/10/31"/><p>Holloween</p><row Id="2" Date="2025/12/25"/><p>Xmas</p><row Id="3" Date="2025/01/01"/><p>New Year</p></post>'
    def remove_Id(tag):
        if "Id" in tag.attrs:
            del tag.attrs["Id"]

    replacer = SoupReplacer(xformer = remove_Id)
    soup = BeautifulSoup(xml, "xml", replacer = replacer)

    assert "Id" not in soup.find("row")
    assert len(soup.find_all(ID = True)) == 1
    assert len(soup.find_all(id = True)) == 0

#pytest -s bs4/tests/test_soupReplacer.py