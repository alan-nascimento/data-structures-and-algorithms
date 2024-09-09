class Page:
    def __init__(self, page: str, prev = None):
        self.page = page
        self.prev = prev
        self.next = None

class BrowserHistory:
    def __init__(self, homepage: str):
        page = Page(homepage)
        self.current = page

    def visit(self, url: str) -> None:
        page = Page(url, self.current)
        self.current.next = page
        self.current = page

    def back(self, steps: int) -> str:
        while steps is not 0:
            if self.current.prev:
                self.current = self.current.prev
            steps -= 1
        return self.current.page

    def forward(self, steps: int) -> str:
        while steps is not 0:
            if self.current.next:
                self.current = self.current.next
            steps -= 1
        return self.current.page

# Time Complexity: O(N) for back and forward
# Space Complexity: O(N) for storing the history
