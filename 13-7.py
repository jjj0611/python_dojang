price = int(input())
coupon = input()
if coupon == "Cash3000":
    price -= 3000
elif coupon == "Cash5000":
    price -= 5000
print(price)