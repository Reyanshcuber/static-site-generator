from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def leaf_to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return self.value
        if self.tag != "a":
            return f"<{self.tag}>{self.value}</{self.tag}>"
        # anchor tag with possible props
        props_str = self.props_to_html()
        attrs = f" {props_str}" if props_str else ""
        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"

    def to_html(self):
        if self.tag is None:
            return self.value
        props_str = self.props_to_html()
        attrs = f" {props_str}" if props_str else ""
        return f"<{self.tag}{attrs}>{self.value}</{self.tag}>"