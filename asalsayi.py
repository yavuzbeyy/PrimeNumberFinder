girilenSayi =int(input("Bir sayı giriniz : "))

asalMi = 0

for i in range(2,girilenSayi):
    if (girilenSayi % i) == 0:
        counter = counter+1

if (asalMi==0):
    print(girilenSayi,"Sayi Asaldır")
else:
    for j in range(girilenSayi,(girilenSayi+10)):
        sayac=0
        for k in range(2,j):
            if(j%k==0):
                sayac=sayac+1
                break
        if(sayac==0):
            print(j)
            break