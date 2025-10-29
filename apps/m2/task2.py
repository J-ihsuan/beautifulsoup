import sys
from bs4 import SoupStrainer, BeautifulSoup

""" 
Print out all CreationDate attributes from <row> tags
as the equivalent of printing all hyperlinks from <a> tags.
"""

def main():
    if len(sys.argv) < 2:
        print("Please use the following command: python3 task2.py <filename>")
        return
    
    parser = ""
    filename = sys.argv[1]
    
    # Parse row tags
    only_row_tags = SoupStrainer("row")

    if filename.endswith(".html"):
        parser = "html.parser"
    elif filename.endswith(".xml"):
        parser = "xml"
    else:
        print("Please input .html or .xml file only.")
        return  
        
    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser, parse_only = only_row_tags)

    # Print all CreationDate in row tag
    if not soup:
        print('No tag <row> were found in this file.')
    else:
        for link in soup:
            print(link.get('CreationDate'))



if __name__ == "__main__":
    main()

##python3 apps/m2/task2.py ../Posts.xml