import unittest
from textnode import TextNode, TextType
from split_nodes_images_and_links import split_nodes_image, split_nodes_link


class TestSplitNodesImage(unittest.TestCase):
    def test_single_image(self):
        node = TextNode(
            "This is text with an ![image](https://example.com/image.png) in it",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("This is text with an ", TextType.PLAIN),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" in it", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_images(self):
        node = TextNode(
            "![alt1](url1) and ![alt2](url2)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("alt1", TextType.IMAGE, "url1"),
            TextNode(" and ", TextType.PLAIN),
            TextNode("alt2", TextType.IMAGE, "url2"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_image_at_start(self):
        node = TextNode(
            "![alt](url) some text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("alt", TextType.IMAGE, "url"),
            TextNode(" some text", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)

    def test_image_at_end(self):
        node = TextNode(
            "some text ![alt](url)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        expected = [
            TextNode("some text ", TextType.PLAIN),
            TextNode("alt", TextType.IMAGE, "url"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_images(self):
        node = TextNode(
            "This is just plain text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_image([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_non_plain_node_unchanged(self):
        node = TextNode(
            "This is bold text with ![alt](url)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_image([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("Text with ![alt1](url1)", TextType.PLAIN),
            TextNode("Bold text", TextType.BOLD),
            TextNode("![alt2](url2) and more", TextType.PLAIN),
        ]
        new_nodes = split_nodes_image(nodes)
        expected = [
            TextNode("Text with ", TextType.PLAIN),
            TextNode("alt1", TextType.IMAGE, "url1"),
            TextNode("Bold text", TextType.BOLD),
            TextNode("alt2", TextType.IMAGE, "url2"),
            TextNode(" and more", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)


class TestSplitNodesLink(unittest.TestCase):
    def test_single_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("This is text with a link ", TextType.PLAIN),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.PLAIN),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
            ),
        ]
        self.assertEqual(new_nodes, expected)

    def test_single_link_only(self):
        node = TextNode(
            "Check out [this link](https://example.com)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("Check out ", TextType.PLAIN),
            TextNode("this link", TextType.LINK, "https://example.com"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_link_at_start(self):
        node = TextNode(
            "[link](url) some text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("link", TextType.LINK, "url"),
            TextNode(" some text", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)

    def test_link_at_end(self):
        node = TextNode(
            "some text [link](url)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("some text ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertEqual(new_nodes, expected)

    def test_no_links(self):
        node = TextNode(
            "This is just plain text",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_non_plain_node_unchanged(self):
        node = TextNode(
            "This is bold text with [link](url)",
            TextType.BOLD,
        )
        new_nodes = split_nodes_link([node])
        expected = [node]
        self.assertEqual(new_nodes, expected)

    def test_multiple_nodes(self):
        nodes = [
            TextNode("Text with [link1](url1)", TextType.PLAIN),
            TextNode("Bold text", TextType.BOLD),
            TextNode("[link2](url2) and more", TextType.PLAIN),
        ]
        new_nodes = split_nodes_link(nodes)
        expected = [
            TextNode("Text with ", TextType.PLAIN),
            TextNode("link1", TextType.LINK, "url1"),
            TextNode("Bold text", TextType.BOLD),
            TextNode("link2", TextType.LINK, "url2"),
            TextNode(" and more", TextType.PLAIN),
        ]
        self.assertEqual(new_nodes, expected)

    def test_multiple_links_in_sequence(self):
        node = TextNode(
            "[link1](url1) [link2](url2) [link3](url3)",
            TextType.PLAIN,
        )
        new_nodes = split_nodes_link([node])
        expected = [
            TextNode("link1", TextType.LINK, "url1"),
            TextNode(" ", TextType.PLAIN),
            TextNode("link2", TextType.LINK, "url2"),
            TextNode(" ", TextType.PLAIN),
            TextNode("link3", TextType.LINK, "url3"),
        ]
        self.assertEqual(new_nodes, expected)


if __name__ == "__main__":
    unittest.main()
