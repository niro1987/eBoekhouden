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
    - [get\_open\_posten\_debiteuren() en get\_open\_posten\_crediteuren()](#get_open_posten_debiteuren-en-get_open_posten_crediteuren)
    - [get\_relaties()](#get_relaties)
    - [get\_saldi()](#get_saldi)
    - [get\_saldo()](#get_saldo)
    - [add\_factuur()](#add_factuur)
    - [add\_mutatie()](#add_mutatie)
    - [add\_relatie()](#add_relatie)
    - [open\_session() en close\_session()](#open_session-en-close_session)
  - [Models](#models)
    - [Administratie](#administratie)
    - [Artikel](#artikel)
    - [Factuur](#factuur)
    - [Factuur Regel](#factuur-regel)
    - [Grootboekrekening](#grootboekrekening)
    - [Kostenplaats](#kostenplaats)
    - [Mutatie](#mutatie)
    - [Mutatie Regel](#mutatie-regel)
    - [Open Post](#open-post)
    - [Relatie](#relatie)
    - [Saldo](#saldo)
  - [Types](#types)
    - [BTW Code](#btw-code)
    - [Eenheid](#eenheid)
    - [Grootboek Categorie](#grootboek-categorie)
    - [In Ex BTW](#in-ex-btw)
    - [Incasso Machtiging Soort](#incasso-machtiging-soort)
    - [Mutatie Soort](#mutatie-soort)
    - [Relatie Type](#relatie-type)

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

Het `App` object gebruik je om een connectie te maken met jouw eBoekhouden omgeving. Je kunt het
gebruiken als context manager, maar het is niet verplicht.

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

Lijst met Artikelen ophalen. Gebruik een of meerdere van onderstaande parameters om het resultaat te
filteren. Geeft een `list` van één of meer [Artikelen](#artikel).

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

Lijst met facturen ophalen. Gebruik een of meerdere van onderstaande parameters om het resultaat te
filteren. Geeft een `list` van één of meer [Facturen](#factuur).

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

Lijst met kostenplaatsen ophalen. Geeft een `list` van één of meer [Kostenplaatsen](#kostenplaats).

```py
from eboekhouden import App, Kostenplaats

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    kostenplaatsen: list[Kostenplaats] = app.get_kostenplaatsen()
```

### get\_mutaties()

Lijst met mutaties ophalen. Gebruik een of meerdere van onderstaande parameters om het resultaat te
filteren. Geeft een `list` van één of meer [Mutaties](#mutatie).

Er zullen nooit meer dan de laatste 500 mutaties opgehaald worden. Voor deze functie geldt een
maximum van 5.000 calls per maand.

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

### get\_open\_posten\_debiteuren() en get\_open\_posten\_crediteuren()

Lijst met openstaande posten van debiteuren en crediteuren ophalen. Geeft een `list` van geen of
meer [Open Posten](#open-post).

```py
from eboekhouden import App, OpenPost

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    debiteuren: list[OpenPost] = app.get_open_posten_debiteuren()
    crediteuren: list[OpenPost] = app.get_open_posten_crediteuren()
```

### get\_relaties()

Lijst met relaties ophalen. Gebruik een of meerdere van onderstaande parameters om het resultaat te
filteren. Geeft een `list` van één of meer [Relaties](#relatie).

| Parameter  | Type  |                                    Beschrijving                                    |
| ---------- | ----- | ---------------------------------------------------------------------------------- |
| relatie_id | `int` | Filter relaties op basis van uniek identificatie nummer.                           |
| trefwoord  | `str` | Zoek relaties op basis code, bedrijfsnaam, plaats, contactpersoon, email en soort. |
| code       | `str` | Filter relaties op basis van code.                                                 |

```py
from eboekhouden import App, Relatie

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    # Alle relaties
    relaties: list[Relatie] = app.get_relaties()

    # Relaties met een emailadres bij `@example.com`
    relaties: list[Relatie] = app.get_relaties(trefwoord='@example.com')

    # Relatie met code 'SPAM'
    relatie: Relatie = app.get_relaties(code='SPAM')[0]
```

### get\_saldi()

Lijst van saldi per grootboekrekening ophalen. Geeft een `list` van [Saldo](#saldo) per
grootboekrekening.

```py
from eboekhouden import App, Saldo

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    saldi: list[Saldo] = app.get_saldi()
```

### get\_saldo()

Saldo voor een specifieke grootboekrekening of kostenplaats ophalen. Geeft het saldo van de
gespecificeerde grootboekrekening als een `float`.

|    Parameter    | Type  |                        Beschrijving                        |
| --------------- | ----- | ---------------------------------------------------------- |
| grootboek_code  | `str` | Grootboek code.                                            |
| kostenplaats_id | `int` | Optioneel. Uniek identificatie nummer van de kostenplaats. |

```py
from eboekhouden import App

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    kas: float = app.get_saldo("1000")  # Kas
    bank: float = app.get_saldo("1010")  # Bank
```

### add\_factuur()

Nieuwe factuur toevoegen. Geeft het uniek identificatie nummer van de aangemaakt
[Factuur](#factuur). Geeft een `Exception` foutmelding als de factuur niet kan worden aangemaakt.

| Parameter |        Type         |          Beschrijving           |
| --------- | ------------------- | ------------------------------- |
| factuur   | [Factuur](#factuur) | Factuur object om aan te maken. |

```py
from eboekhouden import App, Factuur, FactuurRegel, BTWCode, Eenheid
from datetime import datetime

new_factuur: Factuur = Factuur(
    relatiecode="SPAM",
    datum=datetime.today(),
    betalingstermijn="14",
    per_email_verzenden=True,
    email_onderwerp="Factuur",
    email_van_adres="email@example.com",
    email_bericht="Eggs",
    automatische_incasso=False,
    in_boekhouding_plaatsen=True,
    boekhoudmutatie_omschrijving="Bacon",
    regels=[
        FactuurRegel(
            code="SAUSAGE",
            omschrijving="Sausage",
            aantal=1,
            eenheid=Eenheid.STUK,
            prijs_per_eenheid=2,
            btw_code=BTWCode.HOOG_VERK_21,
            tegenrekening_code="0130",  # Inventarissen
        ),
    ],
)

with App(USERNAME, SECURITY_CODE_1, SECURITY_CODE_2) as app:
    new_factuur_id: int = app.add_factuur(new_factuur)
```

### add\_mutatie()

Nieuwe mutatie toevoegen. Geeft het uniek identificatie nummer van de aangemaakt
[Mutatie](#mutatie). Geeft een `Exception` foutmelding als de mutatie niet kan worden aangemaakt.

| Parameter |        Type         |          Beschrijving           |
| --------- | ------------------- | ------------------------------- |
| mutatie   | [Mutatie](#mutatie) | Mutatie object om aan te maken. |

```py
from eboekhouden import App, Mutatie, MutatieSoort, MutatieRegel, BTWCode
from datetime import datetime

new_mutatie: Mutatie = Mutatie(
    soort=MutatieSoort.GELD_ONTVANGEN,
    datum=datetime.today(),
    rekening="1000",  # Kas
    omschrijving="SPAM_EGGS",
    in_ex_btw=InExBTW.EX,
    mutaties=[
        MutatieRegel(
            bedrag_invoer=1,
            bedrag_excl_btw=1,
            bedrag_btw=0.21,
            bedrag_incl_btw=1.21,
            btw_percentage=21,
            btw_code=BTWCode.HOOG_VERK_21,
            tegenrekening_code="1400",  # Eigen vermogen
        ),
    ],
)

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    new_mutatie_id: int = app.add_mutatie(new_mutatie)
```

### add\_relatie()

Nieuwe relatie toevoegen. Geeft het unieke identificatie nummer van de aangemaakt
[Relatie](#relatie). Geeft een `Exception` foutmelding als de relatie niet kan worden aangemaakt.

| Parameter |        Type         |          Beschrijving           |
| --------- | ------------------- | ------------------------------- |
| relatie   | [Relatie](#relatie) | Relatie object om aan te maken. |

```py
from eboekhouden import App, Relatie, RelatieType

new_relatie: Relatie = Relatie(
    bedrijf="SPAM",
    code="EGGS",
    relatie_type=RelatieType.BEDRIJF,
)

with App("Gebruikersnaam", "Beveiligingscode 1", "Beveiligingscode 2") as app:
    new_relatie_id: int = app.add_relatie(new_relatie)
```

### open\_session() en close\_session()

Open een sessie met e-Boekhouden. Wanneer `App` niet al context manager wordt gebruikt, moet eerst
een sessie met e-Boekhouden worden gestart met `open_session()`. Zonder een sessie kan geen data
worden opgehaald of verwerkt in e-Boekhouden. Na gebruik moet de sessie worden gesloten met
`close_session()`.

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

Het `Administratie` object modelleert een gekoppelde administratie.
In e-Boekhouden vindt u deze via **Beheer > Instellingen > Overige**

|   Attribuut    |    Type    |                                Beschrijving                                 |
| -------------- | ---------- | --------------------------------------------------------------------------- |
| bedrijf        | `str`      | Naam van het bedrijf.                                                       |
| plaats         | `str`      | Plaatsnaam.                                                                 |
| guid           | `str`      | Unieke systeem identificatie van de gekoppelde administratie.               |
| start_boekjaar | `datetime` | Begin van het boekjaara, alleen indien sprake is van een gebroken boekjaar. |

### Artikel

Het `Artikel` object modelleert een product of dienst.

|       Attribuut       |  Type   |                  Beschrijving                   |
| --------------------- | ------- | ----------------------------------------------- |
| artikel_id            | `int`   | Unieke identificatie nummer van het artikel.    |
| artikel_omschrijving  | `str`   | Omschrijving.                                   |
| artikel_code          | `str`   | Artikel code.                                   |
| groep_omschrijving    | `str`   | Artikelgroep omschrijving.                      |
| groep_code            | `str`   | Artikelgroep code.                              |
| eenheid               | `str`   | Eenheid, enkelvoud benaming.                    |
| inkoopprijs_excl_btw  | `float` | Inkoopprijs Excl. BTW.                          |
| verkoopprijs_excl_btw | `float` | Verkoopprijs Excl. BTW.                         |
| verkoopprijs_incl_btw | `float` | Verkoopprijs Incl. BTW.                         |
| btw_code              | `str`   | BTW Code.                                       |
| tegenrekening_code    | `str`   | Grootboekrekening code.                         |
| btw_percentage        | `float` | BTW percentage.                                 |
| kostenplaats_id       | `int`   | Uniek identificatie nummer van de kostenplaats. |
| actief                | `bool`  | Geeft aan of het artikel actief is.             |

### Factuur

Het `Factuur` object modelleert een factuur.

|               Attribuut                |                        Type                         |        Beschrijving         |
| -------------------------------------- | --------------------------------------------------- | --------------------------- |
| relatiecode                            | `str`                                               | Relatie code.               |
| datum                                  | `datetime`                                          | Factuurdatum.               |
| regels                                 | `list`\[[FactuurRegel](#factuur-regel)\]            | Factuur regels.             |
| factuursjabloon                        | `str`                                               | Sjabloon.                   |
| factuurnummer                          | `str`                                               | Factuurnummer.              |
| betalingstermijn                       | `int`                                               | Betalingstermijn in dagen.  |
| per_email_verzenden                    | `bool`                                              | Per email verzenden.        |
| email_onderwerp                        | `str`                                               | Onderwerp.                  |
| email_bericht                          | `str`                                               | Bericht.                    |
| email_van_adres                        | `str`                                               | Van emailadres.             |
| email_van_naam                         | `str`                                               | Van naam.                   |
| automatische_incasso                   | `bool`                                              | Automatische incasso.       |
| incasso_iban                           | `str`                                               | IBAN.                       |
| incasso_machtiging_soort               | [IncassoMachtigingSoort](#incasso-machtiging-soort) | Machtigingsoort.            |
| incasso_machtiging_id                  | `str`                                               | Machtiging ID.              |
| incasso_machtiging_datum_ondertekening | `datetime`                                          | Datum ondertekenen.         |
| incasso_machtiging_first               | `bool`                                              | Wel of niet eerste incasso. |
| incasso_rekening_nummer                | `str`                                               | Rekeningnummer.             |
| incasso_tnv                            | `str`                                               | Ten naame van.              |
| incasso_plaats                         | `str`                                               | Plaats.                     |
| incasso_omschrijving_regel1            | `str`                                               | Regel 1.                    |
| incasso_omschrijving_regel2            | `str`                                               | Regel 2.                    |
| incasso_omschrijving_regel3            | `str`                                               | Regel 3.                    |
| in_boekhouding_plaatsen                | `bool`                                              | In boekhouding plaatsen.    |
| boekhoudmutatie_omschrijving           | `str`                                               | Mutatie omschrijving.       |

### Factuur Regel

Het `FactuurRegel` object modelleert een regel op een [Factuur](#factuur).

|     Attribuut      |         Type         |                  Beschrijving                   |
| ------------------ | -------------------- | ----------------------------------------------- |
| aantal             | `float`              | Aantal.                                         |
| eenheid            | [Eenheid](#eenheid)  | Eenheid.                                        |
| code               | `str`                | Artikel code.                                   |
| omschrijving       | `str`                | Omschrijving.                                   |
| prijs_per_eenheid  | `float`              | Prijs per eenheid.                              |
| btw_code           | [BTWCode](#btw-code) | BTW code.                                       |
| tegenrekening_code | `str`                | Grootboekrekening code.                         |
| kostenplaats_id    | `int`                | Uniek identificatie nummer van de kostenplaats. |

### Grootboekrekening

Het `Grootboekrekening` object modelleert een grootboekrekening.

|  Attribuut   |                    Type                    |        Beschrijving         |
| ------------ | ------------------------------------------ | --------------------------- |
| id           | `int`                                      | Uniek identificatie nummer. |
| code         | `str`                                      | Code.                       |
| omschrijving | `str`                                      | Omschrijving.               |
| categorie    | [GrootboekCategorie](#grootboek-categorie) | Categorie.                  |
| groep        | `str`                                      | Groep.                      |

### Kostenplaats

Het `Kostenplaats` object modelleert een kostenplaats. In e-Boekhouden vindt u deze via
**Beheer > Instellingen > Functies aan/uit zetten**

|       Attribuut        | Type  |                        Beschrijving                        |
| ---------------------- | ----- | ---------------------------------------------------------- |
| kostenplaats_id        | `int` | Uniek identificatie nummer.                                |
| omschrijving           | `str` | Omschrijving.                                              |
| kostenplaats_parent_id | `int` | Uniek identificatie nummer van bovenliggende kostenplaats. |

### Mutatie

Het `Mutatie` object modelleert een boukhoudmutatie.

|    Attribuut     |                   Type                   |         Beschrijving          |
| ---------------- | ---------------------------------------- | ----------------------------- |
| soort            | [MutatieSoort](#mutatie-soort)           | Soort mutatie.                |
| datum            | `datetime`                               | Mutatie datum.                |
| rekening         | `str`                                    | Grootboekrekening code.       |
| mutaties         | `list`\[[MutatieRegel](#mutatie-regel)\] | Mutatie regels.               |
| relatie_code     | `str`                                    | Relatie code.                 |
| factuurnummer    | `str`                                    | Factuurnummer.                |
| betalingstermijn | `str`                                    | Betalingstermijn in dagen.    |
| mutatie_nr       | `int`                                    | Uniek identificatie nummer.   |
| boekstuk         | `str`                                    | Boekstuk.                     |
| omschrijving     | `str`                                    | Omschrijving.                 |
| betalingskenmerk | `str`                                    | Betalingskenmerk.             |
| in_ex_btw        | [InExBTW](#in-ex-btw)                    | Invoer is Incl. of Excl. BTW. |

### Mutatie Regel

Het `MutatieRegel` object modelleert een regel op een [Mutatie](#mutatie).

|     Attribuut      |         Type         |                  Beschrijving                   |
| ------------------ | -------------------- | ----------------------------------------------- |
| bedrag_invoer      | `float`              | Bedrag.                                         |
| bedrag_excl_btw    | `float`              | Bedrag Excl. BTW.                               |
| bedrag_btw         | `float`              | BTW bedrag.                                     |
| bedrag_incl_btw    | `float`              | Bedrag Incl. BTW.                               |
| btw_percentage     | `float`              | BTW percentage.                                 |
| btw_code           | [BTWCode](#btw-code) | BTW code.                                       |
| tegenrekening_code | `str`                | Grootboekrekening code.                         |
| kostenplaats_id    | `int`                | Uniek identificatie nummer van de kostenplaats. |

### Open Post

Het `OpenPost` object modelleert een regel op een [Mutatie](#mutatie).

|  Attribuut  |    Type    |      Beschrijving      |
| ----------- | ---------- | ---------------------- |
| mut_datum   | `datetime` | Mutatie datum.         |
| mut_factuur | `str`      | Factuurnummer.         |
| rel_code    | `str`      | Relatie code.          |
| rel_bedrijf | `str`      | Naam van de relatie.   |
| bedrag      | `float`    | Factuurbedrag.         |
| voldaan     | `float`    | Bedrag dat is voldaan. |
| openstaand  | `float`    | Openstaand bedrag.     |

...

### Relatie

Het `Relatie` object modelleert een relatie.

|        Attribuut         |             Type             |             Beschrijving             |
| ------------------------ | ---------------------------- | ------------------------------------ |
| relatie_type             | [RelatieType](#relatie-type) | Bedrijf / Particulier.               |
| code                     | `str`                        | Relatiecode.                         |
| relatie_id               | `int`                        | Uniek identificatie nummer.          |
| add_datum                | `datetime`                   | Datum toegevoegd.                    |
| bedrijf                  | `str`                        | Naam.                                |
| contactpersoon           | `str`                        | Naam van contactpersoon bij bedrijf. |
| geslacht                 | `str`                        | Man / Vrouw / Afdeling               |
| adres                    | `str`                        | Adres.                               |
| postcode                 | `str`                        | Postcode van het vestigingsadres.    |
| plaats                   | `str`                        | Plaats van het vestigingsadres.      |
| land                     | `str`                        | Land van het vestigingsadres.        |
| adres_factuur            | `str`                        | Postadres.                           |
| postcode_factuur         | `str`                        | Postcode van het postadres.          |
| plaats_factuur           | `str`                        | Plaats van het postadres.            |
| land_factuur             | `str`                        | Land van het postadres.              |
| telefoon                 | `str`                        | Telefoonnummer.                      |
| mobiel                   | `str`                        | Mobiel telefoonnummer.               |
| fax                      | `str`                        | Faxnummer.                           |
| email                    | `str`                        | E-mailadres.                         |
| site                     | `str`                        | Website.                             |
| notitie                  | `str`                        | Notitieveld.                         |
| bankrekening             | `str`                        | Bankrekeningnummer.                  |
| girorekening             | `str`                        | Girorekening.                        |
| btw_nummer               | `str`                        | BTW nummer.                          |
| kvk_nummer               | `str`                        | KvK nummer.                          |
| aanhef                   | `str`                        | Aanhef.                              |
| iban                     | `str`                        | IBAN.                                |
| bic                      | `str`                        | BIC van IBAN.                        |
| def1                     | `str`                        | Vrij veld.                           |
| def2                     | `str`                        | Vrij veld.                           |
| def3                     | `str`                        | Vrij veld.                           |
| def4                     | `str`                        | Vrij veld.                           |
| def5                     | `str`                        | Vrij veld.                           |
| def6                     | `str`                        | Vrij veld.                           |
| def7                     | `str`                        | Vrij veld.                           |
| def8                     | `str`                        | Vrij veld.                           |
| def9                     | `str`                        | Vrij veld.                           |
| def10                    | `str`                        | Vrij veld.                           |
| la                       | `str`                        | * Ledenadministratie ('0' of '1').   |
| gb_id                    | `int`                        | ...                                  |
| geen_email               | `int`                        | ...                                  |
| nieuwsbriefgroepen_count | `int`                        | ...                                  |

**\* Ledenadministratie**: _Bevat standaard het cijfer 0, alleen als u gebruik maakt van de_
_ledenadministratiemodule en het betreft een lid dan vult u hier het cijfer 1 in._

### Saldo

Het `Saldo` object modelleert een regel op een [Mutatie](#mutatie).

| Attribuut |                    Type                    |           Beschrijving           |
| --------- | ------------------------------------------ | -------------------------------- |
| id        | `int`                                      | Uniek identificatie nummer.      |
| code      | `str`                                      | Grootboekrekening code.          |
| categorie | [GrootboekCategorie](#grootboek-categorie) | Categorie van grootboekrekening. |
| saldo     | `float`                                    | Saldo.                           |

## Types

### BTW Code

|  Constante   |              Beschrijving               |
| ------------ | --------------------------------------- |
| HOOG_VERK    | BTW hoog, verkopen 19%                  |
| HOOG_VERK_21 | BTW hoog, verkopen 21%                  |
| LAAG_VERK    | * BTW laag, verkopen                    |
| LAAG_VERK_9  | BTW laag, verkopen 9%                   |
| VERL_VERK_L9 | BTW Verlegd 9% (1e op de btw-aangifte)  |
| VERL_VERK    | BTW Verlegd 21% (1e op de btw-aangifte) |
| AFW          | Afwijkend btw-tarief                    |
| BU_EU_VERK   | Leveringen naar buiten de EU 0%         |
| BI_EU_VERK   | Goederen naar binnen de EU 0%           |
| BI_EU_VERK_D | Diensten naar binnen de EU 0%           |
| AFST_VERK    | Afstandsverkopen naar binnen de EU 0%   |
| LAAG_INK     | * BTW laag, inkopen                     |
| LAAG_INK_9   | BTW laag, inkopen 9%                    |
| VERL_INK_L9  | BTW verlegd, laag, inkopen              |
| HOOG_INK     | BTW hoog, inkopen                       |
| HOOG_INK_21  | BTW hoog, inkopen 21%                   |
| VERL_INK     | BTW verlegd, hoog, inkopen              |
| AFW_VERK     | Afwijkend btw-tarief verkoop            |
| BU_EU_INK    | Leveringen/diensten van buiten de EU 0% |
| BI_EU_INK    | Leveringen/diensten van binnen de EU 0% |
| GEEN         | Geen BTW                                |

**\*** _Indien de boekdatum in 2019 of er na valt, wordt 9% aangehouden, daarvoor 6%._

### Eenheid

| Constante | Beschrijving |
| --------- | ------------ |
| GEEN      | Niet bepaald |
| STUK      | Per stuk     |
| DOOS      | Per doos     |
| UUR       | Per uur      |

### Grootboek Categorie

|    Constante     |      Beschrijving       |
| ---------------- | ----------------------- |
| BALANS           | Balans                  |
| WINST_EN_VERLIES | Winst & Verlies         |
| BETAALMIDDELEN   | Betalingsmiddelen       |
| BTW_LAAG         | BTW af te dragen Laag   |
| BTW_HOOG         | BTW af te dragen Hoog   |
| BTW_OVERIG       | BTW af te dragen overig |
| BTWRC            | BTW Rekening Courant    |
| DEBITEUR         | Debiteuren              |
| CREDITEUR        | Crediteuren             |
| VOORBELASTING    | Voorbelasting           |

### In Ex BTW

| Constante | Beschrijving  |
| --------- | ------------- |
| IN        | Inclusief BTW |
| EX        | Exclusief BTW |

### Incasso Machtiging Soort

| Constante  |      Beschrijving      |
| ---------- | ---------------------- |
| EENMALIG   | Eenmalige machtiging   |
| DOORLOPEND | Doorlopende machtiging |

### Mutatie Soort

|         Constante          |       Beschrijving        |
| -------------------------- | ------------------------- |
| FACTUUR_ONTVANGEN          | Factuur ontvangen         |
| FACTUUR_VERSTUURD          | Factuur verstuurd         |
| FACTUUR_BETALING_ONTVANGEN | Factuurbetaling ontvangen |
| FACTUUR_BETALING_VERSTUURD | Factuurbetaling verstuurd |
| GELD_ONTVANGEN             | Geld ontvangen            |
| GELD_UITGEGEVEN            | Geld uitgegeven           |
| MEMORIAAL                  | Memoriaal                 |

### Relatie Type

|  Constante  | Beschrijving |
| ----------- | ------------ |
| PARTICULIER | Particulier  |
| BEDRIJF     | Bedrijf      |

***

[eboekhouden]: "https://www.e-boekhouden.nl/"
[api_doc]: "https://www.e-boekhouden.nl/koppelingen/api"
[buymecoffee]: https://www.buymeacoffee.com/niro1987
[buymecoffeebadge]: https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg?style=for-the-badge
