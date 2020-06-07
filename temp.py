from urllib.request import urlopen, Request
 
old_url = 'https://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FGLDAS%2FGLDAS_NOAH025_M.2.1%2F2000%2FGLDAS_NOAH025_M.A200001.021.nc4&FORMAT=bmM0Lw&BBOX=30.69%2C120.86%2C31.87%2C122.01&LABEL=GLDAS_NOAH025_M.A200001.021.nc4.SUB.nc4&SHORTNAME=GLDAS_NOAH025_M&SERVICE=L34RS_LDAS&VERSION=1.02&DATASET_VERSION=2.1&VARIABLES=AvgSurfT_inst%2CRainf_f_tavg%2CRainf_tavg%2CSnowf_tavg%2CTair_f_inst%2CWind_f_inst'
req = Request(old_url)
response = urlopen(req)  
print('Info():')
print(response.info())