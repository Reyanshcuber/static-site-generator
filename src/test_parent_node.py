import unittest

from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):

    # ---------- BASIC FUNCTIONALITY ----------

    def test_single_child(self):
        node = ParentNode(
            "p",
            [LeafNode(None, "Hello")]
        )
        self.assertEqual(node.to_html(), "<p>Hello</p>")

    def test_multiple_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode("b", "Bold"),
                LeafNode(None, " "),
                LeafNode("i", "Italic"),
            ]
        )
        self.assertEqual(
            node.to_html(),
            "<div><b>Bold</b> <i>Italic</i></div>"
        )

    def test_nested_parent_nodes(self):
        inner = ParentNode(
            "span",
            [LeafNode(None, "Inner text")]
        )
        outer = ParentNode(
            "div",
            [inner]
        )
        self.assertEqual(
            outer.to_html(),
            "<div><span>Inner text</span></div>"
        )

    # ---------- ASSIGNMENT EXAMPLE ----------

    def test_assignment_example(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )

    # ---------- PROPS ----------

    def test_parentnode_with_props(self):
        node = ParentNode(
            "a",
            [LeafNode(None, "Click me")],
            props={"href": "https://example.com"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com">Click me</a>'
        )

    def test_multiple_props(self):
        node = ParentNode(
            "p",
            [LeafNode(None, "Text")],
            props={"class": "text", "id": "para1"}
        )
        self.assertEqual(
            node.to_html(),
            '<p class="text" id="para1">Text</p>'
        )

    # ---------- ERROR HANDLING ----------

    def test_no_tag_raises_error(self):
        node = ParentNode(
            None,
            [LeafNode(None, "Text")]
        )
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children_raises_error(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()

    # ---------- EDGE CASES ----------

    def test_empty_children_list(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

    def test_deeply_nested_structure(self):
        node = ParentNode(
            "div",
            [
                ParentNode(
                    "section",
                    [
                        ParentNode(
                            "p",
                            [LeafNode(None, "Deep text")]
                        )
                    ]
                )
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<div><section><p>Deep text</p></section></div>"
        )

    def test_mixed_leaf_and_parent_children(self):
        node = ParentNode(
            "div",
            [
                LeafNode(None, "Start "),
                ParentNode(
                    "span",
                    [LeafNode("b", "bold")]
                ),
                LeafNode(None, " end")
            ]
        )

        self.assertEqual(
            node.to_html(),
            "<div>Start <span><b>bold</b></span> end</div>"
        )


if __name__ == "__main__":
    unittest.main()
