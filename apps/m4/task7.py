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

    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser)

    # Find all the <p> tags and add (or replace) a class attribute class="test" then write the tree onto a file
    for node in soup:
        if node.name == "p":
            node["class"] = "test"

    ## Check
    # for node in soup:
    #     if node.name == "p":
    #         print(node) 

    with open(output, "w") as o:
        o.write(soup.prettify())


if __name__ == "__main__":
    main()

##python3 apps/m4/task7.py ../CS231n.html