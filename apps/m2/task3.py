import sys
from bs4 import BeautifulSoup, SoupStrainer

def main():
    if len(sys.argv) < 2:
        print("Please use the following command: python3 task3.py <filename>")
        return
    
    parser = ""
    filename = sys.argv[1]

    # Parse all tags
    all_tags = SoupStrainer(True)

    if filename.endswith(".html"):
        parser = "html.parser"
    elif filename.endswith(".xml"):
        parser = "xml"
    else:
        print("Please input .html or .xml file only.")
        return  
        
    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser, parse_only = all_tags)

    # Print all the tags
    if not soup:
        print('No tag were found in this file.')
    else:
        for tag in soup.find_all(True):
            print(tag.name)

if __name__ == "__main__": 
    main()

##python3 apps/m2/task3.py ../Posts.xml