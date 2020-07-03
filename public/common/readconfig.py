import configparser
import codecs

class ReadConfig:
    """
    专门读取配置文件的，.ini文件格式
    """
    def __init__(self, filename):
        # configpath = os.path.join(prjDir,filename)
        configpath = filename
        # print(configpath)
        fd = open(configpath)
        data = fd.read()
        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            files = codecs.open(configpath, "w")
            files.write(data)
            files.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self, env, name):
        """
        [projectConfig]
        project_path=D:/ProgramFiles/wamp3.2.0/www/TestingFramework
        :param env:[projectConfig]
        :param name:project_path
        :return:D:/ProgramFiles/wamp3.2.0/www/TestingFramework
        """
        return self.cf.get(env,name)