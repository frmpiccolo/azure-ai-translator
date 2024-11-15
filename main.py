import time
from modules.translator_module import extract_content_from_url, translate_text, translate_word_document

def translate_url_content(url):
    """Extracts and translates content from a URL."""
    print(f"Fetching content from: {url}")
    try:
        paragraphs = extract_content_from_url(url)
        if not paragraphs:
            print("No paragraphs found on the page.")
            return

        print(f"Extracted {len(paragraphs)} paragraphs from the URL.\n")
        print("Translating paragraphs...\n")

        for paragraph in paragraphs:
            translated_paragraph = translate_text(paragraph)
            if translated_paragraph:
                print(translated_paragraph)
                time.sleep(1)  # Pause to respect API rate limits

        print("\nURL translation complete.")
    except Exception as e:
        print(f"An error occurred while translating the URL content: {e}")

def translate_word_file(input_file, output_file):
    """Translates the content of a Word document."""
    print(f"Translating Word document: {input_file}")
    try:
        translate_word_document(input_file, output_file)
        print(f"Translation saved to: {output_file}")
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
    except Exception as e:
        print(f"An error occurred while translating the Word document: {e}")

if __name__ == "__main__":
    # Example usage with a URL
    example_url = "https://azure.microsoft.com/en-us/blog/introducing-o1-openais-new-reasoning-model-series-for-developers-and-enterprises-on-azure/"
    translate_url_content(example_url)

    print("\n---\n")

    # Example usage with a Word document
    input_docx = "resources/sample.docx"  # Ensure the file is in the 'resources' folder
    output_docx = "resources/sample_translated.docx"
    translate_word_file(input_docx, output_docx)
