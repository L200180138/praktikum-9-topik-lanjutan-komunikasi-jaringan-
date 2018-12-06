#Kegiatan 1. Data diri dari server
##
##import socket
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.bind(("", 50009))
##s.listen (5)
##print "Program komunikasi tentang diri anda"
##data = ''
##kamus = {'nama' : 'karina muslimah',
##         'NIM' : 'L200180138',
##         'keluar' : ' Siapp !!!' }
##while data.lower() != 'keluar' :
##    komm, addr = s.accept()
##    while data.lower () != 'keluar' :
##        data = komm.recv(1024)
##        if data.lower() == 'keluar' :
##            s.close()
##            break
##        print 'perintah: ', data
##        if kamus.has_key(data) :
##            komm.send(kamus[data])
##        else :
##            komm.send('Maaf, perintah tidak dimengerti')


###Kegiatan 2. Informasi tentang server
##
##import socket
##import platform
##s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
##s.bind(("", 50008))
##s.listen (5)
##print "Program komunikasi tentang diri anda"
##baba = ''
##masukan = {'machine' : platform.machine(),
##         'release' : platform.release(),
##         'system' : platform.system(),
##         'version' : platform.version(),
##         'node'    : platform.node(),
##         'quit' : ' Siapp !!!' }
##while baba.lower() != 'quit' :
##    komm, addr = s.accept()
##    while baba.lower () != 'quit' :
##        baba = komm.recv(1024)
##        if baba.lower() == 'quit' :
##            s.close()
##            break
##        print 'Command: ', baba
##        if masukan.has_key(baba) :
##            komm.send(masukan[baba])
##        else :
##            komm.send('unknown command')

#Kegiatan 3. Server menghitung luas bangun geometri

            
import socket
import platform
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind(("", 50008))
s.listen(5)
print "server penjawab otomatis sudah siap"
data= ''
angkaHitung = 0
# komm, addr = s.accept()
# data = komm.recv(1024)

# kamus = {'parameter1=' : platform.machine(),
#          'hitung' : 
#          'quit' : ' Siapp !!!' }


def hitung(a):
    return a*a


while data.lower() != 'quit' :
    komm, addr = s.accept()
    data = komm.recv(1024)
    print 'Command: ', data
    if data[0:11].lower() == 'parameter1=':
            angkaHitung = int(data[11:])
            if angkaHitung != 0:
                komm.send("Parameter di catat")
    else:
        komm.send('unknown command')
    data = komm.recv(1024)
    if data.lower() == 'hitung':
        hasil = hitung(angkaHitung)
        hasil = str(hasil)
        komm.send("Hasil persegi dari sisi "+str(angkaHitung)+" adalah "+hasil)
    else:
        komm.send('unknown command')
    if data.lower() == 'keluar':
        s.close()
        break
