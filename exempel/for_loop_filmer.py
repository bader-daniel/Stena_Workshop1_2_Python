alla_filmer = ['Life of Brian', 'Quest for the Holy Grail', 'forget the third one']
filmer_hemma = []
filmer_ute = ['Life of Brian', 'Quest for the Holy Grail', 'forget the third one']
filmer_tillbaka = ["Life of Brian", "Quest for the Holy Grail"]  # Dessa ska registreras

print("Så här ser listorna ut inledningsvis:")
print(f"Alla filmer: {alla_filmer}")
print(f"filmer hemma: {filmer_hemma}")
print(f"filmer ute: {filmer_ute}")
print(f"filmer tillbaka: {filmer_tillbaka}")
print() # ny rad för läsbarhet

print("Loop")
for film in filmer_tillbaka:                         # Loopa igenom filmerna som ska registreras som hemma
    print(f"Denna gången tittar loopen på {film}")   # Inte nödvändig, ger oss insyn i vad som händer i loopen
    filmer_hemma.append(film)                        # Lägg till nuvarande film i listan över filmer vi har hemma
    filmer_ute.remove(film)                          # Ta bort filmen ur listan över filmer vi har utlånade

filmer_tillbaka.clear()          # Rensa listan över filmer som ska registreras


print() # ny rad för läsbarhet
print("såhär ser listorna ut efter loopen")S
print(f"Alla filmer: {alla_filmer}")
print(f"filmer hemma: {filmer_hemma}")
print(f"filmer ute: {filmer_ute}")
print(f"filmer tillbaka: {filmer_tillbaka}")
