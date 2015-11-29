#run this command from terminal : easy_install configobj

from configobj import ConfigObj

#return value for a given key from conf file
def read_property(key):
	config = ConfigObj('properties.conf')
        value = config[key]
        return value

value=read_property('trainingfilepath')
print value
