import unittest
from markdown_to_blocks import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_single_block(self):
        markdown = "This is a single block"
        result = markdown_to_blocks(markdown)
        expected = ["This is a single block"]
        self.assertEqual(result, expected)

    def test_two_blocks(self):
        markdown = "Block one\n\nBlock two"
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two"]
        self.assertEqual(result, expected)

    def test_three_blocks(self):
        markdown = "Block one\n\nBlock two\n\nBlock three"
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two", "Block three"]
        self.assertEqual(result, expected)

    def test_blocks_with_leading_trailing_whitespace(self):
        markdown = "  Block one  \n\n  Block two  \n\n  Block three  "
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two", "Block three"]
        self.assertEqual(result, expected)

    def test_multiple_newlines_between_blocks(self):
        markdown = "Block one\n\n\n\nBlock two\n\n\n\nBlock three"
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two", "Block three"]
        self.assertEqual(result, expected)

    def test_empty_blocks_removed(self):
        markdown = "Block one\n\n\n\nBlock two"
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two"]
        self.assertEqual(result, expected)

    def test_assignment_example(self):
        markdown = """# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item"""
        result = markdown_to_blocks(markdown)
        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]
        self.assertEqual(result, expected)

    def test_blocks_with_internal_newlines(self):
        markdown = "Line 1\nLine 2\n\nLine 3\nLine 4"
        result = markdown_to_blocks(markdown)
        expected = [
            "Line 1\nLine 2",
            "Line 3\nLine 4"
        ]
        self.assertEqual(result, expected)

    def test_whitespace_only_blocks_removed(self):
        markdown = "Block one\n\n   \n\nBlock two"
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two"]
        self.assertEqual(result, expected)

    def test_empty_string(self):
        markdown = ""
        result = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(result, expected)

    def test_whitespace_only_string(self):
        markdown = "   \n\n   \n\n   "
        result = markdown_to_blocks(markdown)
        expected = []
        self.assertEqual(result, expected)

    def test_block_with_leading_newlines(self):
        markdown = "\n\n\nBlock one\n\n\nBlock two"
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two"]
        self.assertEqual(result, expected)

    def test_block_with_trailing_newlines(self):
        markdown = "Block one\n\n\nBlock two\n\n\n"
        result = markdown_to_blocks(markdown)
        expected = ["Block one", "Block two"]
        self.assertEqual(result, expected)

    def test_multiline_list_block(self):
        markdown = "Some text\n\n- Item 1\n- Item 2\n- Item 3\n\nMore text"
        result = markdown_to_blocks(markdown)
        expected = [
            "Some text",
            "- Item 1\n- Item 2\n- Item 3",
            "More text"
        ]
        self.assertEqual(result, expected)

    def test_multiline_code_block(self):
        markdown = "Some text\n\n```\ncode line 1\ncode line 2\n```\n\nMore text"
        result = markdown_to_blocks(markdown)
        expected = [
            "Some text",
            "```\ncode line 1\ncode line 2\n```",
            "More text"
        ]
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
