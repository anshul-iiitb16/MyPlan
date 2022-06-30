# Writing to an excel 
# sheet using Python
import xlwt
import xlrd
import numpy as np
import random

wb1 = xlrd.open_workbook("Final.xlsx")
sheet1 = wb1.sheet_by_index(0)

lst_of_Phone_no = []
date_list = np.arange('2019-01', '2019-04', dtype='datetime64[D]')


Social_Media_Sites = []
Browsing_Sites = []
Email_Sites = []
E_Commerce_Sites = []
Education_Sites = []
Random_Sites = []

Bytes_Upload = []
Bytes_Download = []

day_list = []
site_list = []
phn_list = []


Social_Media_users = []
Email_users = []
Browsing_users = []
Education_users = []
E_Commerce_users = []
Random_users = []


for i in range(1, sheet1.nrows):
    lst_of_Phone_no.append(sheet1.cell_value(i, 0))

for i in range(1, 15):
    Social_Media_Sites.append(sheet1.cell_value(i, 1))

for i in range(1, 7):
    Browsing_Sites.append(sheet1.cell_value(i, 2))

for i in range(1, 8):
    Email_Sites.append(sheet1.cell_value(i, 3))

for i in range(1, 8):
    E_Commerce_Sites.append(sheet1.cell_value(i, 4))

for i in range(1, 7):
    Education_Sites.append(sheet1.cell_value(i, 5))

for i in range(1, 7):
    Random_Sites.append(sheet1.cell_value(i, 6))


# for i in range(91):
#     date_list.append(sheet1.cell_value(i, 1))

random.shuffle(Social_Media_Sites)
random.shuffle(Browsing_Sites)
random.shuffle(Email_Sites)
random.shuffle(E_Commerce_Sites)
random.shuffle(Education_Sites)
random.shuffle(Random_Sites)


for j in range(0, 44):
    Social_Media_users.append(lst_of_Phone_no[j])
for j in range(44, 62):
    Email_users.append(lst_of_Phone_no[j])
for j in range(62, 97):
    Browsing_users.append(lst_of_Phone_no[j])
for j in range(97, 112):
    Education_users.append(lst_of_Phone_no[j])
for j in range(112, 166):
    E_Commerce_users.append(lst_of_Phone_no[j])
for j in range(166, 170):
    Random_users.append(lst_of_Phone_no[j])



All_Sites = Social_Media_Sites + Browsing_Sites + Email_Sites + E_Commerce_Sites + Education_Sites + Random_Sites
temp = All_Sites
Percentage_SM = []

for i in Social_Media_users:
    Total = 0
    count = 0

    s = random.randint(1, 10)
    for l in Social_Media_Sites[:]:
        if l in temp:
            temp.remove(l)

    for j in date_list:
        n = random.randint(0, 14)

        random.shuffle(Social_Media_Sites)
        for k in range(n):
            Total = Total + 1
            day_list.append(j)
            phn_list.append(i)

            num1 = random.randint(2, s+5)
            num = random.randint(1, num1)

            if num == 1:
                site_list.append(temp[0])
                random.shuffle(temp)
                Bytes_Upload.append(random.random()*1000)
                Bytes_Download.append(random.random()*1000)

            else:
                site_list.append(Social_Media_Sites[k])
                count = count + 1
                Bytes_Upload.append(random.random() * 10000)
                Bytes_Download.append(random.random() * 10000)

    Percentage_SM.append((count/Total)*100)




All_Sites = Social_Media_Sites + Browsing_Sites + Email_Sites + E_Commerce_Sites + Education_Sites + Random_Sites
temp = All_Sites
Percentage_Email = []

for i in Email_users:
    Total = 0
    count = 0

    s = random.randint(1, 4)
    for l in Email_Sites[:]:
        if l in temp:
            temp.remove(l)

    for j in date_list:
        n = random.randint(0, 7)

        random.shuffle(Email_Sites)
        for k in range(n):
            Total = Total + 1
            day_list.append(j)
            phn_list.append(i)

            # num1 = random.randint()
            num = random.randint(1, 3)

            if num == 1:
                site_list.append(temp[0])
                random.shuffle(temp)
                Bytes_Upload.append(random.random() * 1000)
                Bytes_Download.append(random.random() * 1000)

            else:
                site_list.append(Email_Sites[k])
                count = count + 1
                Bytes_Upload.append(random.random() * 10000)
                Bytes_Download.append(random.random() * 10000)

    Percentage_Email.append((count/Total)*100)

All_Sites = Social_Media_Sites + Browsing_Sites + Email_Sites + E_Commerce_Sites + Education_Sites + Random_Sites
temp = All_Sites
Percentage_Browse = []

for i in Browsing_users:
    Total = 0
    count = 0

    s = random.randint(1, 10)
    for l in Browsing_Sites[:]:
        if l in temp:
            temp.remove(l)

    for j in date_list:
        n = random.randint(0, 6)

        random.shuffle(Browsing_Sites)
        for k in range(n):
            Total = Total + 1
            day_list.append(j)
            phn_list.append(i)

            num1 = random.randint(2, 2)
            num = random.randint(1, num1)

            if num == 1:
                site_list.append(temp[0])
                random.shuffle(temp)
                Bytes_Upload.append(random.random() * 1000)
                Bytes_Download.append(random.random() * 1000)

            else:
                site_list.append(Browsing_Sites[k])
                count = count + 1
                Bytes_Upload.append(random.random() * 10000)
                Bytes_Download.append(random.random() * 10000)

    Percentage_Browse.append((count/Total)*100)

