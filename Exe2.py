bill = (float(input("enter your bill? ")))
tip = (int(input()))
people = int(input())
tips_person = tip / 100
# 10/100=0.1 1
total_tip_amt = bill * tips_person
# 157.45*0.1
total_bill = bill + total_tip_amt
# 157.45+total_tip amt
bill_person = total_bill / people
# final_amt = round(bill_person,2)
final_amt="{:.2f}".format(bill_person)
print(f"${final_amt}")
