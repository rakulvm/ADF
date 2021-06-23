from configparser import ConfigParser

file= "config.ini"
config=ConfigParser()
config.read(file)

print(config.sections())

config.add_section('bank')
config.set('bank','name','HDFC')
#
# with open(file, 'w') as configfile:
#     config.write(configfile)