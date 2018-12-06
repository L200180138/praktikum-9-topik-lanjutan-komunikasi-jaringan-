###Kegiatan 1. Data diri server (client)
##
##import socket
##
##hostname = 'localhost'
##client = ''
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((hostname, 50009))
##print "Program komunikasi tentang diri anda "
##while client.lower() != 'keluar' :
##    client = raw_input( 'Perintah: ')
##    s.send(client)
##    if client.lower() != 'keluar' :
##        response = s.recv(1024)
##        print "Jawab: " , response
##    else :
##       print 'Jawab : Siap!!'
##s.close()

###Kegiatan 2. Informasi data diri(client)
##
##import socket
##import platform
##hostname = 'localhost'
##client = ''
##s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##s.connect((hostname, 50008))
##print "Program komunikasi tentang diri anda "
##while client.lower() != 'quit' :
##    client = raw_input( 'Command: ')
##    s.send(client)
##    if client.lower() != 'quit' :
##        response = s.recv(1024)
##        print "jawab: " , response
##    else :
##        print 'Jawab: Siap!!'
##s.close()


#Kegiatan 3. Server yang menghitung luas bangun geometri
import socket

hostname = 'localhost'
client = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hostname, 50008))
print "Menghitung Luas Bangun Persegi "
while client.lower() != 'keluar' :
    client = raw_input( 'Pesan: ')
    s.send(client)
    if client.lower() != 'keluar' :
        response = s.recv(1024)
        print "Respon: " , response
    else :
        print 'Respon: -'
s.close()


