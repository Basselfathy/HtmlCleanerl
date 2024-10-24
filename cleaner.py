import logging
from lxml import html
from rich.logging import RichHandler

# Set up logging with Rich
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)

logger = logging.getLogger("html_cleaner")


def keep_first_word(text):
    """
    Keep only the first word of a given text.
    
    Args:
    - text (str): The original text content.
    
    Returns:
    - str: The first word of the text, or an empty string if no text exists.
    """
    if text:
        words = text.split()
        if words:
            return words[0]  # Keep only the first word
    return ''  # Return empty string if text is empty or None


def clear_text_nodes(element):
    """
    Recursively modify text and tail nodes to keep only the first word from the given HTML element.
    
    Args:
    - element (lxml.html.HtmlElement): The HTML element to process.
    """
    # Modify the text content within the element (keeping only the first word)
    if element.text:
        element.text = keep_first_word(element.text)
    
    # Modify the trailing text after the element (keeping only the first word)
    if element.tail:
        element.tail = keep_first_word(element.tail)
    
    # Recursively process all child elements
    for child in element:
        clear_text_nodes(child)


def remove_inner_text_from_html(html_content):
    """
    Keeps only the first word of all inner text in an HTML document.
    
    Args:
    - html_content (str): The raw HTML content as a string.
    
    Returns:
    - str: The cleaned HTML content with only the first word kept in text nodes.
    """
    try:
        logger.info("Parsing the HTML content...")
        # Parse the HTML content
        tree = html.fromstring(html_content)

        logger.debug("Modifying all text nodes to keep only the first word...")
        # Modify text nodes to keep only the first word
        clear_text_nodes(tree)

        # Serialize the cleaned tree back to HTML
        cleaned_html = html.tostring(tree, pretty_print=True, method='html').decode('utf-8')
        
        logger.debug("HTML cleaned successfully, keeping only the first word of each text node.")
        return cleaned_html
    
    except Exception as e:
        logger.error(f"Error cleaning HTML: {e}")
        return None
