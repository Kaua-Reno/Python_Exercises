# exemplo 1 "MOD09A1.A2006001.h08v05.005.2006012234657.hdf"
# exemplo 2 "MOD09A1.A2006001.h08v05.006.2015113045801.hdf"
arquivo = input("Digite o nome do arquivo MODIS: ")
 
product = arquivo[0:7]
if product[0:3] == "MOD":
  satellite = "Terra"
else:
  satellite = "unknown"
year_of_acquisition = arquivo[9:13]
julian_day = arquivo[13:16]
horizontal_tile = arquivo[18:20]
vertical_tile = arquivo[21:23]
collection = arquivo[24:27]
year_of_production = arquivo[28:32]
julian_day_of_production = arquivo[32:35]
production_hour = arquivo[35:37]
production_minute = arquivo[37:39]
production_second = arquivo[39:41]
data_format = arquivo[42:45]
 
print ("Satellite...............: " + satellite) 
print ("Product.................: " + product) 
print ("Year of Acquisition.....: " + year_of_acquisition) 
print ("Julian Day..............: " + julian_day) 
print ("Horizontal Tile.........: " + horizontal_tile) 
print ("Vertical Tile...........: " + vertical_tile) 
print ("Collection..............: " + collection) 
print ("Year of Production......: " + year_of_production) 
print ("Julian Day of Production: " + julian_day_of_production) 
print ("Production Hour.........: " + production_hour) 
print ("Production Minute.......: " + production_minute) 
print ("Production Second.......: " + production_second) 
print ("Data Format.............: " + data_format) 