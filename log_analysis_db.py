#!/usr/bin/env python

import psycopg2

DBNAME = "news"


def reporting():
    db = psycopg2.connect(database=DBNAME)
    cur = db.cursor()

    # 1. Popular articles
    cur.execute(("select count(*) as num, articles.title from log "
                 "join articles on log.path like '%' || articles.slug || '%' "
                 "where log.status = '200 OK' and log.path like '/%/%' "
                 "group by articles.title order by num desc limit 3"))
    popular_articles = cur.fetchall()

    print "Popular Articles:"
    for item in popular_articles:
        print '"' + item[1] + '" - ' + str(item[0]) + ' views'

    # 2. Popular authors
    print ""
    cur.execute(("select count(*) as num, authors.name from log "
                 "join articles on log.path like '%' || articles.slug || '%' "
                 "join authors on articles.author = authors.id "
                 "where log.status = '200 OK' and log.path like '/%/%' "
                 "group by  authors.name order by num desc"))
    popular_authors = cur.fetchall()

    # 3. Days with error more than 1%
    print "Popular Authors:"
    for author in popular_authors:
        print author[1] + " - " + str(author[0]) + " views"

    print ""
    cur.execute(("select cast(log.time as date), (count(*) "
                 "filter "
                 "(where log.status = '404 NOT FOUND') * 100.0 / count(*)) "
                 "as error "
                 "from log group by cast(log.time as date) "
                 "having (count(*) filter "
                 "(where log.status = '404 NOT FOUND') * 100.0 / count(*)) > 1"))
    buggy_days = cur.fetchall()

    if len(buggy_days) == 1:
        print "Day on which more than 1% of requests lead to errors:"
    else:
        print "Days on which more than 1% of requests lead to errors"
    for item in buggy_days:
        print item[0].strftime("%b, %d %Y -")+" "+str(round(item[1], 2))+"% errors"

    db.close()

if __name__ == "__main__":
    reporting()
