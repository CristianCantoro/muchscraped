    #!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import sys
import itertools
import requests
import time
import lxml

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

import bs4
from bs4 import BeautifulSoup

import sqlite3 as sqlite


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return itertools.izip(a, b)


def get_page(base_url):
    delay = 3

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)

    verificationErrors = []
    accept_next_alert = True

    driver.get(base_url)
    for i in range(1, 10):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(delay)
    html_source = driver.page_source
    data = html_source.encode('utf-8')
    return data


def create_db():
    con = None
    con = sqlite.connect('verybello.sqlite')
    cur = con.cursor()

    try:
        command = 'DROP TABLE IF EXISTS verybello'
        cur.execute(command)

        command = '''CREATE TABLE verybello(
                            id TEXT PRIMARY KEY,
                            titolo TEXT,
                            data TEXT,
                            categoria TEXT,
                            citta TEXT,
                            regione TEXT,
                            descrizione TEXT,
                            sito TEXT,
                            sede TEXT,
                            indirizzo TEXT,
                            thumb TEXT,
                            caption TEXT
                            )
                    '''
        cur.execute(command)
    except sqlite.Error as e:

        print "Error %s:" % e.args[0]
        sys.exit(1)

    finally:
        if con:
            con.close()


def quote_identifier(s, errors="strict"):
    encodable = s.encode("utf-8", errors).decode("utf-8")

    nul_index = encodable.find("\x00")

    if nul_index >= 0:
        error = UnicodeEncodeError("utf-8",
                                   encodable,
                                   nul_index,
                                   nul_index + 1,
                                   "NUL not allowed"
                                   )
        error_handler = codecs.lookup_error(errors)
        replacement, _ = error_handler(error)
        encodable = encodable.replace("\x00", replacement)

    return "\"" + encodable.replace("\"", "\"\"") + "\""


def save(data):
    con = None
    con = sqlite.connect('verybello.sqlite')
    cur = con.cursor()

    for k, v in data.iteritems():
        if v:
            data[k] = quote_identifier(v)
        else:
            data[k] = 'NULL'

    try:
        command = u'''INSERT INTO verybello VALUES(
                            {id},
                            {titolo},
                            {data},
                            {categoria},
                            {citta},
                            {regione},
                            {descrizione},
                            {sito},
                            {sede},
                            {indirizzo},
                            {thumb},
                            {caption}
                            )
                    '''.format(**data)
        cur.execute(command)
        con.commit()

    except sqlite.Error as e:
        print "Error %s:" % e.args[0]
        import pdb
        pdb.set_trace()
        sys.exit(1)

    finally:
        if con:
            con.close()


if __name__ == '__main__':
    create_db()

    base_url = "https://www.verybello.it"

    # req = requests.get(base_url)
    # html = req.content
    html = get_page(base_url)

    tree = BeautifulSoup(html)
    doc = tree.find(attrs={'id': 'eventi-list'})
    events = [child
              for child in doc.childGenerator()
              if isinstance(child, bs4.element.Tag)
              ]

    for start, stop in pairwise(range(0, len(events), 4)):
        event = events[start:stop]
        event_id = event[0].get('id')
        event_tree = BeautifulSoup('\n'.join([unicode(e) for e in event]))

        titolo = event_tree.find(attrs={'class': 'evento-titolo'}).text
        data = event_tree.find(attrs={'class': 'evento-data'}).text
        sede = event_tree.find(attrs={'class': 'evento-sede'}).text
        citta = event_tree.find(attrs={'class': 'evento-citta'}).text
        regione = event_tree.find(attrs={'class': 'evento-regione'}).text
        descrizione = event_tree.find(
            attrs={'class': 'evento-descrizione'}).text.strip()
        sito = event_tree.find(attrs={'class': 'evento-sito'}).attrs['href']

        event_map = event_tree.find(attrs={'class': 'map'}).attrs
        sede = event_map['data-sede']
        indirizzo = event_map['data-indirizzo']

        try:
            mixxiethumb = event_tree.find(
                attrs={'class': 'evento-mixxiethumb'})
            thumb = mixxiethumb.attrs['style']\
                .replace('background-image:url(', '')\
                .replace(')', '')
        except:
            thumb = ''

        try:
            caption = event_tree.find(
                attrs={'class': 'evento-mixxietitolo'}).text
        except:
            caption = ''

        categoria = [c
                     for c in event_tree.
                     find(attrs={'class': 'evento-categoria'}).
                     children][0].attrs['class']

        print 'EVENTO'
        print 'titolo: ', titolo
        print 'data: ', data
        print 'categoria: ', categoria
        print 'sede: ', sede
        print 'citta: ', citta
        print 'regione: ', regione
        print 'descrizione: ', descrizione
        print 'sito: ', sito
        print 'sede: ', sede
        print 'indirizzo: ', indirizzo
        print 'thumb: ', thumb
        print 'caption: ', caption
        print '---\n'

        # Saving data:
        data = {'id': event_id,
                'titolo': titolo,
                'data': data,
                'categoria': ','.join(categoria),
                'citta': citta,
                'regione': regione,
                'descrizione': descrizione,
                'sito': sito,
                'sede': sede,
                'indirizzo': indirizzo,
                'thumb': thumb,
                'caption': caption
                }
        save(data)
