a = ['alina', 'katarzyna', 'maciek']
b = ['bartek', 'krzysiek', 'alina', 'maciek']
c = ['bartek', 'ania', 'kasia', 'alina']
a2=set(a)
b2=set(b)
c2=set(c)

suma = {*a2, *b2}
cz_wspolna = a2.intersection(b2)
print(cz_wspolna)
print(c2.difference(a2))
print(a2 &c2 & b2)
print(b2.difference(a2 & c2))
print(a2.union(b2, c2))
print(a2.difference(b2.union(c2)))
all = []
rmf = {"slaskie","mazowieckie", "lubelskie","podkarpackie", "maloposlkie"}
zet = {"slaskie", "lubelskie","podkarpackie", "maloposlkie","zachodnio pomorskie","podlaskie","swietokrzystkie"}
eska = {"dolnoślaskie","mazowieckie", "lubelskie","podkarpackie", "maloposlkie", "opolskie", "pomorskie"}
jedynka= {"slaskie","mazowieckie", "lubelskie","podkarpackie", "maloposlkie", "wielkopolskie", "opolskie","lubuskie", "wielkopolskie"}
dwojka = {"slaskie","mazowieckie", "lodzkie","podkarpackie", "maloposlkie", "warminsko-mazurskie"}
rock_radio = {"slaskie","mazowieckie", "lubelskie","podkarpackie", "maloposlkie","warminsko-mazurskie"}
euro = {"slaskie","mazowieckie", "lubelskie","podkarpackie", "maloposlkie", "zachodnio pomorskie","lubuskie", "wielkopolskie"}
slaskie_radio = {"slaskie","mazowieckie", "lubelskie","pomorskie", "maloposlkie"}
radio_kids = {"slaskie","mazowieckie", "lubelskie","podkarpackie", "maloposlkie", "warminsko-mazurskie"}
radio_polo = {"slaskie","mazowieckie", "pomorskie","podkarpackie", "maloposlkie", "lodzkie"}

all.append(rmf)
all.append(zet)
all.append(eska)
all.append(jedynka)
all.append(dwojka)
all.append(rock_radio)
all.append(euro)
all.append(slaskie_radio)
all.append(radio_kids)
all.append(radio_polo)
wszystkie = {"slaskie","mazowieckie","lubelskie", "podkarpackie", "maloposlkie", "warminsko-mazurskie", "opolskie","zachodnio-pomorskie",
             "pomorskie", "swietokrzystkie","lodzkie", "podlaskie", "kujawsko-pomorskie", "dolnoslaskie", "lubuskie", "wielkopolskie"}


posortowane = sorted(all)
print(posortowane)