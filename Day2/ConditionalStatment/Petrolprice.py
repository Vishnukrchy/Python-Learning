# WAP To Print Petrol Price WIth GST Included According to state
state = input("Enter the state: ")
fiexdprice = 100
totalprice = 0
if state == "Punjab":   
    print("Petrol State Gst in Punjab is 5%")
    totalprice = fiexdprice + (fiexdprice*5)/100
elif state == "Bihar":   
    print("Petrol state Gst in Bihar is 10%")
    totalprice = fiexdprice + (fiexdprice*10)/100   
elif state == "UP":   
    print("Petrol state Gst in UP is 15%")
    totalprice = fiexdprice + (fiexdprice*15)/100
else:   
    print("Invalid state")

print("Total price is: ",totalprice)