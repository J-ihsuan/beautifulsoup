# Milestone-2

##  Test Data
#### [**Posts.xml**](https://archive.org/details/stackexchange$0)
- From superuser.com.7z
- **1.64 GB** file with 2 levels of nesting. 

```xml
<?xml version="1.0" encoding="utf-8"?>
<posts>
  <row Id="1" PostTypeId="1" AcceptedAnswerId="727273" CreationDate="2009-07-15T06:27:46.723" Score="181" ViewCount="123363" Body="&lt;p&gt;A Vista virtual machine I use only has a 10 GB virtual hard disk -- and I'm worried about it running out of space over time.&lt;/p&gt;&#xA;&lt;p&gt;I used &lt;a href=&quot;http://www.jam-software.com/treesize_free/&quot;... />
  <row Id="24" PostTypeId="1" CreationDate="2009-07-08T16:32:47.817" Score="7" ViewCount="6666" Body="&lt;p&gt;I used to record important technical meetings and demos using Camtasia Studio, using a Mic to capture the speaker voice.&lt;/p&gt;&#xA;&#xA;&lt;p&gt;Sometimes we invite attendees by asking them to call us in the meeting, and they would call on a cell phone... /> 
  <row Id="25" PostTypeId="2" ParentId="24" CreationDate="2009-07-08T16:34:52.867" Score="0" Body="&lt;p&gt;You could use a filter on the recording. A low-pass filter should do the trick, since the frequency of noise is usually pretty high.&lt;/p&gt;&#xA;" OwnerUserId="9637" OwnerDisplayName="Burkhard" LastEditorUserId="1218738" LastEditDate="2020-10-09T16:36:16... />
  <row Id="26" PostTypeId="2" ParentId="24" CreationDate="2009-07-08T16:59:00.587" Score="0" Body="&lt;p&gt;Try out something like Audible for Macs, and Sound Forge or Adobe Audition for Windows. The latter should do it real well. You will likely have to build a custom ex to cut out at certain frequencies to first locate, then isolate and reduce the noise. Chanc... />
```

## 📍 Part 1 - Supplementary Notes
#### task2.py
* Print out all `CreationDate` attributes from `<row>` tags, as the equivalent of printing all hyperlinks from `<a>` tags.

> ##### Output preview
> ```xml
> 2009-07-15T06:27:46.723
> 2009-07-08T16:32:47.817
> 2009-07-08T16:34:52.867
> 2009-07-08T16:59:00.587
> 2009-07-08T17:15:59.477
> ```

#### task3.py
* Print out all tags.

> ##### Output preview
> ```xml
> posts
> row
> row
> row
> row
> ```

#### task4.py
* Print out all `AcceptedAnswerId` attributes.
    * In this XML file, the attribute name is capitalized, unlike the typical lowercase **`id`** used in HTML. 
    * Since each `<row>` tag has an `Id` attribute, we look for `AcceptedAnswerId` instead. 

> ##### Output preview
> ```xml
> <row AcceptedAnswerId="727273" AnswerCount="12" Body="&lt;p&gt;A Vista virtual machine I use only has a 10 GB virtual hard disk -- and I'm worried about it running out of space over time.&lt;/p&gt;... />
> <row AcceptedAnswerId="42" AnswerCount="9" Body="&lt;p&gt;What is the difference between the two super user commands, &lt;code&gt;su -s&lt;/code&gt; and &lt;code&gt;sudo -s&lt;/code&gt;?&lt;/p&gt;&lt;p&g... />
> <row AcceptedAnswerId="3841" AnswerCount="3" Body="&lt;p&gt;My late 2008, Macbook Pro Unibody machine has a number of ugly flaws that rear their head under Windows (Bootcamp):&lt;/p&gt;... />
> ```

## 📍 Part 2 - API Source Locations

| API               | File             | Line          |
|-------------------|:----------------:|:-------------:|
| `BeautifulSoup()` | `bs4/__init__.py`| `133 ~ 309`   |
| `prettify()`      | `bs4/element.py` | `2601 ~ 2617` |
| `get()`           | `bs4/element.py` | `2160 ~ 2171` |
| `find()`          | `bs4/element.py` | `2684 ~ 2711` |
| `find_all()`      | `bs4/element.py` | `2715 ~ 2745` |
| `find_parent()`   | `bs4/element.py` | `992 ~ 1018`  |
| `clear()`         | `bs4/element.py` | `2093 ~ 2105` |
| `SoupStrainer()`  | `bs4/filter.py`  | `313 ~ 396`   | 

## 📍 Part3 - SoupReplacer
**`SoupReplacer()`** is a new API that does those additions / replacements during parsing, not after. By doing this during parsing, we avoid having to traverse the parse tree all over again when we want to make those changes.

> ##### Change Log
| File             | Line          | Description                            |
|:----------------:|:-------------:|----------------------------------------|
| `bs4/element.py` | `2888 ~ 2898` | Defines the `SoupReplacer()` class.    |
| `bs4/__init__.py`| `89`          | Import `SoupReplacer` from `element.py`|
| `bs4/__init__.py`| `184`         | Adds a **type hint** for the class attribute `replacer` |
| `bs4/__init__.py`| `217`         | Defines the `replacer` parameter in the `BeautifulSoup` constructor, allowing a `SoupReplacer` object to be passed in.|
| `bs4/__init__.py`| `441`         | Initializes the `replacer` instance attribute|
| `bs4/__init__.py`| `1023 ~ 1027` | Applies the replacement when `replacer` is not `None` and a `start tag` is encountered during parsing |
| `bs4/__init__.py`| `1071 ~ 1075` | Applies the replacement when `replacer` is not `None` and an `end tag` is encountered during parsing |

#### Applying - task6.py
* Change all `<row>` to `<blockquote>`.

> ##### Output preview
> ```xml
> <?xml version="1.0" encoding="utf-8"?>
>    <posts>
>        <blockquote AcceptedAnswerId="727273" AnswerCount="12" Body="&lt;p&gt;A Vista virtual machine I use only has a 10 GB virtual hard disk -- and I'm worried about it running out of... />
>        <blockquote AnswerCount="6" Body="&lt;p&gt;I used to record important technical meetings and demos using Camtasia Studio, using a Mic to capture the speaker voice.&lt;/p&gt... />
> ```

#### Testing - test_soupReplacer.py
Please use the following command to test
> ```python
> pytest -v bs4/tests/test_soupReplacer.py
> ```
The test file contains two test cases using pytest:
* `test_html_replacement()`
Verifies that all `<b>` tags in an HTML document are replaced by `<blockquote>` tags.
* `test_xml_replacements()`
Verifies that all `<row>` tags in an XML document are replaced by `<holiday>` tags.