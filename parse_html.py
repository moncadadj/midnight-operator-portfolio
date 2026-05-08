from html.parser import HTMLParser
import json

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.capture = False
        self.current_tag = ''

    def handle_starttag(self, tag, attrs):
        if tag in ['script', 'style', 'head', 'meta', 'link']:
            self.capture = False
        else:
            self.capture = True
            self.current_tag = tag

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        text = data.strip()
        if self.capture and text and len(text) > 1 and not text.isnumeric() and text != '→':
            self.texts.append(text)

with open('index.html', 'r') as f:
    html = f.read()

extractor = TextExtractor()
extractor.feed(html)

with open('extracted_texts.json', 'w') as f:
    json.dump(extractor.texts, f, indent=2, ensure_ascii=False)
