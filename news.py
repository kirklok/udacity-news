#!/usr/bin/env python3
#

from flask import Flask, request, redirect, url_for
from newsdb import get_popular_articles, get_popular_authors, get_error_days

app = Flask(__name__)

# HTML template for the news page
HTML_WRAP = '''\
<!DOCTYPE html>
<html>
  <head>
    <title>DB News</title>
  </head>
  <body>
    <h1>Logs analysis project</h1>
    <h2>1. What are the most popular three articles of all time?</h2>
    <!-- content will go here -->
    {0}
    <h2>2. Who are the most popular article authors of all time?</h2>
    <!-- content will go here -->
    {1}
    <h2>3. On which days did more than 1% of requests lead to errors?</h2>
    <!-- content will go here -->
    {2}
  </body>
</html>
'''

# HTML template for an individual comment
ANSWER = '''\
<ul>
    <li>%s</li>
</ul>
'''


@app.route('/', methods=['GET'])
def main():
    # '''Main page of the news.'''
    popular_articles = "".join(ANSWER % '\"{}\" - {} views'
                               .format(title, views)
                               for title, views in get_popular_articles())
    popular_authors = "".join(ANSWER % '\"{}\" - {} views'
                              .format(name, views)
                              for name, views in get_popular_authors())
    error_days = "".join(ANSWER % '\"{}\" - {}% errors'
                         .format(date, errors)
                         for date, errors in get_error_days())
    html = HTML_WRAP.format(popular_articles, popular_authors, error_days)
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
