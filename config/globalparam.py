import os
from public.common.readconfig import ReadConfig

# read config file
config_file_path = os.path.split(os.path.realpath(__file__))[0]
read_config = ReadConfig(os.path.join(config_file_path,'config.ini'))
# parameter setup
prj_path = read_config.getValue('projectConfig','project_path')
# log path
log_path = os.path.join(prj_path, 'report', 'log')
# screenshot path
img_path = os.path.join(prj_path, 'report', 'image')
# report path
report_path = os.path.join(prj_path, 'report', 'testreport')
# default browser
browser = 'chrome'

# testdata path
data_path = os.path.join(prj_path, 'data', 'testdata')