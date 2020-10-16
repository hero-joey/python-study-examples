# -*- coding: utf-8 -*-if __name__ == '__main__':
file_name = u"D:\\province.txt"
with open(file_name,'r', encoding='UTF-8') as f:
    for line in f:
        line = line.strip()
        if (line == "\n" or line == ""):
            continue

        #print(line)
        contents = line.split("（")
        province = contents[0]
        code_contents = contents[1].split()
        code = code_contents[0]
        short_name_contents = code_contents[1].split("）")
        short_name = short_name_contents[0]

        sql = format(u"insert into tb_region_province values(%s%s%s, %s%s%s, %s%s%s)%s" % ('''"''', code,'''"''','''"''', province,'''"''','''"''', short_name,'''"''', ''';'''))
        print(sql)


