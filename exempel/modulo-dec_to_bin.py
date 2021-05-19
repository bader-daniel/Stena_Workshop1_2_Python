# Detta är en enkelt konverterare som visar ett inmatat tal i binär form.
# Det saknas validering av inmatning som jag påpekat är viktigt, det är för att göra koden så tydlig som möjligt.
# Likadant med kommentarer, här har jag varit övertydlig.

decimal = int(input('Ange ett heltal du vill se binärt: ')) # initiala talet vill konvertera till decimalt
binar = '' # textsträng vi gradvis kommer bygga på tills vi får vårt tal i binär form


while decimal > 0: # loop som kör tills vi gått igenom hela talet
    if decimal % 2 == 1:  # jämför om vårt decimala tal går att dela med två
        binar = '1' + binar  # om ej lägger vi på en 1:a längst till vänster i vårt binära tal, det blir alltså den
        # mest signifikanta biten.
        decimal -= 1 # vi tar även bort ettan om den fanns
    else:
        binar = '0' + binar # gick det att dela jämt med 2 lägger vi till en 0:a
        # ex, 128 kan vi dela med två, men vi vill ju ha med den biten, så vi lägger till en nolla, vi tar inte bort
        # nånting

    decimal /= 2 # för att gå vidare till nästa signifikans delar vi talet vi jobbar med med två. är vi inte nere på
    # noll börjar loopen om igen.

print(binar)

