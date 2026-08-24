print("*****Grocery Billing calculator*****")

soap_qty=float(input("Enter quantity of soap(in unit): "))
soap_price_per_unit=50
soap_total=soap_qty*soap_price_per_unit 

rice_qty=float(input("Enter quantity of rice(in kg): "))
rice_price_per_kg=100
rice_total=rice_qty*rice_price_per_kg

flour_qty=float(input("Enter quantity of flour(in kg): "))
flour_price_per_kg=200
flour_total=flour_qty*flour_price_per_kg

oil_qty=float(input("Enter quantity of oil(in lit): "))
oil_price_per_lit=150
oil_total=oil_qty*oil_price_per_lit

dal_qty=float(input("Enter quantity of dal(in kg): "))
dal_price_per_kg=100
dal_total=dal_qty*dal_price_per_kg

print("***Bill Details***")
print("soap:", soap_total)
print("rice: ", rice_total)
print("flour: ", flour_total)
print("oil: ", oil_total)
print("dal: ", dal_total)

total_Bill= soap_total+rice_total+flour_total+oil_total+dal_total
print("total Bill:", total_Bill)


if total_Bill>=1000:
    discount=total_Bill*0.10

    discount=total_Bill*0.05

else:
    discount=0
 
finalamount=total_Bill-discount

print("\n***Bill Details***")
print("total:",total_Bill)
print("discount:",discount)
print("final amount:",finalamount)

