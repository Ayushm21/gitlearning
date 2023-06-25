#simple intererest calculation
principal = (input("Please Enter the down payment you wish to pay : "))
roi = (input("Enter rate of interest per annum : "))
time = (input("Enter the time period in years : "))

print("\n")
print("*****EMI Calculator*****")
print("\n")

#calculating the finsl amount
if(roi<=0):
    print("ERROR!!ROI can't be zero or negative")
elif(time<=0):
    print("ERROR!!Time can't be zero or negative")
else:
    amount = int(principal)+int(principal)*int(roi)*int(time)
    print("As per the provided by you, your final amount would be :",amount)
    #calculating the emi
    months = int(time)*12
    emi = int(amount)/int(months)
    print("Your monthly EMI for",time,"years would be :",emi)



