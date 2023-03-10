# Analiza prometnih nesreč v Sloveniji

## Člani skupine

| Ime in priimek | Vpisna številka |
| -------------- | --------------- |
| Špela Čoha | 04200493 |
| Gal Fajon | 63210064 |
| Manca Lapanje | 04200495 |
| Tia Šarkezi | 63220525 |

## Opis problema in cilji raziskave

V naši nalogi želimo analizirati podatke o prometnih nesrečah v Sloveniji od leta 2009 do 2022. Naš cilj je ugotoviti:

- delež prometnih nesreč po letih,
- kdo so največkrat povzročitelji nesreč,
- stopnjo korelacije med povzročitvijo nesreče in vozniškim stažem,
- kako pogoste so različne stopnje poškodb,
- v kakšnem vremenu, ob katerem delu dneva, v katerih mestih in na katerih cestah so prometne nesreče najpogostejše.

## Opis podatkov

Podatke o prometnih nesrečah v Sloveniji smo našli na spletni strani OPSI (https://podatki.gov.si/dataset/mnzpprometne-nesrece-od-leta-2009-dalje).
Podatki o nesrečah za vsako leto so zapisani v ločenih .csv datotekah. V teh datotekah najdemo naslednje atribute:

`ZaporednaStevilkaPN` - številka za štetje in ločevanje posamezne prometne nesreče

`KlasifikacijaNesrece` - klasifikacija nesreče glede na posledice (avtomatičen izračun glede na najhujšo posledico pri udeležencih v prometni nesreči)

`UpravnaEnotaStoritve` - upravna enota, na območju katere se je zgodila prometna nesreča

`DatumPN`, `UraPN` - datum in ura prometne nesreče

`VNaselju` - indikator ali se je nesreča zgodila v naselju (D) ali izven (N)

`Lokacija` - lokacija nesreče (cesta/naselje)

`VrstaCesteNaselja`, `SifraCesteNaselja`, `TekstCesteNaselja` - vrsta, oznaka in tekst ceste ali naselja, kjer je prišlo do nesreče

`SifraOdsekaUlice`, `TekstOdsekaUlice` - oznaka in tekst odseka ali ulice, kjer je prišlo do nesreče

`StacionazaDogodka` - točna stacionaža ali hišna številka, kjer je prišlo do nesreče

`OpisKraja` - opis prizorišča nesreče

`VzrokNesrece`, `TipNesrece` - glavni vzrok in tip nesreče

`VremenskeOkolicine` - vremenske okoliščine v času nesreče (jasno, oblačno, megla, deževno...)

`StanjePrometa`, `StanjeVozisca` - stanje prometa in vozišče v času nesreče

`GeoKoordinataX`, `GeoKoordinataY` - koordinate prometne nesreče

`ZaporednaStevilkaOsebeVPN` - številka za štetje in ločevanje oseb, udeleženih v prometnih nesrečah

`Povzrocitelj` - kot kaj nastopa oseba v prometni nesreči (povzročitelj/udeleženec)

`Starost`, `Spol` - starost in spol osebe

`UEStalnegaPrebivalisca` - upravna enota stalnega prebivališča

`Drzavljanstvo` - državljanstvo osebe

`PoskodbaUdelezenca` - poškodba osebe (brez poškodbe, lažja telesna poškodba, huda telesna poškodba, smrt)

`VrstaUdelezenca` - vrsta udeleženca (voznik osebnega avtomobila, voznik lahkega motornega vozila, pešec, potnik, voznik avtobusa, voznik tovornega vozila...)

`UporabaVarnostnegaPasu` - ali je oseba uporabljala varnostni pas ali čelado (polje se interpretira v odvisnosti od vrste udeleženca) (Da/Ne)

`VozniskiStazVLetih`, `VozniskiStazVMesecih` - vozniški staž osebe za kategorijo, ki jo potrebuje glede na vrsto udeleženca v prometu

`VrednostAlkotesta` - vrednost alkotesta za osebo, če je bil opravljen (n.nn v enoti mg alkohola/liter izdihanega zraka (mg/l))

`VrednostStrokovnegaPregleda` - vrednost strokovnega pregleda za osebo, če je bil odrejen in so rezultati že znani (n.nn v enoti g alkohola/kg krvi (g/kg))
