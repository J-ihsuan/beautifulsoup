from bs4 import BeautifulSoup, SoupReplacer
import sys

""" 
For html file: Change all <b> to <blockquote>
For xml file: Change all <row> to <blockquote>
"""

def main():
    if len(sys.argv) < 2:
        print("Please use the following command: python3 task6.py <filename>")
        return
    old_tag = ""
    new_tag = "blockquote"
    parser = ""
    output = ""
    replacer_b = None
    filename = sys.argv[1]

    if filename.endswith(".html"):
        old_tag = "b"
        parser = "html.parser"
        output = "../prettyfied_b.html"
        replacer_b = SoupReplacer(og_tag = old_tag, alt_tag = new_tag)

    elif filename.endswith(".xml"):
        old_tag = "row"
        parser = "xml"
        output = "../prettyfied_b.xml"
        replacer_b = SoupReplacer(og_tag = old_tag, alt_tag = new_tag)

    else:
        print("Please input .html or .xml file only.")
        return   

    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser, replacer = replacer_b)

    if not soup:
        print('No tag <', old_tag,'> were found in this file.')
    else:
        with open(output, "w") as o:
            o.write(soup.prettify())

    ##print(soup.prettify())


if __name__ == "__main__":
    main()

##python3 apps/m2/task6.py ../Posts.xml