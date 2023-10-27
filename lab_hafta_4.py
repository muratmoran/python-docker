# -*- coding: utf-8 -*-

# Giresun Üniversitesi
# Bilgisayar Mühendisliği, 2022-2023
# BILM 101 - Bilgisayar Programlama - Python Lab_3

# Programlama en iyi örneklerle öğretilir ve programlamayı öğrenmenin tek yolu 
# daha fazla programlama yapmaktır. Lütfen, örnekleri kendiniz deneyiniz ve 
# alıştırmaları kendiniz yapınız. Başkalarından kopyala yapıştır yapmak size 
# bir şey kazandırmayacaktır. 

# ========================
# Bazı operatörler
# ========================
# Kalan operatörü % bir bölmede kalanı verir, sonuç int
# Tam bölme operatörü // bir bölmede bölümün tam kısmını verir sonuç int

# Çoklu atama ve Karşılaştırma
x,y,z=1,2,3
print(x<y<z)

# ========================
# Mantıksal operatörler (and, or)
# ========================
saat = 12
sıcaklık = 35
print(saat<16 and sıcaklık>30)
print(saat<16 or sıcaklık>30)
print(not(sıcaklık>30))

# ========================
# Bitsel işlem operatörleri and &, or |, XOR ^ eXclusive OR
# ========================
a = 60 # 0011 1100 2 lik düzende
b = 13 # 0000 1101 2 lik düzende
         
# Bitsel ve (&) işlemi 
c = a & b
print(c)

# Bitsel veya (|) işlemi 
d = a | b
print(d)

# Bitsel özel veya, XOR (^) işlemi 
# 0^0=0
# 0^1=1
# 1^0=1
# 1^1=0

e = a ^ b
print(e)

# Bitsel değil (tümleyen) işlemi ~
# Sayı içerisinde her bir bitin tersinin alınması
# 0 -> 1
# 1 -> 0

print(~a)
print(5+(~a))

# Bitsel sola << ve sağa kaydırma >>
# a = 0 0 1 1 1 1 0 0 , a = 60
# c = a<<2
# c = 1 1 1 1 0 0 0 0 , c = 240

# d = a>>2
# d = 0 0 0 0 1 1 1 1 , d = 15

# ========================
# Aitlik operatörü
# ========================
# Aitlik operatörü "in" ve "not in"
print("a" in "merhaba")
print("abc" in "merhaba")
print("abc" not in "merhaba")

# ========================
# AKIŞ KONTROLÜ, YİNELEME ve DÖNGÜLER
# Örnekler
# ======================== 
# 1. 
# In[]:
# ========================
i = 1
while i < 6:
    print(i)
    i += 1

# In[]:
# ========================  
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# In[]:
# ========================  
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# In[]:
# ======================== 
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Döngü tamamlandı.')

# In[]:
# ======================== 
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Döngü tamamlandı.')

# In[]:
# ======================== 
# Dikkat! Çalıştırma!
sayı = 0
while sayı < 10:
    print(f"Sayı şudur {sayı}!")

# In[]:
# ======================== 
# Dikkat! do while!
sifre = "python"
sayac = 0

while True:
    kelime = input("Şifreyi giriniz: ").lower()
    sayac = sayac + 1
    if kelime == sifre:
        break
    if kelime != sifre and sayac > 3: 
        break
    
# In[]:
# ========================
# Girilen bir n sayısına kadar olan doğal sayıların toplamını bulan program.

# n = int(input("Bir n sayısı giriniz: "))

n = 10

# toplamı ve sayacı başlat
top = 0
i = 1

while i <= n:
    top = top + i
    i = i+1    # sayacı güncelle

# toplamı yazdır
print("Toplam", top)

# In[]:
# ========================
# Stringler
isim = "Galatasaray"

for harf in isim:
    print(harf, end=" ")

# In[]:
# ========================  
# Listeler  
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

# In[]:
# ========================
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

# In[]:
# ========================
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Bunu çalıştırır

# In[]:
# ========================
for i in ['foo', 'bar', 'baz', 'qux']:
    if i == 'bar':
        break
    print(i)
