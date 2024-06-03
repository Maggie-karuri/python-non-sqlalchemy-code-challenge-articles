# Phase 3 Code Challenge: Articles - without SQLAlchemy (Updated)

In this project, I worked on a Magazine domain where we have three models: `Author`, `Article`, and `Magazine`.

For our purposes, an `Author` has many `Article`s, a `Magazine` has many `Article`s, and `Article`s belong to both `Author` and `Magazine`.

`Author` - `Magazine` is a many-to-many relationship.

## Setup

To get started, ensure you have `pipenv` installed. Then, run the following commands:

```bash
pipenv install
pipenv shell
# Core Deliverables

## Author

### `Author.__init__(self, name)`
Initializes an Author with a name.

### `Author.name`
Returns the author's name (immutable).

### `Author.articles()`
Returns a list of all articles written by the author.

### `Author.magazines()`
Returns a unique list of magazines the author has contributed to.

### `Author.add_article(magazine, title)`
Creates and returns a new Article instance associated with the author and the magazine.

### `Author.topic_areas()`
Returns a unique list of categories of magazines the author has contributed to, or `None` if the author has no articles.

## Magazine

### `Magazine.__init__(self, name, category)`
Initializes a Magazine with a name and category.

### `Magazine.name`
Returns and allows changing the magazine's name.

### `Magazine.category`
Returns and allows changing the magazine's category.

### `Magazine.articles()`
Returns a list of all articles the magazine has published.

### `Magazine.contributors()`
Returns a unique list of authors who have written for the magazine.

### `Magazine.article_titles()`
Returns a list of titles of all articles written for the magazine, or `None` if the magazine has no articles.

### `Magazine.contributing_authors()`
Returns a list of authors who have written more than 2 articles for the magazine, or `None` if there are no such authors.

## Article

### `Article.__init__(self, author, magazine, title)`
Initializes an Article with an Author instance, a Magazine instance, and a title.

### `Article.title`
Returns the article's title (immutable).

### `Article.author`
Returns the author object for the article (can be changed).

### `Article.magazine`
Returns the magazine object for the article (can be changed).

# Advanced Deliverables

## Bonus: Aggregate and Association Method

### `Magazine.top_publisher()`
Returns the Magazine instance with the most articles, or `None` if there are no articles.

