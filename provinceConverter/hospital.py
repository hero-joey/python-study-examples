import json

if __name__ == '__main__':
    hospital_file = u"D:\\hospital.json"
    new_hospital_file = u"D:\\hospital_list.json"
    new_hospital_dict = {}
    new_hospital_list = []
    with open(hospital_file, "r", encoding='UTF-8') as load_file:
        hospital_dict = json.load(load_file)
        hospital_list = hospital_dict["hospital"]
        for i in range(len(hospital_list)):
            hospital_id = hospital_list[i]["id"]
            hospital_name = hospital_list[i]["name"]
            hospital_address = hospital_list[i]["address"]
            hospital = {"id":str(hospital_id), "name" : hospital_name, "address": hospital_address}
            new_hospital_list.append(hospital)
    new_hospital_dict = {"hospital": new_hospital_list}
    with open(new_hospital_file, "w", encoding='UTF-8') as dump_f:
        json.dump(new_hospital_dict, dump_f, ensure_ascii=False)
