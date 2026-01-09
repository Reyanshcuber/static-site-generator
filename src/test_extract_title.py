import unittest
from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        """Test extracting a simple h1 title"""
        markdown = "# Hello"
        self.assertEqual(extract_title(markdown), "Hello")
    
    def test_title_with_extra_whitespace(self):
        """Test extracting title with leading/trailing whitespace"""
        markdown = "#   Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")
    
    def test_title_with_content_below(self):
        """Test extracting title when there's content below it"""
        markdown = "# My Title\n\nSome content here"
        self.assertEqual(extract_title(markdown), "My Title")
    
    def test_title_with_multiple_lines(self):
        """Test extracting title from markdown with multiple sections"""
        markdown = """# Main Title

## Subtitle

Some content"""
        self.assertEqual(extract_title(markdown), "Main Title")
    
    def test_no_title_raises_exception(self):
        """Test that exception is raised when no h1 is found"""
        markdown = "## Only a subtitle\n\nSome content"
        with self.assertRaises(Exception) as context:
            extract_title(markdown)
        self.assertIn("No h1 header found", str(context.exception))
    
    def test_empty_markdown_raises_exception(self):
        """Test that exception is raised for empty markdown"""
        markdown = ""
        with self.assertRaises(Exception):
            extract_title(markdown)
    
    def test_title_with_special_characters(self):
        """Test extracting title with special characters"""
        markdown = "# My Awesome Title (2024) & Beyond!"
        self.assertEqual(extract_title(markdown), "My Awesome Title (2024) & Beyond!")


if __name__ == "__main__":
    unittest.main()
