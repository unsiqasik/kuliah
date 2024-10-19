print('Masukan Kode (4 Angka)')
kode = int(input('Kode = '))

while kode != 2112:
  kode = int(input('Kode Salah. Masukan Kode Lagi: '))
if kode == 2112:
  print ('Kode Benar. Lanjutkan')
q1 = str(input('3 + 1 = '))

if q1 == 4:
  print ('benar')
else:
  print ('Salah')

q2 = int(input('2 + 1 = '))

if q2 == 3:
  print ('Benar')
else:
  print ('Salah')
