from extract_markdown_images_and_links import extract_markdown_images, extract_markdown_links
import unittest
class TestExtractMarkdownImagesAndLinks(unittest.TestCase):
    def test_extract_markdown_images(self):
        text="Here is an image: ![Alt text](http://example.com/image.png) and another one ![Another image](http://example.com/another_image.jpg)"
        expected=[("Alt text","http://example.com/image.png"),("Another image","http://example.com/another_image.jpg")]
        result=extract_markdown_images(text)
        self.assertEqual(result,expected)
    def test_extract_markdown_links(self):
        text="Here is a link: [Example](http://example.com) and another one [Another Example](http://example.org)"
        expected=[("Example","http://example.com"),("Another Example","http://example.org")]
        result=extract_markdown_links(text)
        self.assertEqual(result,expected)
    def test_no_images(self):
        text="This text has no images."
        expected=[]
        result=extract_markdown_images(text)
        self.assertEqual(result,expected)
    def test_no_links(self):
        text="This text has no links."
        expected=[]
        result=extract_markdown_links(text)
        self.assertEqual(result,expected)
    def test_mixed_content(self):
        text="![Image](http://example.com/image.png) and [Link](http://example.com)"
        expected_images=[("Image","http://example.com/image.png")]
        expected_links=[("Link","http://example.com")]
        result_images=extract_markdown_images(text)
        result_links=extract_markdown_links(text)
        self.assertEqual(result_images,expected_images)
        self.assertEqual(result_links,expected_links)
if __name__=="__main__":
    unittest.main()