All_Sites = Social_Media_Sites + Browsing_Sites + Email_Sites + E_Commerce_Sites + Education_Sites + Random_Sites
temp = All_Sites
Percentage_ECom = []

for i in E_Commerce_users:
    Total = 0
    count = 0

    s = random.randint(1, 3)
    for l in E_Commerce_Sites[:]:
        if l in temp:
            temp.remove(l)

    for j in date_list:
        n = random.randint(0, 7)

        random.shuffle(E_Commerce_Sites)
        for k in range(n):
            Total = Total + 1
            day_list.append(j)
            phn_list.append(i)

            num1 = random.randint(3, s+2)
            num = random.randint(1, num1)

            if num == 1:
                site_list.append(temp[0])
                random.shuffle(temp)
                Bytes_Upload.append(random.random() * 1000)
                Bytes_Download.append(random.random() * 1000)

            else:
                site_list.append(E_Commerce_Sites[k])
                count = count + 1
                Bytes_Upload.append(random.random() * 10000)
                Bytes_Download.append(random.random() * 10000)

    Percentage_ECom.append((count/Total)*100)

All_Sites = Social_Media_Sites + Browsing_Sites + Email_Sites + E_Commerce_Sites + Education_Sites + Random_Sites
temp = All_Sites
Percentage_Edu = []

for i in Education_users:
    Total = 0
    count = 0

    s = random.randint(1, 80)
    for l in Education_Sites[:]:
        if l in temp:
            temp.remove(l)

    for j in date_list:
        n = random.randint(0, 6)

        random.shuffle(Education_Sites)
        for k in range(n):
            Total = Total + 1
            day_list.append(j)
            phn_list.append(i)

            num1 = random.randint(2, s+5)
            num = random.randint(1, num1)

            if num == 1:
                site_list.append(temp[0])
                random.shuffle(temp)
                Bytes_Upload.append(random.random() * 1000)
                Bytes_Download.append(random.random() * 1000)

            else:
                site_list.append(Education_Sites[k])
                count = count + 1
                Bytes_Upload.append(random.random() * 10000)
                Bytes_Download.append(random.random() * 10000)

    Percentage_Edu.append((count/Total)*100)


for i in Random_users:
    Total = 0
    count = 0
    for j in date_list:
        n = random.randint(0, 6)

        random.shuffle(Random_Sites)
        for k in range(n):
            Total = Total + 1
            day_list.append(j)
            phn_list.append(i)
            site_list.append(Random_Sites[k])

            Bytes_Upload.append(random.random() * 10000)
            Bytes_Download.append(random.random() * 10000)


from xlwt import Workbook

# Workbook is created
wb2 = Workbook()
wb3 = Workbook()
# add_sheet is used to create sheet.
sheet2 = wb2.add_sheet('Sheet 1')
sheet3 = wb3.add_sheet('Sheet 1')

sheet2.write(0,0,'Phone Number')
sheet2.write(0,1,'Date')
sheet2.write(0,2,'Domain Name')
sheet2.write(0,3,'Bytes Upload')
sheet2.write(0,4,'Bytes Download')
for i in range(len(day_list)):
    sheet2.write(i + 1, 0, phn_list[i])
    sheet2.write(i+1, 1, str(day_list[i]))
    sheet2.write(i+1, 2, site_list[i])
    sheet2.write(i + 1, 3, str(Bytes_Upload[i]))
    sheet2.write(i + 1, 4, str(Bytes_Download[i]))

write_pointer = 0
ptr = 0
sheet3.write(0,0,'Phone Number')
sheet3.write(0,1,'Percentage of Social Media Sites Opened')
for i in range(len(Percentage_SM)):
    sheet3.write(i + 1, 0, lst_of_Phone_no[ptr])
    ptr = ptr + 1
    sheet3.write(i+1, 1, Percentage_SM[i])

write_pointer = write_pointer + 3
sheet3.write(0,3,'Phone Number')
sheet3.write(0,4,'Percentage of Email Sites Opened')
for i in range(len(Percentage_Email)):
    sheet3.write(i+1, 3, lst_of_Phone_no[ptr])
    ptr = ptr + 1
    sheet3.write(i+1, 4, Percentage_Email[i])

write_pointer = write_pointer + 3
sheet3.write(0,6,'Phone Number')
sheet3.write(0,7,'Percentage of Browsing Sites Opened')
for i in range(len(Percentage_Browse)):
    sheet3.write(i+1, 6, lst_of_Phone_no[ptr])
    ptr = ptr + 1
    sheet3.write(i+1, 7, Percentage_Browse[i])

write_pointer = write_pointer + 3
sheet3.write(0,9,'Phone Number')
sheet3.write(0,10,'Percentage of ECom Sites Opened')
for i in range(len(Percentage_ECom)):
    sheet3.write(i+1, 9, lst_of_Phone_no[ptr])
    ptr = ptr + 1
    sheet3.write(i+1, 10, Percentage_ECom[i])

write_pointer = write_pointer + 3
sheet3.write(0,12,'Phone Number')
sheet3.write(0,13,'Percentage of Education Sites Opened')
for i in range(len(Percentage_Edu)):
    sheet3.write(i+1, 12, lst_of_Phone_no[ptr])
    ptr = ptr + 1
    sheet3.write(i+1, 13, Percentage_Edu[i])

write_pointer = write_pointer + 3
sheet3.write(0,15,'Phone Number')
sheet3.write(0,16,'Percentage of Random Sites Opened')
for i in range(4):
    sheet3.write(i+1, 15, lst_of_Phone_no[ptr])
    sheet3.write(i+1, 16, '--')
    ptr = ptr + 1


wb2.save('UDR_Final.xlsx')
wb3.save('Analysis.xlsx')

