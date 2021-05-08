#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os

os.system("figlet Quick Scanner")
print("""

Hedefinizi Giriniz.

""")

hedef = raw_input("Hedef Domain Ya Da IP: ")

os.system("clear")
os.system("figlet Quick Scanner")




	
print(""""
	
	Yapmak istediğiniz işlemin seçiniz
	
	1-)Normal Tarama
	
	2-)Hızlı Tarama
	
	3-)İşletim Sistemi Algılama
	
	4-)Agresif Tarama
	
	5-)Servis Sürüm Taraması
	
	6-)Dmitry
	
	
	""")
	
	
secim2 = raw_input("Seçiminiz: ")
	
	
	
if(secim2=="1"):
	
	os.system("nmap " + hedef)
	
	
elif(secim2=="2"):
	     
	os.system("nmap -F -sS -sV " + hedef)
	
	
elif(secim2=="3"):
		
		os.system("nmap -O " + hedef)
		
		
elif(secim2=="4"):

	    os.system("nmap -A " + hedef)
	    
	    
elif(secim2=="5"):
	
	    os.system("nmap -sS -sV " + hedef)

	
if(secim2=="6"):


    os.system("dmitry -winsen " + hedef)



else:

    print("Hatalı Tuşlama Yaptınız")









