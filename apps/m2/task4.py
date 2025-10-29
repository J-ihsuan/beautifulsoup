from bs4 import SoupStrainer, BeautifulSoup
import sys

""" 
Print out all `AcceptedAnswerId` attributes
As in the test XML file, the attribute name is Id (capitalized), unlike the typical lowercase id used in HTML
Since each <row> tag has an Id attribute, we look for AcceptedAnswerId instead.
"""

def main():
    if len(sys.argv) < 2:
        print("Please use the following command: python3 task4.py <filename>")
        return
    
    parser = ""
    filename = sys.argv[1]

    # Parse all tags that have "Id" attribute
    only_row_tags = SoupStrainer(True, attrs={"AcceptedAnswerId": True})

    if filename.endswith(".html"):
        parser = "html.parser"
    elif filename.endswith(".xml"):
        parser = "xml"
    else:
        print("Please input .html or .xml file only.")
        return     

    with open(filename, "r") as f:
        soup = BeautifulSoup(f, parser, parse_only = only_row_tags)

    if not soup:
        print('No tag with an Id attribute were found in this file.')
    else:
        for tag in soup:
            print(tag)


if __name__ == "__main__":
    main()

##python3 apps/m2/task4.py ../Posts.xml