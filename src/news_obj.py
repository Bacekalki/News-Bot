class NewsObj:
    def __init__(
        self, title : str, source: str, description : str, url : str, category : str
        ) -> None:
        self.title = title
        self.source = source
        self.description = description
        self.url = url
        self.category = category

    def __repr__(self):
        return f"News_obj(source={self.source!r}, title={self.title!r}, url={self.url!r})"

    def __str__(self):
        return f"Title: {self.title}\nURL: {self.url}\n"
