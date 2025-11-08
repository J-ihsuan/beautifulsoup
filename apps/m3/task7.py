from bs4 import BeautifulSoup, SoupReplacer
import sys

def main():
    if len(sys.argv) < 2:
        print("Please use the following command: python3 task7.py <filename>")
        return
    
    parser = ""
    output = ""
    filename = sys.argv[1]

    if filename.endswith(".html"):
        parser = "html.parser"
        output = "../prettyfied_p.html"
    elif filename.endswith(".xml"):
        parser = "xml"
        output = "../prettyfied_p.xml"
    else:
        print("Please input .html or .xml file only.")
        return   

    def add_class(tag):
        attrs = dict(tag.attrs)
        if tag.name == "p":
            attrs["class"] = "test"
        return attrs

    replacer = SoupReplacer(attrs_xformer = add_class)

    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser, replacer = replacer)

    ## print(soup.prettify()) ## Check

    with open(output, "w") as o:
        o.write(soup.prettify())


if __name__ == "__main__":
    main()

##python3 apps/m3/task7.py ../CS231n.html