else:
    print('Done.')  # Bunu çalıştırmaz

# In[]:
# ========================
# Kümeler
soc_set = {"Twitter", "Facebook", "Instagram", "Quora"}

for platform in soc_set:
    print(platform, end=" ")
    
# In[]:
# ========================
# Tuples/Demetler
footballers_tuple = ("Ronaldo", "Mendy", "Lukaku", "Lampard", "Messi", "Pogba")

for footballer in footballers_tuple:
    print(footballer, end=" ")

# In[]:
# ========================
# Dictionary/Sözlükler

fcc_dict = {"name": "freeCodeCamp",
           "type": "non-profit", 
           "mode": "remote", 
           "paid": "no"}

for key in fcc_dict:
    print(key, end=" ")

# In[]:
# ========================
# Range    

sayı = range(1, 10)

for i in sayı:
    print(i, end="")

# In[]:
# ========================    
for i in range(1, 10):
    print(i, end="")    

# In[]:
# ========================

# x = int(input("Bir sayı giriniz: "))
# cvp = 0
# itersLeft = abs(x)
# while (itersLeft != 0):
#     cvp = cvp + abs(x)
#     itersLeft = itersLeft - 1
# print(str(x) + '*' + str(x) + ' = ' + str(cvp))

# Girilen sayi negatif ise? abs(x) kullanılır

# ========================
# 2. Girilen bir mükemmel küpün, küp kökünün alınması    

# x = int(input('Bir tamsayı giriniz: '))
# cvp = 0
# while cvp**3 < abs(x):
#     cvp = cvp + 1
# if cvp**3 != abs(x):
#     print(x, 'bir mükemmel küp değildir')
# else:
#     if x < 0:
#         cvp = -cvp
#     print('Küp kök', x,':', cvp)

# Şunu dene 1957816251
# Şunu da dene 7406961012236344616

# ========================
# 3. Parola belirleme 

# for i in range(3):
#     parola = input("parola belirleyin: ")
#     if not parola:
#         print("parola bölümü boş geçilemez!")

#     elif len(parola) in range(3, 8):
#         print("Yeni parolanız", parola)
#         break

#     elif i == 2:
#         print("parolayı 3 kez yanlış girdiniz.",
#         "Lütfen 30 dakika sonra tekrar deneyin!")

#     else:
#         print("parola 8 karakterden uzun 3 karakterden kısa olmamalı")

# ========================
# 4. Tahmin oyunu 

# from random import randint
 
# rand=randint(1, 100)
# sayac=0
 
# while True:
#     sayac+=1
#     sayi=int(input("1 ile 100 arasında değer girin (0 çıkış):"))
#     if(sayi==0):
#         print("Oyunu İptal Ettiniz")
#         break
#     elif sayi < rand:
#         print("Daha Yüksek Bir Sayı Girin.")
#         continue
#     elif sayi > rand:
#         print("Daha Düşük Bir Sayı Girin.")
#         continue
#     else:
#         print("Rastele seçilen sayı {0}!".format(rand))
#         print("Tahmin sayınız {0}".format(sayac))

# ========================
# 5. Taş, kağıt, makas oyunu 

# import random          # random kütüphanesi çagırılır

# oyuncu = input("Seç (taş. kağıt ya da makas): ")
# bilgisayar = random.choice(['taş','kağıt','makas'])

# print()

# print('Kullanıcı (Sen) şunu seçtin :', oyuncu)
#     # print()

# if oyuncu == 'taş':
#     print('Bilgisayar (Ben) şunu seçtim :', bilgisayar)
#     print()
#     if bilgisayar == 'kağıt':
#         print('Ha! Kağıt seçtim ve Ben kazandım!')
#     if bilgisayar == 'makas':
#         print('Kahretsin! Makas seçtim ve Sen kazandın!')

# if oyuncu == 'kağıt':
#     print('Bilgisayar (Ben) şunu seçtim :', bilgisayar)
#     print()
#     if bilgisayar == 'taş':
#         print('Ha! Makas seçtim ve Ben kazandım!')
#     if bilgisayar == 'makas':
#         print('Kahretsin! Taş seçtim ve Sen kazandın!')

