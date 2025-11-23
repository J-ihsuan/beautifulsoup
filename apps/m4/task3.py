import sys
from bs4 import BeautifulSoup

def main():
    if len(sys.argv) < 2:
        print("Please use the following command: python3 task3.py <filename>")
        return
    
    parser = ""
    filename = sys.argv[1]

    if filename.endswith(".html"):
        parser = "html.parser"
    elif filename.endswith(".xml"):
        parser = "xml"
    else:
        print("Please input .html or .xml file only.")
        return  
        
    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser)

    # Print all the tags
    for node in soup:
        if getattr(node, "name"):
            print(node.name)


if __name__ == "__main__": 
    main()

##python3 apps/m4/task3.py ../CS231n.html