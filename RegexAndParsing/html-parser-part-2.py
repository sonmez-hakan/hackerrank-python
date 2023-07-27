from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        print(data)

    def handle_data(self, data):
        if data.rstrip():
            print(">>> Data")
            print(data.rstrip())


MyHTMLParser().feed('\n'.join([input().rstrip() for _ in range(int(input()))]))
