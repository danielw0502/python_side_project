# _*_ coding: utf-8 -*-
import re
import xlwt

file_read = open('test.txt')
workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet('Test')
row = 0

while 1:
    line = file_read.readline().strip()
#    print line
    if not line:
        workbook.save('test.xls')
        break
    pattern = re.compile(r'.(\d+).*"(.*)".(\d+).(\d+).(\d+)')
    a = re.match(pattern,line)
    if a:
        worksheet.write(row,0,a.group(1))
        worksheet.write(row,1,a.group(2))
        worksheet.write(row,2,a.group(3))
        worksheet.write(row,3,a.group(4))
        worksheet.write(row,4,a.group(5))
        row += 1
