from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag=tag,children=children,props=props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent nodes must have a tag")
        if self.children is None:
            raise ValueError("Parent nodes must have children")
        children_html=""
        for child in self.children:
            children_html+=child.to_html()
        if self.props:
            props_str=""
            for key,value in self.props.items():
                props_str+=f' {key}="{value}"'
            return f"<{self.tag}{props_str}>{children_html}</{self.tag}>"
        return f"<{self.tag}>{children_html}</{self.tag}>"
        
