import json

countrys_file_name = u"D:\\countries.json"
file_name = u"D:\\country.txt"
countrys_name_code = u"D:\\countries_name_code.json"

if __name__ == '__main__':
    with open(file_name, "r", encoding='UTF-8') as file:
        lines = file.readlines()

    with open(countrys_file_name, "r", encoding='UTF-8') as load_file:
        country_dict = json.load(load_file)
        for i in range(len(country_dict)):
            letter_group = country_dict[i]["name"]
            country_list = country_dict[i]["countries"]
            for j in range(len(country_list)):
                country_name = country_list[j]["name"]

                for line in lines:
                    if (country_name in line):
                        country_infos = line.split()
                        code = country_infos[1]
                        country_list[j]["code"] = code
                        print(country_list[j])

        with open(countrys_name_code, "w", encoding='UTF-8') as dump_f:
            json.dump(country_dict, dump_f, ensure_ascii=False)
