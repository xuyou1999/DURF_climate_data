import netCDF4 as nc
import csv

class CD4File:
    def __init__(self, filename):
        self._obj = nc.Dataset(filename)
        self.vairables = self._obj.variables
        self.keys = self.vairables.keys()
        self.year = int(filename[-22:-18])
        self.month = int(filename[-18:-16])

    def __str__(self):
        return self._obj
        
    def get_keys(self):
        return self.keys

    def get_longname(self, variable_name):
        return self.vairables[variable_name].long_name
    
    def get_unit(self, variable_name):
        return self.vairables[variable_name].units
    
    def get_data(self, variable_name):
        return self.vairables[variable_name]
    
    def transalate_keys(self):
        d = {}
        for short in self.get_keys():
            try:
                longname = self.get_longname(short)
            except:
                longname = 'NoLongName'
            d[short] = longname
        return d

    #calculate the average number of one variable in the region, return a numpy float32
    def average(self, datas):
        n = 0
        total = 0
        for i in datas[0]:
            for j in i:
                if float(j) == j:
                    n += 1
                    total += j
        return total / n

    #pile the average data of each variable in a list in the original order
    def pile_avg_data(self, vairable_list = ['Snowf_tavg', 'Rainf_tavg', 'AvgSurfT_inst', 'Wind_f_inst', 'Rainf_f_tavg', 'Tair_f_inst']):
        avg_list = []
        for i in vairable_list:
            avg_list.append(self.average(self.get_data(i)))
        return avg_list
    
    #same as above, but output a dict
    def pile_avg_data_dict(self, vairable_list = ['Snowf_tavg', 'Rainf_tavg', 'AvgSurfT_inst', 'Wind_f_inst', 'Rainf_f_tavg', 'Tair_f_inst']):
        d = {'Year': self.year, 'Month': self.month}
        trans = self.transalate_keys()
        for i in vairable_list:
            longname = trans[i]
            d[longname] = self.average(self.get_data(i))
        return d
        
def output_csv(name, data_dict_list):
    with open(name, 'w', newline='') as file:
        fieldnames = data_dict_list[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for d in data_dict_list:
            writer.writerow(d)


#testcode
if __name__ == '__main__':
    '''
    obj = CD4File('G:\\我的云端硬盘\\2020 Summer Break\\DURF\\Data\\Climate\\Shanghai\\2000\\GLDAS_NOAH025_M.A200001.021.nc4.SUB.nc4')
    filename = 'GLDAS_NOAH025_M.A200001.021.nc4.SUB.nc4'
    obj = CD4File(filename)
    print(obj.keys)
    print(obj.transalate_keys())
    print(obj.get_unit('Snowf_tavg'))
    print(obj.pile_avg_data_dict())
    output_csv('test.csv', [obj.pile_avg_data_dict()])
    '''