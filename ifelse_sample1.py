#Kullanıcıdan veri almak için kullandığımız komut INPUT
sinav1=input("Birinci yazılı notunu giriniz:")
sinav2=input("İkinci yazılı notunu giriniz:")
per=input("Performans notunu giriniz:")
ort=(int(sinav1)+int(sinav2)+int(per))/3
if ort<50:
    print("Başarısız")
else:
    print("Başarılı")
