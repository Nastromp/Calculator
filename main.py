Zahl1=int(input("1 Number:"))
Zahl2=int(input("2 Number:"))
Rechenzeichen=input("Choose +, -, *, /: ")

Ergebnis=0

if Rechenzeichen=="+":
    Ergebnis=Zahl1+Zahl2
if Rechenzeichen=="-":
    Ergebnis=Zahl1-Zahl2
if Rechenzeichen=="*":
    Ergebnis=Zahl1*Zahl2
if Rechenzeichen=="/":
    Ergebnis=Zahl1/Zahl2
print("The result is:", Ergebnis)
