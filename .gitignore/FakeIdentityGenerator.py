import random
import time
import sys
import os
import names
import pycountry

os.system('clear')
def cardgenerator():
    mmdic = ['01','02','03','04','05','06','07','08','09','10','11','12']
    binn = random.randint(400000,499999)
    mm = random.choice(mmdic)
    yy = random.randint(2019,2026)
    geneccv = random.randint(100,999)
    genenum = random.randint(1000000000,9999999999)
    creditcard = (binn,genenum)
    creditcardstr = "%s%s"%(creditcard)
    all = creditcardstr,"|",mm,"|",yy,"|",geneccv
    allstring = "%s%s%s%s%s%s%s"%(all)
    print allstring

rname = names.get_first_name()
rlastname = names.get_last_name()
gmails = ["gmail.com","mail.ru","live.fr","yahoo.com"]
gmail = random.choice(gmails)
num = random.randint(1900,2018)
n = ("Name : ",rname)
name = "%s%s"%(n)
l = ("LastName : ",rlastname)
lname = "%s%s"%(l)
allg = (name,num,"@",gmail)
all = "%s%s%s%s"%(allg)

cdic =['AF','AL','DZ','AS','AD','AO','AI','AQ','AG','AR','AM','AW','AU','AT','AZ','BS','BH','BD','BB','BY','BE','BZ','BJ','BM','BT','BO','BA','BW','BR']

rc = random.choice(cdic) 
country = pycountry.countries.get(alpha_2=rc)
ncountry = "Country : ",country.name
ccountry = "%s%s"%(ncountry)
cardi = "Card Number/mm/yy/cc : "
card = "%s"%(cardi)

time.sleep(2)
print """
+=========================+=========================+
|              Coded By AbdXSlayer69                |
|            E-mail: As8apple@gmail.com             |
+=========================+=========================+"""
time.sleep(1)
print "============================"
print name
time.sleep(0.5)
print "============================"
print lname
time.sleep(0.5)
print "============================"
print all
time.sleep(0.5)
print "============================"
print ccountry
time.sleep(0.5)
print "============================"
print card
cardgenerator()
print "============================"
