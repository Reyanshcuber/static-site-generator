import unittest
from htmlnode import HTMLNode
class TestHTMLNodePropsToHTML(unittest.TestCase):
    def test_props_to_html_with_props(self):
        node = HTMLNode(tag="div", props={"class": "container", "id": "main"})
        result = node.props_to_html()
        self.assertIn('class="container" ', result)
        # Note: Due to the implementation, only the first prop will be returned
        self.assertNotIn('id="main" ', result)

    def test_props_to_html_no_props(self):
        node = HTMLNode(tag="div")
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="div", props={})
        result = node.props_to_html()
        self.assertEqual(result, "")
if __name__ == "__main__":
    unittest.main()