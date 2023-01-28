from blogapp.documents import ArticleDocument

def test_function():
    s = ArticleDocument.search().filter()
    for hit in s:
        print(hit.author)
        print(hit.title)
        print(hit.content)