# if oyuncu == 'makas':
#     print('Bilgisayar (Ben) şunu seçtim :', bilgisayar)
#     print()
#     if bilgisayar == 'taş':
#         print('Ha! Taş seçtim ve Ben kazandım!')
#     if bilgisayar == 'kağıt':
#         print('Kahretsin! Kağıt seçtim ve Sen kazandın!')
   
# if oyuncu == bilgisayar:
#     print("Beraberlik, sonrakine bol şans...")

# ========================
# Çalışma Soruları
# ========================
# 1. Ödev verilecek

# ========================
# Gecen haftaki örnekler
# ========================
# 1. Dikdörtgenin alanını ve çevresini hesaplayan programı yazınız, 4.9 
# genişlik ve 7.5 uzunluk için bu değerlerin sonuçlarını ekrana yazdırınız.

# k=input("Kısa kenarı giriniz: ") 
# u=input("Uzun kenarı giriniz: ") 
# a=int(k)*int(u); print(a);

# ========================
# 2. Aşağıdaki ekran çıktısını veren programı yazınız.
# """ Enter number x: 2
#     Enter number y: 3
#     x**y = 8
#     log(x) = 1 # log2 de
# """
# import math
# x = float(input("x'i giriniz: "))
# y = float(input("y'i giriniz: "))
# print("x**y nin cevabı" ,x**y)
# print("log2 tabanında değeri : " ,math.log2(x))   

# ========================
# 3. Girilen bir sayısının 2 veya 3 ile bölünebilmesi    

# x = int(input("Bir sayı gir:"))

# if x%2 == 0:
#     if x%3 == 0:
#         print("2 ve 3'e bölünebilir")
#     else:
#         print("2'ye bölünebilir ama 3'e bölünemez")
# elif x%3 == 0:
#     print("3'e bölünebilir ama 2'ye bölünemez")
# else: 
#     print("Ne 2'ye ne de 3'e bölünebilir")

# ========================
# 4. ax^2 + bx + c = 0 ikinci derece denklemini çözdürün ve ekrana yazdırın.
# Not: a, b ve c input olarak kullanıcı tarafından girilir.

# import math

# a = int(input("a'yı gir': "))
# b = int(input("b'yi gir': "))
# c = int(input("c'yi gir': "))

# discriminant = (b * b) - (4 * a * c)

# if discriminant > 0:
#     sqrt_discriminant = math.sqrt(discriminant)
#     x1 = float(-b + sqrt_discriminant) / (2 * a)
#     x2 = float(-b - sqrt_discriminant) / (2 * a)
#     print("İki kökü mevcut")
#     print("Kök(ler): {0:.2f} ".format(x1)+ "{0:.2f}".format(x2))

# elif discriminant == 0:
#     x1 = float(-b) / (2 * a)
#     print("Bir kökü mevcut")
#     print("Kök: {0:.2f}".format(x1))
# else:
#     print("Bir kök mevcut değil")

# ========================
# 5. ABD seçimlerinde aday olup olamayacağınızı belirleryen programı yazınız.
# Amerikan Başkanligi için adaylık kriterleri:
# 1. 35 yaşından büyük olmak 
# 2. ABD vatandaşı olmak
# 3. 14 yıldır ABD'de yaşıyor olmak
# Kullanıcıya bu üç soruyu sorun ve cevaplarına göre ekrana başkanlık adayı 
# olup olamayacağını yazdırın.

# yaş = int(input("Lütfen yaşınızı giriniz:"))
# vatandaş = input("Bir Amerikan vatandaşı mısınız (evet/hayır)?")
# yıl = int(input("Kaç yıldır Amerika'da yaşıyorsunuz?"))

# elverişli = True
# if yaş < 35:
#     elverişli = False

# if vatandaş !="evet":
#     elverişli = False

# if yıl < 14:
#     elverişli = False

# if elverişli:
#     print("Başkanlık için yarışabilirsin!")

# else :
#     print("Başkanlı yarışı için elverişli değilsin!")