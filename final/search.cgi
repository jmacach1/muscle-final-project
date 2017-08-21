#!/usr/local/bin/python3

import cgi, json
import os
import mysql.connector

def main():
    print("Content-Type: application/json\n\n")
    form = cgi.FieldStorage()
    term = form.getvalue('search_term')
        
    conn = mysql.connector.connect(user='jmacach1', password='Milkshake11', host='localhost', database='jmacach1')
    cursor = conn.cursor()
    
    qry = "SELECT Title, Sequence FROM faaSeq WHERE Title LIKE %s"

    cursor.execute(qry, ('%' + term + '%', ))

    results = { 'match_count': 0, 'matches': list() }
    for (Title, Sequence) in cursor:
        results['matches'].append({'Title': Title, 'Sequence': Sequence})
        results['match_count'] += 1

    conn.close()

    print(json.dumps(results))


if __name__ == '__main__':
    main()