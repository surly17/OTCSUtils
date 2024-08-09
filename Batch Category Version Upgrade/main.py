from ConfigLoader.ConfigReader import locate_config_file

cfg_file_location = locate_config_file()

print ("Here is the file from main call:" + cfg_file_location)