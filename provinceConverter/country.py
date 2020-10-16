# -*- coding: utf-8 -*-if __name__ == '__main__':
import json
file_name = u"D:\\country.txt"
file_name = u"D:\\country.txt"
country_file_name = open(u"D:\\country_file.txt", "w")
with open(file_name, 'r', encoding='UTF-8') as f:
    for line in f:
        line = line.strip()
        if (line == "\n" or line == ""):
            continue

        #print(line)
        contents = line.split()
        id = contents[1]
        name = contents[2]
        short_name = contents[0]

        #sql = format(u"insert into tb_region_country values(%s%s%s, %s%s%s, %s%s%s)%s" % ('''"''', id,'''"''','''"''', name,'''"''','''"''', short_name,'''"''', ''';'''))
        country_record = format("%s %s %s" % (id, name, short_name))
        print(country_record, file=country_file_name)


