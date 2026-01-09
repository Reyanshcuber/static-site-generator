import unittest
from markdown_to_html_node import markdown_to_html_node
from parentnode import ParentNode
from leafnode import LeafNode


class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraph(self):
        md = "This is a paragraph"
        node = markdown_to_html_node(md)
        # should be a div > p
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")

    def test_heading(self):
        md = "## Hello World"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h2>Hello World</h2></div>")

    def test_code_block(self):
        md = "```\nprint('hi')\n```"
        node = markdown_to_html_node(md)
        # pre > code
        self.assertEqual(node.to_html(), "<div><pre><code>print('hi')</code></pre></div>")

    def test_quote(self):
        md = "> Quote line 1\n> Quote line 2"
        node = markdown_to_html_node(md)
        # blockquote containing a paragraph with the combined text
        self.assertEqual(node.to_html(), "<div><blockquote><p>Quote line 1\nQuote line 2</p></blockquote></div>")

    def test_unordered_list(self):
        md = "- Item 1\n- Item 2\n- Item 3"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>")

    def test_ordered_list(self):
        md = "1. First\n2. Second\n3. Third"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>")

    def test_complex_document(self):
        md = """# Title\n\nThis is a paragraph with **bold** and a [link](https://example.com).\n\n- Item A\n- Item B\n\n> A quote\n\n```\ncode()\n```"""
        node = markdown_to_html_node(md)
        expected = (
            "<div>"
            "<h1>Title</h1>"
            "<p>This is a paragraph with <b>bold</b> and a <a href=\"https://example.com\">link</a>.</p>"
            "<ul><li>Item A</li><li>Item B</li></ul>"
            "<blockquote><p>A quote</p></blockquote>"
            "<pre><code>code()</code></pre>"
            "</div>"
        )
        self.assertEqual(node.to_html(), expected)


if __name__ == '__main__':
    unittest.main()
