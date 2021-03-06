import master
import os

def get_nc4_filenames_list_deep(root_path):
    files_list = []
    for root, dirs, files in os.walk(root_path):
        for filename in files:
            if filename[-3:] == 'nc4':
                files_list.append(os.path.join(root, filename))
    return files_list
    
def get_nc4_filenames_list_year(root_path, y):
    files_list = []
    for files in os.listdir(root_path):
        if files[-3:] == 'nc4' and files[-22: -18] == y:
            files_list.append(os.path.join(root_path, files))
    return files_list

def get_nc4_filenames_list_month(root_path, m):
    files_list = []
    for files in os.listdir(root_path):
        if files[-3:] == 'nc4' and files[-18: -16] == m:
            files_list.append(os.path.join(root_path, files))
    return files_list


def from_filenames_to_obj_list(filenames):
    obj_list = []
    for f in filenames:
        obj_list.append(master.CD4File(f))
    return obj_list

def from_objlist_to_datadict_list(obj_list, vairable_list = ['Snowf_tavg', 'Rainf_tavg', 'AvgSurfT_inst', 'Wind_f_inst', 'Rainf_f_tavg', 'Tair_f_inst']):
    d_list = []
    for obj in obj_list:
        d = obj.pile_avg_data_dict(vairable_list)
        d_list.append(d)
    return d_list


def main():
    city = input('City? ')
    if input('include time? [y] or [n] ') == 'y':
        y_or_n = input('Year or Month? [y] or [m] ')
        time = input('Number? ')
        deep = 'n'
    else:
        time = ''
        deep = 'y'
    name = input('filename ') + '.csv'
    main_path = os.getcwd()
    path = main_path + '\\' + city
    output_name = path + "\\" + name
    if deep == 'y':
        filenames = get_nc4_filenames_list_deep(path)
    else:
        if y_or_n == 'y':
            filenames = get_nc4_filenames_list_year(path, time)
        else:
            filenames = get_nc4_filenames_list_month(path, time)
    
    obj_list = from_filenames_to_obj_list(filenames)
    d_list = from_objlist_to_datadict_list(obj_list)
    master.output_csv(output_name, d_list)

if __name__ == "__main__":
    main()