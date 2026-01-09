import unittest
from textnode import TextNode, TextType
from text_to_textnodes import text_to_textnodes


class TestTextToTextnodes(unittest.TestCase):
    def test_plain_text(self):
        text = "This is plain text"
        result = text_to_textnodes(text)
        expected = [TextNode("This is plain text", TextType.PLAIN)]
        self.assertEqual(result, expected)

    def test_bold_text(self):
        text = "This is **bold** text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_italic_text(self):
        text = "This is _italic_ text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_code_text(self):
        text = "This is `code` text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_image(self):
        text = "This is an ![alt text](https://example.com/image.png) image"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is an ", TextType.PLAIN),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" image", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_link(self):
        text = "This is a [link](https://example.com) here"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://example.com"),
            TextNode(" here", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_complex_text_from_assignment(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("This is ", TextType.PLAIN),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.PLAIN),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.PLAIN),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_bold(self):
        text = "**bold** and **more bold**"
        result = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("more bold", TextType.BOLD),
        ]
        self.assertEqual(result, expected)

    def test_multiple_italic(self):
        text = "_italic_ and _more italic_"
        result = text_to_textnodes(text)
        expected = [
            TextNode("italic", TextType.ITALIC),
            TextNode(" and ", TextType.PLAIN),
            TextNode("more italic", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)

    def test_multiple_code(self):
        text = "`code1` and `code2`"
        result = text_to_textnodes(text)
        expected = [
            TextNode("code1", TextType.CODE),
            TextNode(" and ", TextType.PLAIN),
            TextNode("code2", TextType.CODE),
        ]
        self.assertEqual(result, expected)

    def test_multiple_images(self):
        text = "![img1](url1) and ![img2](url2)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("img1", TextType.IMAGE, "url1"),
            TextNode(" and ", TextType.PLAIN),
            TextNode("img2", TextType.IMAGE, "url2"),
        ]
        self.assertEqual(result, expected)

    def test_multiple_links(self):
        text = "[link1](url1) and [link2](url2)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("link1", TextType.LINK, "url1"),
            TextNode(" and ", TextType.PLAIN),
            TextNode("link2", TextType.LINK, "url2"),
        ]
        self.assertEqual(result, expected)

    def test_bold_and_italic(self):
        text = "**bold** and _italic_"
        result = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" and ", TextType.PLAIN),
            TextNode("italic", TextType.ITALIC),
        ]
        self.assertEqual(result, expected)

    def test_bold_and_code_and_link(self):
        text = "**bold** `code` [link](url)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" ", TextType.PLAIN),
            TextNode("code", TextType.CODE),
            TextNode(" ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertEqual(result, expected)

    def test_text_starting_with_bold(self):
        text = "**bold** text"
        result = text_to_textnodes(text)
        expected = [
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.PLAIN),
        ]
        self.assertEqual(result, expected)

    def test_text_ending_with_link(self):
        text = "text [link](url)"
        result = text_to_textnodes(text)
        expected = [
            TextNode("text ", TextType.PLAIN),
            TextNode("link", TextType.LINK, "url"),
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
