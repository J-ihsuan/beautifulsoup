# Milestone-3
#### Overview
The Milestone 3 version of the `SoupReplacer` extends Milestone 2 version to support dynamic and flexible tag transformations during parsing, this new API can modify a tag’s name, attributes, or apply side effects on entire nodes.


## 📍 Comparison of SoupReplacer API — Milestone 2 vs. Milestone 3

#### Milestone 2 — Simple Replacement
##### Design
* Constructor: `SoupReplacer(og_tag, alt_tag)`
* Implementation: When the parser encounters a tag name matching `og_tag`, it replaces it with `alt_tag`.
##### Strengths
* Easy to understand and use for tag renaming (e.g., `<b>` → `<blockquote>`).
* Integrates cleanly into the parsing loop via `handle_starttag` and `handle_endtag`.
##### Limitations
* Only supports tag name replacement.
* Cannot modify tag attributes or manipulate tags contextually.
* Not flexible enough for advanced transformations (e.g., conditional logic).

#### Milestone 3 — Flexible Transformation
##### Design
* Extended constructor:
`SoupReplacer(name_xformer = None, attrs_xformer = None, xformer = None)`
* Adds functional “transformer” interfaces
    * `name_xformer(tag)` : returns a new tag name.
    * `attrs_xformer(tag)` : returns a modified attribute dictionary.
    * `xformer(tag)` : applies arbitrary side effects on the tag (e.g., remove or modify attributes).

##### Strengths
* Supports conditional logic for renaming, attribute modification, and tag-level side effects.
* All transformations occur during parsing.
* Extensible for advanced modification.

##### Limitations
* More complicated — users must understand tag object behavior and parsing order.
* Harder to debug because transformations happen in real time as the parser runs.

## 📍 Recommendation
| Task Description   | Example |Implementation       |
|:-------------------|:----------------|:---------|
| Replace specific tags name| `<b>` -> `<blockquote>`| **Milestone 2** - `SoupReplacer(og_tag, alt_tag)`|
| Perform advanced transformations | `<b>` -> `<b class = "test">`| **Milestone 3** - `SoupReplacer(name_xformer = None, attrs_xformer = None, xformer = None)`|

## 📍 SoupReplacer API - Milestone 3 ver.

> ##### Change Log
| File             | Line          | Description                            |
|:----------------:|:-------------:|----------------------------------------|
| `bs4/soupReplacer.py` | `1 ~ 35` | Defines the `SoupReplacer()` class.    |
| `bs4/__init__.py`| `1023 ~ 1027` | Applies the transformations when `replacer` is not `None` and a `start tag` is encountered during parsing |
| `bs4/__init__.py`| `1057 ~ 1059` | Apply `xformer()` while the Tag object exists |
| `bs4/__init__.py`| `1077 ~ 1079` | Applies the transformations when `replacer` is not `None` and an `end tag` is encountered during parsing |
>###### Expand milestone 2 and move `SoupReplacer` class from `element.py` to a separate `soupreplacer.py` file.

#### Testing - test_soupReplacer.py
Please use the following command to test
> ```python
> pytest -v bs4/tests/test_soupReplacer.py
> ```
The test file adds six test cases using pytest:
* `test_html_name_xformer()` Verifies that all `<b>` tags in an HTML document are renamed to `<blockquote>` using `name_xformer`.
* `test_xml_name_xformer()` Verifies that all `<row>` tags in an XML document are renamed to `<holiday>` using `name_xformer`.
* `test_html_attrs_xformer()` Verifies that all `<i>` tags in an HTML document have their `'id'` attribute set to `"2026 Fall"` using `attrs_xformer`.
* `test_xml_attrs_xformer()` Verifies that all `'Id'` attributes on `<row>` tags in an XML document are renamed to `'id'` using `attrs_xformer`.
* `test_html_xformer()` Verifies that `xformer` correctly mutates existing `'id'` attributes in HTML by prefixing their values with `"UCI "`.
* `test_xml_xformer()` Verifies that `xformer` removes all `'Id'` attributes from `<row>` tags in an XML document.

#### Applying - task7.py
* [**Cs231n.html**](https://cs231n.stanford.edu)
* Change all `<p>` to `<p class = "test">`.

> ##### Input preview
> ```html
> <h3>Assignments (45%)</h3>
> <p>See the <a href="assignments.html">Assignments</a> page for details regarding assignments, late days and collaboration policies.</p>
> <h3>Midterm (20%)</h3>
> <p>Detailed information regarding the midterm will be made available as an announcement on Ed in the coming weeks.</p>
> ```

> ##### Output preview
> ```html
>  <h3>
>   Assignments (45%)
>  </h3>
>  <p class="test">
>   See the
>   <a href="assignments.html">
>    Assignments
>   </a>
>   page for details regarding assignments, late days and collaboration policies.
>  </p>
> ```