class SoupReplacer:
    def __init__(
        self, og_tag = None, alt_tag = None, name_xformer = None, attrs_xformer = None, xformer = None
    ):
        self.og_tag = og_tag
        self.alt_tag = alt_tag
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer
    
    def replace(self, tagname, attrs = None):
        # Milestone 2
        if tagname == self.og_tag:
            tagname = self.alt_tag

        # Milestone 3
        attrs_d = dict(attrs or {})
        dummy_tag = type("DummyTag", (), {"name": tagname, "attrs": attrs_d})()
        
        if self.name_xformer:
            new_name = self.name_xformer(dummy_tag)
            if new_name:
                tagname = new_name

        if self.attrs_xformer:
            new_attrs = self.attrs_xformer(dummy_tag)
            if new_attrs:
                attrs_d = new_attrs

        return tagname, attrs_d
    
    # Used after tag creation
    def apply_xformer(self, tag):
        if self.xformer:
            self.xformer(tag)