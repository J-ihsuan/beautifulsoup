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
        output = "../prettyfied_b.html"
    elif filename.endswith(".xml"):
        parser = "xml"
        output = "../prettyfied_b.xml"
    else:
        print("Please input .html or .xml file only.")
        return   

    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser)

    # Change all the <b> tags to <blockquote> tags and write the tree onto a file
    for node in soup:
        if node.name == "b":
            node.name = "blockquote"

    ## Check
    # for node in soup:
    #     if node.name == "blockquote":
    #         print(node) 

    with open(output, "w") as o:
        o.write(soup.prettify())


if __name__ == "__main__":
    main()

##python3 apps/m4/task6.py ../CS231n.html