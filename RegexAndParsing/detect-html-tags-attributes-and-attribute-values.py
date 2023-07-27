from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print(f'-> {key} > {val}') for key, val in attrs]


MyHTMLParser().feed(''.join([input() for _ in range(int(input()))]))
