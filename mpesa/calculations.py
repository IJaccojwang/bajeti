import tabula
import csv



def convert(conversionfile):
    tabula.convert_into('.'+ conversionfile, "./media/statements/output.csv", pages='2', output_format="csv")

    with open('./media/statements/output.csv') as in_file:
        reader = csv.reader(in_file)
        result = [[item for item in row if item != ''] for row in reader]

        for i in result:
            if len(i)==1:
                result.remove(i)
    with open('./media/statements/final.csv', 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(result)

    writeFile.close()


received = 0
sent = 0
deposited = 0
withdrawn = 0
paybill = 0
buy_goods = 0
others = 0

withdrawals = 0
withdrawn2 = 0
charges_w = 0

payments = 0
paid = 0
charges_p = 0

airbuy = 0
airtime = 0
foodbuy = 0
food = 0
supbuy = 0
sup = 0
uncatbuy = 0
uncat = 0

with open('./media/statements/final.csv') as f:
    reader = csv.reader(f)
    listed = list(reader)
    sent = abs(float((listed[1][2].replace(',', ''))))
    received = abs(float((listed[2][1].replace(',', ''))))
    deposited = abs(float((listed[3][1].replace(',', ''))))
    withdrawn = abs(float((listed[4][2].replace(',', ''))))
    paybill = abs(float((listed[5][2].replace(',', ''))))
    buy_goods = abs(float((listed[6][2].replace(',', ''))))
    others = abs(float((listed[7][2].replace(',', ''))))

with open('./media/statements/final.csv') as f:
    reader2 = csv.reader(f)
    listed2 = list(reader2)
    number2 = listed2[4][2]
    withdrawn2 = float(number2.replace(',', ''))
    
for i in range(len(listed)):
    if listed[i][2]=='Withdrawal Charge':
        withdrawals += 1
        charges_w += abs(float((listed2[i][4].replace(',', '')))) 



with open('./media/statements/final.csv') as f:
    reader3 = csv.reader(f)
    listed3 = list(reader3)
    paid = abs(float((listed3[5][2].replace(',', ''))))

for i in range(len(listed)):
    if listed3[i][2]=='Pay Bill Charge':
        payments += 1
        charges_p += abs(float((listed3[i][4].replace(',', '')))) 



with open('./media/statements/final.csv') as f:
        reader4 = csv.reader(f)
        listed4 = list(reader4)

for i in range(len(listed)):
    if listed[i][2]=='Airtime Purchase' :
        airbuy += 1
        airtime += abs(float((listed[i][4].replace(',', ''))))
    elif listed[i][2]=='Merchant Payment to 131053 - LIPET ENTERPRISES' or listed[i][2]=='KFC Mama Ngina':
        foodbuy += 1
        food += abs(float((listed[i][4].replace(',', ''))))
    elif listed[i][2]=='Merchant Payment to 947792 - PRIZEWORTHY':
        supbuy += 1
        sup += abs(float((listed[i][4].replace(',', ''))))

 

    

# def withdrawal_c():
#     withdrawals = 0
#     withdrawn2 = 0
#     charges_w = 0
    
#     with open('./media/statements/final.csv') as f:
#         reader2 = csv.reader(f)
#         listed2 = list(reader)
#         number2 = listed[4][2]
#         withdrawn2 = float(number2.replace(',', ''))
        
#     for i in range(len(listed)):
#         if listed[i][2]=='Withdrawal Charge':
#             withdrawals += 1
#             charges_w += abs(float((listed[i][4].replace(',', '')))) 




# def paybill_c():
#     payments = 0
#     paid = 0
#     charges_p = 0

#     with open('./media/statements/final.csv') as f:
#         reader3 = csv.reader(f)
#         listed3 = list(reader)
#         paid = abs(float((listed[5][2].replace(',', ''))))
    
#     for i in range(len(listed)):
#         if listed[i][2]=='Pay Bill Charge':
#             payments += 1
#             charges_p += abs(float((listed[i][4].replace(',', '')))) 



# def usage():
#     airbuy = 0
#     airtime = 0
#     foodbuy = 0
#     food = 0
#     supbuy = 0
#     sup = 0
#     uncatbuy = 0
#     uncat = 0

#     with open('./media/statements/final.csv') as f:
#         reader4 = csv.reader(f)
#         listed4 = list(reader4)

#     for i in range(len(listed)):
#         if listed[i][2]=='Airtime Purchase' :
#             airbuy += 1
#             airtime += abs(float((listed[i][4].replace(',', ''))))
#         elif listed[i][2]=='Merchant Payment to 131053 - LIPET ENTERPRISES' or listed[i][2]=='KFC Mama Ngina':
#             foodbuy += 1
#             food += abs(float((listed[i][4].replace(',', ''))))
#         elif listed[i][2]=='Merchant Payment to 947792 - PRIZEWORTHY':
#             supbuy += 1
#             sup += abs(float((listed[i][4].replace(',', ''))))

