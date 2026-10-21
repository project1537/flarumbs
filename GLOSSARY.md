# Rječnik i stil prijevoda

Ovaj dokument opisuje kako paket prevodi Flarum, da novi prijevodi zvuče isto kao postojeći. Kad dodajete ili ispravljate prijevod, držite se termina ispod. Ako vam neki termin ne odgovara, otvorite [Issue](https://github.com/project1537/flarumbs/issues) i predložite izmjenu za cijeli paket. Ne mijenjajte ga samo u jednoj datoteci.

Termini iz kolone „Ne koristiti“, kao i pravila o „vi/vaš“ i tri tačke, provjeravaju se automatski: provjera na svakom pull requestu prikazuje upozorenje na liniji gdje se pojave. Izuzetak su „post“ i „tag“, jer se te riječi javljaju i u varijablama i tehničkim nazivima, pa ih treba paziti ručno.

## Osnovni termini

| Engleski | Bosanski | Ne koristiti |
| --- | --- | --- |
| forum (naziv sajta) | platforma, edukativna platforma | |
| discussion | tema | diskusija |
| post | objava | post |
| reply | odgovor | |
| tag | oznaka | tag |
| user | korisnik | |
| member | član | |
| nickname, display name | prikazano ime | nadimak |
| username | korisničko ime | |
| account | korisnički račun, račun | |
| avatar | profilna slika | |
| sign up | registracija, registrirati se | registrovati |
| log in | prijava, prijaviti se | login |
| log out | odjava, odjaviti se | |
| flag (a post) | prijava, prijaviti objavu | |
| suspend | blokirati, blokada | suspendovati |
| approve | odobriti | |
| hide | sakriti | |
| delete | obrisati | izbrisati |
| edit | urediti | |
| save | sačuvati | spremiti |
| cancel | odustati, otkazati | |
| settings | postavke | |
| permission | dozvola | ovlaštenje (pridjev „ovlašten“ je u redu) |
| notification | obavještenje | notifikacija |
| email | e-mail | e-pošta, mejl |
| file | datoteka | fajl |
| upload | učitati, učitavanje | |
| encrypt | šifrovati, šifrovanje | šifrirati |
| generate | generisati, generisanje | generirati |
| link | link | poveznica |
| browser | preglednik | |
| search | pretraga, pretražiti | |
| week | sedmica | tjedan |
| extension | ekstenzija | |
| private message | privatna poruka | |
| private discussion (Byobu) | privatna tema | |
| audit log | dnevnik aktivnosti | |

Paket je pisan za obrazovne platforme, pa na nekim mjestima, uglavnom u e-mailovima i porukama jezgre, kaže „edukativna platforma“. To je namjerno i tako ostaje. Na ostalim mjestima stoji „platforma“.

Kad engleski kaže „forum“ u smislu softvera ili kategorije sajtova (npr. „drugi forumi koji koriste StopForumSpam“), prevodi se kao „forum“.

## Stil

- **Ijekavica**: mjesec, vrijeme, obavještenje, promijeniti.
- **Navodnici**: „ovako“. Ravne navodnike `"` koristite samo u kodu i primjerima unosa.
- **Crtica**: za umetnute dijelove rečenice koristite crticu s razmacima ( – ), ne minus.
- **Obraćanje korisniku**: u drugom licu množine, bez glagola u rodu („Jeste li sigurni…“, „Prijavite se…“).
- **Vi, vaš**: u sučelju malim slovom („vaš korisnički račun“), u e-mailovima velikim („Vaš korisnički račun“), a na početku rečenice uvijek velikim. E-mailovi su poruke u imenskom prostoru `<ekstenzija>.email.*`.
- **Tri tačke**: znak „…“, ne tri odvojene tačke („Učitavanje…“).
- **Glagoli stranog porijekla**: oba oblika (*-irati* i *-ovati/-isati*) su u bosanskom standardu, ali paket za svaki glagol koristi samo jedan. Pogledajte tabelu iznad; za glagol kojeg nema u tabeli uzmite oblik koji se već koristi u paketu.
- **Bez roda za osobu iz varijable**: Flarum ne zna spol korisnika, pa ne pišite „{username} je poslao“. Napišite rečenicu drugačije, npr. „Nova poruka od korisnika {username}“. Opšti muški rod uz imenicu je ispravan („korisnik je učitao“, „administrator je potvrdio“).
- **Dugmad i naslovi**: kratko, glagol u imperativu za dugmad („Sačuvaj promjene“, „Obriši“), imenica za naslove i dozvole („Brisanje objava“).

## Tehnička pravila

Ova pravila provjerava automatska provjera. Kršenje je greška i pull request ne može proći:

- **Varijable** u vitičastim zagradama (`{username}`, `{count}`) i **oznake** (`<a>`, `<strong>`) moraju ostati iste kao u engleskom. Smiju promijeniti mjesto u rečenici.
- **Množina** u bosanskom ima tri oblika: `one` (1, 21, 31…), `few` (2–4, 22–24…) i `other` (ostalo). Primjer:
  `{count, plural, one {# objava} few {# objave} other {# objava}}`.
  Grana `other` je obavezna.
- **Reference** oblika `=> core.ref.save_changes` moraju voditi na ključ koji postoji.
- **Ključevi** se ne smiju ponavljati unutar iste datoteke.

## Kada ekstenzija doda ili promijeni poruke

Svakog ponedjeljka automatska provjera poredi sve prijevode s najnovijim izdanjem svake ekstenzije. Ako nešto nedostaje ili se engleski tekst promijenio, otvara ili ažurira Issue „Translations to update“ s tačnim spiskom.

- Poruke koje nedostaju, zastarjeli ključevi i pogrešne varijable nestaju sa spiska čim se datoteka ispravi.
- Poruke čiji se engleski tekst promijenio ostaju na spisku dok se nova verzija ne prihvati. Nakon ispravke prijevoda pokrenite workflow **Check upstream translations** (*Actions → Check upstream translations → Run workflow*) i u polje `accept` upišite nazive datoteka, npr. `fof-upload,fof-oauth`, ili `all`.
