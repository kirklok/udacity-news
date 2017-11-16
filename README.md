# udacity-news

The project has two files that answer questions from Log analysis project:
* newsdb.py
* news.py

newsdb.py
This file manages queries and provides data (controller)
In this file a view is being created, but you don't have to worry about - it is dropped and generated in the code of the file.

Here is a code for the view
query = 'CREATE VIEW views AS (\
       select right(path, char_length(path)-9) as slug, \
       count(*) as views from log \
       where path like \'%article%\' and \
       status = \'200 OK\' group by 1);'

news.py
This file represents results from queries in html (view). This file was used to generate news.htm and news.txt

To run the program

0) clone project and cd into /udacity-news
1) vagrant up
2) vagrant ssh
3) python news.py
4) visit 0.0.0.0:8000 to see html with the answer
