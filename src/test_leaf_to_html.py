import unittest
from leafnode import LeafNode
class TestLeafNodeToHTML(unittest.TestCase):
    def test_leaf_to_html_with_tag(self):
        node = LeafNode(tag="p", value="Hello, World!")
        result = node.leaf_to_html()
        self.assertEqual(result, "<p>Hello, World!</p>")

    def test_leaf_to_html_without_tag(self):
        node = LeafNode(tag=None, value="Just text")
        result = node.leaf_to_html()
        self.assertEqual(result, "Just text")

    def test_leaf_to_html_with_anchor_tag_and_props(self):
        node = LeafNode(tag="a", value="Click here", props={"href": "http://example.com"})
        result = node.leaf_to_html()
        self.assertEqual(result, '<a href="http://example.com">Click here</a>')

    def test_leaf_to_html_raises_value_error_on_none_value(self):
        node = LeafNode(tag="p", value=None)
        with self.assertRaises(ValueError):
            node.leaf_to_html()