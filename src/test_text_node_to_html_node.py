import unittest
from text_node_to_html_node import text_node_to_html
from textnode import TextNode, TextType

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_bold_text_node(self):
        node = TextNode("Bold Text", TextType.BOLD)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), "<b>Bold Text</b>")

    def test_italic_text_node(self):
        node = TextNode("Italic Text", TextType.ITALIC)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), "<i>Italic Text</i>")



    def test_plain_text_node(self):
        node = TextNode("Plain Text", TextType.PLAIN)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.to_html(), "Plain Text")
if __name__ == "__main__":
    unittest.main()