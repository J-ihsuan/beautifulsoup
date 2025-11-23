from bs4 import BeautifulSoup
import sys

def main():
    if len(sys.argv) < 2:
        print("Please use the following command: python3 task2.py <filename>")
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

    # Print out type of each node
    for node in soup:
        print(type(node))
    

if __name__ == "__main__":
    main()


##python3 apps/m4/task0.py ../CS231n.html