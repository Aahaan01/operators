amount=int(input("Enter the total amount"))
note1=(amount//2000)
note2=(amount%2000)//500
note3=((amount%2000)%500)//100
note4=(((amount%2000)%500)%100)//50
print("2000 Rs. note", note1)
print("500 Rs. note", note2)
print("100 Rs. note", note3)
print("50 Rs. note", note4)