a = ['alina', 'katarzyna', 'maciek']
b = ['bartek', 'krzysiek', 'alina', 'maciek']
c = ['bartek', 'ania', 'kasia', 'alina']
a2 = set(a)
b2 = set(b)
c2 = set(c)

suma = {*a2, *b2}
cz_wspolna = a2.intersection(b2)
print(cz_wspolna)
print(c2.difference(a2))
print(a2 & c2 & b2)
print(b2.difference(a2 & c2))
print(a2.union(b2, c2))
print(a2.difference(b2.union(c2)))

rmf = {"slaskie", "mazowieckie", "lubelskie", "podkarpackie", "malopolskie"}
zet = {"slaskie", "lubelskie", "podkarpackie", "malopolskie", "zachodnio-pomorskie", "podlaskie", "swietokrzyskie"}
eska = {"dolnoslaskie", "mazowieckie", "lubelskie", "podkarpackie", "malopolskie", "opolskie", "pomorskie"}
jedynka = {"slaskie", "mazowieckie", "lubelskie", "podkarpackie", "malopolskie", "wielkopolskie", "opolskie",
           "lubuskie", "wielkopolskie", "kujawsko-pomorskie"}
dwojka = {"slaskie", "mazowieckie", "lodzkie", "podkarpackie", "malopolskie", "warminsko-mazurskie"}
rock_radio = {"slaskie", "mazowieckie", "lubelskie", "podkarpackie", "malopolskie", "warminsko-mazurskie"}
euro = {"slaskie", "mazowieckie", "lubelskie", "podkarpackie", "malopolskie", "zachodnio-pomorskie", "lubuskie",
        "wielkopolskie"}
slaskie_radio = {"slaskie", "mazowieckie", "lubelskie", "pomorskie", "malopolskie"}
radio_kids = {"slaskie", "mazowieckie", "lubelskie", "podkarpackie", "malopolskie", "warminsko-mazurskie"}
radio_polo = {"slaskie", "mazowieckie", "pomorskie", "podkarpackie", "malopolskie", "lodzkie"}

all = sorted(
    [(rmf, "rmf"), (zet, "zet"), (eska, "eska"), (jedynka, "jedynka"), (dwojka, "dwojka"), (rock_radio, "rock_radio"),
     (euro, "euro"), (slaskie_radio, "slaskie_radio"), (radio_polo, "radio_polo"), (radio_kids, "radio_kids")],
    key=lambda x: len(x[0]), reverse=True)

wszystkie = {"slaskie", "mazowieckie", "lubelskie", "podkarpackie", "malopolskie", "warminsko-mazurskie", "opolskie",
             "zachodnio-pomorskie",
             "pomorskie", "swietokrzyskie", "lodzkie", "podlaskie", "kujawsko-pomorskie", "dolnoslaskie", "lubuskie",
             "wielkopolskie"}

result = {}

