import unittest
from BlockType import BlockType, block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a normal paragraph with some text."
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_paragraph_multiline(self):
        block = "This is a paragraph\nwith multiple lines\nof text"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_heading_h1(self):
        block = "# This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_h2(self):
        block = "## This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_h3(self):
        block = "### This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_h4(self):
        block = "#### This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_h5(self):
        block = "##### This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_heading_h6(self):
        block = "###### This is a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.HEADING)

    def test_not_heading_seven_hashes(self):
        block = "####### This is not a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_heading_no_space(self):
        block = "#This is not a heading"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_code_block(self):
        block = "```\nprint('hello')\nprint('world')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_code_block_single_line(self):
        block = "```\ncode\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.CODE)

    def test_not_code_block_missing_end(self):
        block = "```\nprint('hello')\nprint('world')"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_code_block_missing_start(self):
        block = "print('hello')\nprint('world')\n```"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_quote_single_line(self):
        block = "> This is a quote"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_quote_multiline(self):
        block = "> This is a quote\n> with multiple lines\n> of text"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.QUOTE)

    def test_not_quote_missing_greater_than(self):
        block = "> This is a quote\nwithout greater than\n> symbol"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_quote_no_space_after_greater_than(self):
        block = ">This is not a quote\n>without space\n>after >"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_unordered_list_single_line(self):
        block = "- Item 1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_unordered_list_multiline(self):
        block = "- Item 1\n- Item 2\n- Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.UNORDERED_LIST)

    def test_not_unordered_list_missing_dash(self):
        block = "- Item 1\nItem 2\n- Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_unordered_list_no_space_after_dash(self):
        block = "-Item 1\n-Item 2\n-Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_ordered_list_single_line(self):
        block = "1. Item 1"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ordered_list_multiline(self):
        block = "1. Item 1\n2. Item 2\n3. Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_ordered_list_longer(self):
        block = "1. First\n2. Second\n3. Third\n4. Fourth\n5. Fifth"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.ORDERED_LIST)

    def test_not_ordered_list_wrong_start_number(self):
        block = "2. Item 1\n3. Item 2\n4. Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_ordered_list_wrong_increment(self):
        block = "1. Item 1\n3. Item 2\n5. Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_ordered_list_no_space_after_dot(self):
        block = "1.Item 1\n2.Item 2\n3.Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)

    def test_not_ordered_list_missing_dot(self):
        block = "1 Item 1\n2 Item 2\n3 Item 3"
        result = block_to_block_type(block)
        self.assertEqual(result, BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
