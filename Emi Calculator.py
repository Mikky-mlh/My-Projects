p = int(input("Principal: "))
r = float(input("Rate: "))
m = int(input("Moratorium period (in months): "))
t = int(input("Time exclusive of moratorium: "))
family_income = float(input("Family income: "))

S = p*r*m/1200 + p
C = p*(1 + r/1200)**(t)
c_emi = p * (r/1200) * ((1 + r/1200)**t) / (((1 + r/1200)**t) - 1)
X = (C+S)/(m+t)

if family_income <= 450000:
    print("EMI: ", c_emi)
else:
    print("EMI: ", X)
