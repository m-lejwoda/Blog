from blogapp.documents import ArticleDocument

def get_article_function():
    s = ArticleDocument.search().filter(fields=['title'])
    for hit in s:
        print(hit.author)
        print(hit.title)
        print(hit.content)