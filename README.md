muchscraped
-----------

> «verybello, such website, so expo, much scraped, wow»

![«verybello, such website, so expo, much scraped, wow»](muchscraped.jpeg)

Se siete italiani e girate per _l'interweb_ dovreste aver sentito parlare in
questi giorni (fine gennaio 2015) di [verybello.it](https://www.verybello.it).
In caso contrario ecco un po' di contesto:
* ["Franceschini, #verybello lascia #senzawords ma con tante domande"](http://www.ilfattoquotidiano.it/2015/01/25/franceschini-verybello-lascia-senzawords-tante-domande/1368756/) di Guido Scorza su "Il fatto quotidiano";
* ["Ci vorrebbe il napalm"](http://www.mantellini.it/2015/01/24/ci-vorrebbe-il-napalm/)
di Massimo Mantellini;
* ["#VeryBello: le mie considerazioni tecniche"](http://mgpf.it/2015/01/25/verybello-le-mie-considerazioni-tecniche.html)
di Matteo Flora;
* ["VeryBello!, come trasformare una disfatta in una opportunità"](http://digitalchampions.it/archives/verybello-come-trasformare-una-disfatta-una-opportunita/)
di Riccardo Luna.

Fatte queste premesse, il primo passo per rendere migliore #verybello è rendere
disponibili i dati, che è esattamente lo scopo di questo script python.

I dati sono salvati nel database SQLite:
[`verybello.sqlite`](https://github.com/CristianCantoro/muchscraped/blob/master/verybello.sqlite).

## Installazione

Per installare tutti i moduli di Python necessari:
```
pip install -r requirements.txt
```

## Licenza del software

Il codice  di questo progetto è rilasciato con una licenza MIT.


## Licenza dei dati

I dati di [verybello.it](https://verybello.it) sono per la maggior parte
pubblicati come [open data dal MiBACT](http://www.beniculturali.it/mibac/export/MiBAC/sito-MiBAC/MenuPrincipale/Trasparenza/Open-Data/Sviluppatori/index.html)
I dati sono anche accessibili via REST API in formato XML provvisto di
XMLSchema.

Questi dati sono distribuiti con una licenza CC-BY.

Inoltre, mancando una informazione di note legali sul sito in questione, essendo
questo di una PA, l'accesso ai dati ricade sotto l'articolo 52 comma 2 del
codice dell'amministrazione digitale

> «2. I dati e i documenti che le amministrazioni titolari pubblicano, con
> qualsiasi modalità, senza l'espressa adozione di una licenza di cui
> all'articolo 2, comma 1, lettera h), del decreto legislativo 24 gennaio 2006,
> n. 36, si intendono rilasciati come dati di tipo aperto ai sensi all'articolo
> 68, comma 3, del presente Codice. L'eventuale adozione di una licenza di cui
> al citato articolo 2, comma 1, lettera h), è motivata ai sensi delle linee
> guida nazionali di cui al comma 7.»

che nella versione delle linee guida AgID per la valorizzazione del patrimonio
informativo pubblico di giugno 2014 viene definita come licenza di default la
CC-BY 4.0, si veda
[pag. 84 di questo documento](http://www.agid.gov.it/sites/default/files/linee_guida/patrimoniopubblicolg2014_v0.7finale.pdf).
