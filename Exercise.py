Q:1) extract 5th row and 4th column from the end and add 2 to it.

x[4]
x[4].split(',')[-4]
int(x[4].split(',')[-4])+2
test = int(x[4].split(',')[-4])+2
f1 = open("/Users/akshata/test.file","w")
f1.write(str(int(x[4].split(',')[-4])+2))
f1.close()


Q:2) imported the file from s3,using postman and get the last 2nd row and put that in a file. 
response.text
'Lem,Boissier,lboissier@sf_tuts.com,3002 Ruskin Trail,ShikÄ\x81rpur,
Iain,Hanks,ihanks1@sf_tuts.com,2 Pankratz Hill,Monte-Carlo,
Avo,Laudham,alaudham2@sf_tuts.com,6948 Debs Park,PraÅ¼mÃ³w,
Emili,Cornner,ecornner3@sf_tuts.com,177 Magdeline Avenue,NorrkÃ¶ping,
Harrietta,Goolding,hgoolding4@sf_tuts.com,450 Heath Trail,Osielsko,11/27/2017'

abc = response.text

abc.split('\n')[-2]

f1=open("/Users/akshata/test03","w")

Q=abc.split('\n')[-2]

f1.write(Q)




Q:3) import datetime and find the current date and time using this library.

import datetime
datetime_object = datetime.datetime.now()
print(datetime_object)

date_object = datetime.date.today()
print(date_object)


d = datetime.date(2019, 4, 12)
print(d)

print(dir(datetime))

