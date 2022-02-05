from zeme_kavy import zeme_kavy

with open('vlajky.txt') as vstup:
    vlajky = vstup.read().splitlines()

# vlajky.sort()
# with open('vlajky_sorted.txt', 'w', newline='\n') as zapis:
#     for zeme in vlajky:
#         zapis.write(f"{zeme}\n")

vlajky_slovnik = {}
with open('vlajky_slovnik.py', "w") as vystup:
    vystup.write("flags = {\n")
    for radek in vlajky:
        *zeme, vlajka = radek.split(' ')
        zeme = " ".join(zeme)
        if zeme in zeme_kavy:
            vlajky_slovnik[zeme] = vlajka
            vystup.write(f'    "{zeme}": "{vlajka}",\n')
    vystup.write("}\n")
if len(zeme_kavy) == len(vlajky_slovnik):
    print("Všechny vlajky nalezeny!")