# Analiza prometnih nesreč v sloveniji

## Člani skupine

| Ime in priimek | Vpisna številka |
| -------------- | --------------- |
| Špela Čoha | 04200493 |
| Gal Fajon | 63210064 |
| Manca Lapanje | 04200495 |
| Tia Šarkezi | 63220525 |

## Opis problema in cilji raziskave

V naši nalogi želimo analizirati podatke o prometnih nesrečah v Sloveniji od leta 2009 do 2022. Naš cilj je ugotoviti:

- število prometnih nesreč po letih,
- kdo so največkrat povzročitelji nesreč,
- stopnjo korelacije med povzročitvijo nesreče in vozniškim stažem,
- kako pogosti so različni izidi prometnih nesreč,
- stopnjo korelacije med tipi poškodb in uporabo varnostnega pasu,
- v kakšnem vremenu, ob katerih dneh in katerem delu dneva so prometne nesreče najpogostejše.

## Opis podatkov

Podatke o prometnih nesrečah v Sloveniji smo našli na spletni strani OPSI (https://podatki.gov.si/dataset/mnzpprometne-nesrece-od-leta-2009-dalje).
Podatki o nesrečah za vsako leto so zapisani v ločenih .csv datotekah.

## Rezultati

### Delež prometnih nesreč po letih
![nesrecepoletih](https://user-images.githubusercontent.com/104381957/232863052-f6a00135-ee40-4993-8520-dc75323c9a94.jpg)

V zgornjem grafu smo poskusili prikazati delež prometnih nesreč glede na posamezno leto. Tu je možno opaziti dve zanimivosti. Med letom 2012 in 2013 je opaziti zelo strm upad števila prometnih nesreč, ki je potem ponovno začelo naraščati, dokler leta 2020 in 2021, predvidoma zaradi pandemije covida-19, ponovno ostro upade. Leta 2022, ko je bila večina prepovedi gibanja zaradi pandemije ukinjena, se število nesreč ponovno povzpne na skoraj enako število kot prej.



### Starost povzročiteljev nesreč
![povzrocitelji-vozniki](https://user-images.githubusercontent.com/104381957/232863114-bbccc225-3c30-49fe-8909-9070b79881bd.jpg)
![povzrocitelji-kolesarji](https://user-images.githubusercontent.com/104381957/232863105-d55ad431-9f48-44b0-8e0e-b5ffa3c3ee42.jpg)
![povzrocitelji-pesci](https://user-images.githubusercontent.com/104381957/232863112-164e015b-0fdc-48b9-a3e2-4461074b9a93.jpg)

Iz zgornjih analiz je možno opaziti, da so vozniki, ki povzročajo prometne nesreče najpogosteje med štiridesetim in šestdesetim letom starosti ali starejši. Opaziti je možno tudi presenetljivo število mladoletnih voznikov, nekateri so celo mlajši od 16 let in največkrat navedeni kot vozniki lahkih motornih vozil.
Kolesarji, ki z neodgovorno vožnjo povzročijo prometno nesrečo se bolj jasno razdelijo na mladoletne ali starejše. Podobno velja tudi za pešce, kjer je delež pešcev med osemnajstim in enaindvajsetim letom presenetljivo velik.



### Povprečna starost voznika, ki povzroči nesrečo po letih
![starostpovzrocitelja](https://user-images.githubusercontent.com/104381957/232863154-70e19ddb-0fd5-418c-8282-e90cf4b18d36.jpg)

Na zgornjem grafu lahko vidimo zelo počasno naraščanje povprečne starosti povzročitelja prometne nesreče. To je moč povezati s staranjem populacije Slovenije.



### Spol povzročiteljev nesreč
![spolpovzrociteljev](https://user-images.githubusercontent.com/104381957/232863162-ee0722d1-4c9b-4f9f-aa59-2a285e9b42f7.jpg)

Na zgornjem grafu vidimo da je delež moških, ki povzročijo prometno nesrečo v povprečju sedemdeset odstoten.



### Korelacija med tipom poškodbe in uporabo varnostnega pasu
![varnostnipas](https://github.com/TiaSarkezi/PR23SCGFMLTS/assets/104381957/5498164c-2f5e-4450-9149-2f2665cacb9a)

Iz zgornje statistike je razvidno da je delež ljudi, ki so umrli in med vožnjo niso imeli zapetega varnostnega pasu večja kot pri vseh ostalih. Hkrati je delež voznikov ki v nesreči niso utrpeli poškodbe in niso imeli zapetega pasu opazno manjši od deleža zapetih voznikov. Pri ustvarjanju takih ocen je potrebno tudi upoštevati katere vrste nesreč vodijo do kakšnih izidov.



### Toplotni zemljevid
https://nbviewer.org/github/TiaSarkezi/PR23SCGFMLTS/blob/main/zemljevid.ipynb
