class Author:
    def __init__(self, name):
        # Initialize the Author with a name, raising errors for invalid input.
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        # author's name
        return self._name

    def articles(self):
        # articles written by the author.
        return self._articles

    def magazines(self):
        # unique magazines
        return list({article.magazine for article in self._articles})

    def add_article(self, magazine, title):
        # Add a new article to the author's list of existing articles
        existing_articles = [article for article in self._articles if article.title == title]
        if existing_articles:
            return existing_articles[0]
        else:
            article = Article(self, magazine, title)
            return article


    def topic_areas(self):
        # List of unique topic areas
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    # Class variable for all magazine instances
    all_magazines = []

    def __init__(self, name, category):
         # Initialize the Magazine with a name and category
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        if not isinstance(category, str):
            raise TypeError("Category must be of type str")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # set magazine name
        if not isinstance(value, str):
            raise TypeError("Name must be of type str")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters")
        self._name = value

    @property
    def category(self):
        # Return the category of magazine.
        return self._category

    @category.setter
    def category(self, value):
        # set magazine category
        if not isinstance(value, str):
            raise TypeError("Category must be of type str")
        if len(value) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = value

    def articles(self):
        # list of articles for the magazine.
        return self._articles

    def contributors(self):
        # list of titles of articles published in the magazine.
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            #  list of titles of articles published in the magazine, or None if no articles.
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # list authors with mote than 2 articles
        from collections import Counter
        author_counts = Counter(article.author for article in self._articles)
        result = [author for author, count in author_counts.items() if count > 2]
        return result if result else None

    def add_article(self, article):
         # Add article to the magazine's list of articles.
        self._articles.append(article)

    @classmethod
    def top_publisher(cls):
        # magazine with most articles
        if not cls.all_magazines:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles()))


class Article:
     # Class variable
    all = []
    def __init__(self, author, magazine, title):
         # Initialize the Article with an author, magazine, and title.
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not 5 <= len(title) <= 50:
            raise ValueError("Title must be between 5 and 50 characters")
        self._title = title
        self.author = author
        self.magazine = magazine
        self.__class__.all.append(self)
        magazine.add_article(self)
        author._articles.append(self)

    @property
    def title(self):
        # Return the author
        return self._title

    @title.setter
    def title(self, value):
        # Title change error since it's immutable
        raise AttributeError("Title attribute is immutable and cannot be changed")

    @property
    def author(self):
        # Return the author of the article.
        return self._author

    @author.setter
    def author(self, value):
         # Set the author of the article
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        # Return the magazine of the article
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        # Set the magazine of the article
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine")
        self._magazine = value