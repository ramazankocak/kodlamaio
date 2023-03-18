students =[]

def ogr():
    nameSurname = input("\nÖğrenci Adı Soyadı\n(Çıkış için sıfır girin):")
    return nameSurname.title()

def add(ogrenci):
    students.append(ogrenci)

def multiDel(sil):
    if len(sil) != 0:
        for i in sil:
            if i in students:
                students.remove(i)
            else:
                print(f"Öğrenci listesinde {i} yok.")
        print("Silme işlemi tamamlanmıştır.")
    else:
        print("İşlem sonlandırılmıştır.")

def view(liste):
    for i in liste:
        print(i)

def search(isim):
    if isim in students:
        return print("Aradığınız öğrencinin numarası: ",students.index(isim))
    else:
        return print("Aradığınız öğrenci bulunmadı.")

while True:
    print("\nÖğrenci ekelemek için 1'e, Öğrenci silmek için 2'ye, öğrencileri listelemek için 3'e, Öğrenci numarasını öğrenmek için 4'e, Çoklu silmek için 5'e, Çıkış için 6'e basınız:\n")
    try:
        secim = int(input("İşlem: "))
        if secim == 1:
            while True:
                x = ogr()
                if x == "0":
                    break
                else:
                    add(x)
        elif secim == 2:
            adSoyadSil = input("Silinecek öğrencinin Adı Soyadı: ").title()
            for i in students:
                if adSoyadSil == i:
                    students.remove(adSoyadSil)
                else:
                    print("Girdiğiniz isim ve soyisim bulunamadı...")
        elif secim == 3:
            if len(students) == 0:
                print("Öğrenci listesi boş...")
            else:
                view(students)
        elif secim == 4:
            adSoyad = input("Numarasını öğrenmek istediğiniz öğrencinin Adı Soyadı: ").title()
            no = search(adSoyad)

        elif secim == 5:
            liste =[]
            while True:
                adSoyad = input("Silinecek öğrencilerin Ad Soyad bilgilerini giriniz (silme işlemini başlatmak için 9 giriniz):").title()
                if adSoyad != "9":
                    liste.append(adSoyad)
                else:
                    break
            multiDel(liste)
            
        elif secim == 6:
            print("Program Sonlandırıldı.")
            break
        else:
            print("...!Hatalı giriş yaptınız!...")
    except:
        print("...!Hatalı giriş yaptınız!...")
