from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.write_attrs(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.write_attrs(attrs)

    @staticmethod
    def write_attrs(attrs):
        [print(f'-> {key} > {val}') for key, val in attrs]


MyHTMLParser().feed(''.join([input() for _ in range(int(input()))]))
