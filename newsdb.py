import datetime
import psycopg2

DBNAME = 'news'

db = psycopg2.connect(database=DBNAME)
c = db.cursor()
c.execute('drop view  if exists views;')
query = 'CREATE VIEW views AS (\
       select right(path, char_length(path)-9) as slug, \
       count(*) as views from log \
       where path like \'%article%\' and \
       status = \'200 OK\' group by 1);'
c.execute(query)
c.execute('select * from views')
result = c.fetchall()
db.commit()
db.close()


def get_popular_articles():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = 'select a.title, v.views from views v \
             join articles a on \
             a.slug = v.slug order by v.views desc;'
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def get_popular_authors():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = 'select au.name, v.views from views v \
             join articles a on a.slug = v.slug \
             join authors au on au.id = a.author \
             order by v.views desc;'
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def get_error_days():
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query = 'select date_trunc(\'day\',time) :: DATE as date, \
             round(sum(case when status <> \'200 OK\' \
             then 1 else 0 end)*100.0 / count(*),1) as error_perc \
             from log \
             group by 1 \
             having (sum(case when status <> \'200 OK\' \
             then 1 else 0 end)*100.0 / count(*) > 1);'
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result
