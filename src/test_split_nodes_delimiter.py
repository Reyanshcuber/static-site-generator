import unittest

from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_basic_split(self):
        nodes = [TextNode("This is **bold** and normal", TextType.PLAIN)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" and normal", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_non_plain_untouched(self):
        nodes = [TextNode("Already italic", TextType.ITALIC)]
        result = split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertEqual(result, nodes)

    def test_unclosed_delimiter_raises(self):
        nodes = [TextNode("An **unclosed bold", TextType.PLAIN)]
        with self.assertRaises(Exception) as cm:
            split_nodes_delimiter(nodes, "**", TextType.BOLD)
        self.assertIn("unclosed delimiter", str(cm.exception))


if __name__ == "__main__":
    unittest.main()
