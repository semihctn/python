#magaza adi, magaza geliri verilecek. Gelire göre ekstra promosyon sağlanacak

magaza_adi=input("Magazanizin ismini giriniz: ")
magaza_gelir=float(input("Magazanizin aylik gelirini giriniz:"))
sinir=40000
if magaza_gelir<sinir:
    print(magaza_adi + " firması olarak sinirin altinda kaldiniz. Promosyon kazanamadiniz")
elif magaza_gelir>sinir:
    print(magaza_adi + " firmasi olarak siniri gectiniz. Tebrikler %10 promosyon kazandiniz.\nKazandiginiz promosyon miktarı :" + str(int(magaza_gelir*.1)) + "\nYeni geliriniz=" + str(int(magaza_gelir*1.1)))
else:
    print(magaza_adi + " sfirmasi olarak tam sinirda kaldiniz. Siki çalismaya devam.")