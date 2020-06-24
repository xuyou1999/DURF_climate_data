import gen_csv
import master
import os

class Year:
    def __init__(self, year, obj):
        self.year = year
        self.obj = [obj]
        self.data_dic = obj.pile_avg_data_dict()
        self.n = 1

    def add_obj(self, new_obj):
        add_data = new_obj.pile_avg_data_dict()
        for key in add_data.keys():
            if key in self.data_dic:
                self.data_dic[key] *= self.n
                self.data_dic[key] += add_data[key]
                new_n = self.n + 1
                self.data_dic[key] /= new_n
        self.n += 1
    
    def pile_avg_data_dict(self):
        return self.data_dic
        
def main():
    city = input('City? ')
    name = input('filename ') + '.csv'
    main_path = os.getcwd()
    path = main_path + '\\' + city
    output_name = path + "\\" + name
    filenames = gen_csv.get_nc4_filenames_list_deep(path)
    obj_list = gen_csv.from_filenames_to_obj_list(filenames)
    year_list = []
    obj = []
    for i in obj_list:
        if i.year not in year_list:
            year_list.append(i.year)
            obj.append(Year(i.year, i))
        else:
            index = year_list.index(i.year)
            obj[index].add_obj(i)
    d_list = []
    for j in obj:
        d_list.append(j.pile_avg_data_dict())
    master.output_csv(output_name, d_list)

if __name__ == '__main__':
    main()
