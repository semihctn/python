# maası 3000'den yüksek olanlara %10 3000'den az olanlara %20 zam   
maas=[5000,4000,3000,5200,2400,3600,1000,800]
yeni_maas=[]
for i in maas:
    if i<3000:
        i=i*1.2
        yeni_maas.append(i)
        print(i)
    else:
        i=i*1.1
        yeni_maas.append(i)
        print(i)
print(yeni_maas)
        
    