# e-Boekhouden

[![BuyMeCoffee][buymecoffeebadge]][buymecoffee]

Dit project wordt niet ondersteund door [e-Boekhouden.nl][eboekhouden]. Het is volledig
gebasseerd op de openbare [API documentatie][api_doc].

- [e-Boekhouden](#e-boekhouden)
  - [Installatie](#installatie)
  - [Gebruik](#gebruik)
  - [App](#app)
    - [get\_administraties()](#get_administraties)
    - [get\_artikelen()](#get_artikelen)
    - [get\_facturen()](#get_facturen)
    - [get\_grootboekrekeningen()](#get_grootboekrekeningen)
    - [get\_kostenplaatsen()](#get_kostenplaatsen)
    - [get\_mutaties()](#get_mutaties)
    - [get\_open\_posten()](#get_open_posten)
    - [get\_relaties()](#get_relaties)
    - [get\_saldi()](#get_saldi)
    - [get\_saldo()](#get_saldo)
    - [add\_relatie()](#add_relatie)
    - [add\_mutatie()](#add_mutatie)
    - [add\_factuur()](#add_factuur)
    - [open\_session() en close\_session()](#open_session-en-close_session)
  - [Models](#models)
    - [Administratie](#administratie)
    - [Artikel](#artikel)
    - [Factuur](#factuur)
    - [Grootboekrekening](#grootboekrekening)
    - [Kostenplaats](#kostenplaats)

***

## Installatie

Gebruik minimaal Python 3.10.

```txt
pip3 install eboekhouden
```

## Gebruik

U vindt deze gegevens via **Beheer > Instellingen > Koppelingen > API/SOAP**.

- Gebruikersnaam
- Beveiligingscode 1
- Beveiligingscode 2

```py
from eboekhouden import App, Artikel

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    # Alle artikelen
    artikelen: list[Artikel] = app.get_artikelen()

    # Zoek een specifiek artikel op basis van omschrijving
    artikelen: list[Artikel] = app.get_artikelen(artikel_omschrijving="Spam")
```

```py
from eboekhouden import App, Factuur

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    # Alle facturen
    facturen: list[Factuur] = app.get_facturen()

    # Zoek een specifieke factuur op basis van factuurnummer
    facturen: list[Factuur] = app.get_facturen(factuurnummer="Eggs")
```

## App

Het `App` object gebruik je om een connectie te maken met jouw eBoekhouden omgeving. Je
kunt het gebruiken als context manager, maar het is niet verplicht.

```py
from eboekhouden import App

# Context Manager (aanbevolen)
with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    ...

# Zonder Context Manager
app = App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2")
app.open_session()
...
app.close_session()
```

Dit object geeft je de onderstaande mogelijkheden.

### get\_administraties()

Gekoppelde administraties ophalen. Geeft een `list` van één of meer
[Administraties](#administratie).

```py
from eboekhouden import App, Administratie

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    administraties: list[Administratie] = app.get_administraties()
```

### get\_artikelen()

Lijst met Artikelen ophalen. Gebruik een of meerdere van onderstaande parameters om het
resultaat te filteren. Geeft een `list` van één of meer [Artikelen](#artikel).

|      Parameter       | Type  |                        Beschrijving                         |
| -------------------- | ----- | ----------------------------------------------------------- |
| artikel_id           | `int` | Filter artikelen op basis van uniek identificatie nummer.   |
| artikel_code         | `str` | Filter artikelen op basis van artikel code.                 |
| artikel_omschrijving | `str` | Filter artikelen op basis van de artikelgroep omschrijving. |
| groep_code           | `str` | Filter artikelen op basis van de artikelgroep code.         |
| groep_omschrijving   | `str` | Filter artikelen op basis van de artikelgroep omschrijving. |

```py
from eboekhouden import App, Artikel

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    # Alle artikelen
    artikelen: list[Artikel] = app.get_artikelen()

    # Artikel met unieke identificatie nummer 123
    artikel: Artikel = app.get_artikelen(artikel_id=123)[0]

    # Artikelen in de groep 'SPAM' met 'EGGS' in de artikel omschrijving
    artikelen: list[Artikel] = app.get_artikelen(
        groep_code='SPAM',
        artikel_omschrijving='EGGS',
    )
```

### get\_facturen()

Lijst met facturen ophalen. Gebruik een of meerdere van onderstaande parameters om het
resultaat te filteren. Geeft een `list` van één of meer [Facturen](#factuur).

|   Parameter   |    Type    |                                                 Beschrijving                                                  |
| ------------- | ---------- | ------------------------------------------------------------------------------------------------------------- |
| factuurnummer | `str`      | Filter facturen op basis van uniek identificatie nummer.                                                      |
| relatiecode   | `str`      | Filter facturen op basis van een relatiecode, gebruik altijd in combinatie met `start_datum` en `eind_datum`. |
| start_datum   | `datetime` | Filter facturen op basis van de factuurdatum, verplicht in combinatie met `relatiecode` en `eind_datum`.      |
| eind_datum    | `datetime` | Filter facturen op basis van de factuurdatum, verplicht in combinatie met `relatiecode` en `start_datum`.     |

```py
from eboekhouden import App, Factuur
from datetime import datetime

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    # Alle facturen
    facturen: list[Factuur] = app.get_facturen()

    # Facturen met factuurnummer 'F123'
    factuur: Factuur = app.get_facturen(factuurnummer='F123')[0]

    # Facturen in het bereik van januari t/m maart 2023.
    facturen: list[Factuur] = app.get_facturen(
        start_datum=datetime(2023, 1, 1),
        eind_datum=datetime(2023, 3, 31),
    )
```

### get\_grootboekrekeningen()

Lijst met grootboekrekeningen ophalen. Geeft een `list` van één of meer
[Grootboekrekeningen](#grootboekrekening).

```py
from eboekhouden import App, Grootboekrekening

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    grootboekrekeningen: list[Grootboekrekening] = app.get_grootboekrekeningen()
```

### get\_kostenplaatsen()

Lijst met kostenplaatsen ophalen. Geeft een `list` van één of meer
[Kostenplaatsen](#kostenplaats).

```py
from eboekhouden import App, Kostenplaats

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    kostenplaatsen: list[Kostenplaats] = app.get_kostenplaatsen()
```

### get\_mutaties()

Lijst met mutaties ophalen. Gebruik een of meerdere van onderstaande parameters om het
resultaat te filteren. Geeft een `list` van één of meer [Facturen](#factuur).

Er zullen nooit meer dan de laatste 500 mutaties opgehaald worden. Voor deze functie
geldt een maximum van 5.000 calls per maand.

|     Parameter     |    Type    |                                       Beschrijving                                       |
| ----------------- | ---------- | ---------------------------------------------------------------------------------------- |
| mutatienummer     | `int`      | Filter mutaties op basis van uniek identificatie nummer.                                 |
| mutatienummer_van | `int`      | Filter mutaties vanaf uniek identificatie nummer.                                        |
| mutatienummer_tot | `int`      | Filter mutaties tot en met uniek identificatie nummer.                                   |
| factuurnummer     | `str`      | Filter mutaties op basis van het bijbehorende factuurnummer.                             |
| start_datum       | `datetime` | Filter mutaties op basis van de mutatiedatum, verplicht in combinatie met `eind_datum`.  |
| eind_datum        | `datetime` | Filter mutaties op basis van de mutatiedatum, verplicht in combinatie met `start_datum`. |

```py
from eboekhouden import App, Mutatie
from datetime import datetime

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    # Alle mutaties, maximaal 500.
    mutaties: list[Mutatie] = app.get_mutaties()

    # Mutaties behorende bij factuurnummer 'F123'
    mutaties: Mutatie = app.get_mutaties(factuurnummer='F123')

    # Mutaties in het bereik van januari t/m maart 2023.
    mutaties: list[Mutatie] = app.get_mutaties(
        start_datum=datetime(2023, 1, 1),
        eind_datum=datetime(2023, 3, 31),
    )
```

### get\_open\_posten()

Lijst met openstaande posten bij debiteuren óf crediteuren ophalen.

```py
from eboekhouden import App, Administratie

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    administraties: list[Administratie] = app.get_administraties()
```

### get\_relaties()

Lijst met relaties ophalen.

```py
from eboekhouden import App, Administratie

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    administraties: list[Administratie] = app.get_administraties()
```

### get\_saldi()

Lijst van saldi per grootboekrekening ophalen.

```py
from eboekhouden import App, Administratie

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    administraties: list[Administratie] = app.get_administraties()
```

### get\_saldo()

Saldo voor een specifieke grootboekrekening of kostenplaats ophalen.

### add\_relatie()

Nieuwe relatie toevoegen.

### add\_mutatie()

Nieuwe mutatie toevoegen.

### add\_factuur()

Nieuwe factuur toevoegen.

### open\_session() en close\_session()

Open een sessie met e-Boekhouden. Wanneer `App` niet al context manager wordt gebruikt,
moet eerst een sessie met e-Boekhouden worden gestart met `open_session()`. Zonder een
sessie kan geen data worden opgehaald of verwerkt in e-Boekhouden. Na gebruik moet de
sessie worden gesloten met `close_session()`.

```py
from eboekhouden import App

app = App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2")
app.open_session()
...
app.close_session()
```

Wanneer `App` wel wordt gebruikt als contect manager, is dit niet nodig.

```py
from eboekhouden import App

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    ...
```

## Models

### Administratie

Het `Administratie` object representeert een gekoppelde administratie. In
e-Boekhouden vindt u deze via
**Beheer > Instellingen > Overige > Gekoppelde administraties**

Het `Administratie` object bevat de volgende attributen.

- `bedrijf`: Naam van het bedrijf.
- `plaats`: Plaatsnaam van het bedrijf.
- `guid`:  Unieke systeem identificatie van de gekoppelde administratie.
- `start_boekjaar`: Datum van beging van het boekjaar van gekoppelde administratie.
Alleen van toepassing indien sprake is van een gebroken boekjaar.

`get_administraties()`

Gekoppelde administraties ophalen. Deze methode vraagt geen parameters en geeft een
`list` van `Administratie` objecten.

```py
with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    administraties = app.get_administraties()
```

### Artikel

...

### Factuur

...

### Grootboekrekening

...

### Kostenplaats

...

***

[eboekhouden]: "https://www.e-boekhouden.nl/"
[api_doc]: "https://www.e-boekhouden.nl/koppelingen/api"
[buymecoffee]: https://www.buymeacoffee.com/niro1987
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
