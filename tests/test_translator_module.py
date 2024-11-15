import unittest
from modules.translator_module import extract_content_from_url, translate_text, translate_word_document

class TestTranslatorModule(unittest.TestCase):

    def test_extract_content_from_url(self):
        try:
            url = "https://example.com"
            paragraphs = extract_content_from_url(url)
            self.assertIsInstance(paragraphs, list)
        except Exception:
            self.fail("test_extract_content_from_url raised an exception unexpectedly!")

    def test_translate_text(self):
        try:
            text = "Hello, world!"
            translated_text = translate_text(text, target_language="es")
            self.assertIsInstance(translated_text, str)
            self.assertNotEqual(translated_text, "")
        except Exception:
            self.fail("test_translate_text raised an exception unexpectedly!")

    def test_translate_word_document(self):
        input_file = "resources/sample.docx"
        output_file = "resources/sample_translated.docx"
        try:
            translate_word_document(input_file, output_file)
            self.assertTrue(True)  # Se não houver exceção, o teste passa
        except Exception:
            self.fail("translate_word_document raised an exception unexpectedly!")

if __name__ == "__main__":
    unittest.main()
