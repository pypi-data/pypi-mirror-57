"""
配置文件读取类：读取两个配置文件：一个settings下的项目配置文件，一个pageElement下的locator元素定位文件
主要用于解析配置文件，并回写
"""
import configparser


class ConfigHandler:
    def __init__(self, path):
        """
        解析配置文件
        :param path: 传入的为ini文件所在的路径，拼接到配置文件的路径.ini
        """
        self.path = path
        config = configparser.ConfigParser()
        config.read(path, encoding='utf-8')
        self.config = config

    def read(self, section, option):
        """读取config.ini配置文件中的值"""
        try:
            return self.config.get(section=section, option=option)
        except configparser.NoSectionError:
            print('没有这个section')
        except configparser.NoOptionError:
            print('没有这个option')

    def write(self, section, option, value, mode='w'):
        """写操作 写入config.ini"""
        if self.config.has_section(section):
            self.config.set(section, option, value)
            with open(file=self.path, mode=mode, encoding='utf-8') as f:
                self.config.write(f)

    def get_locator_value(self, section, option=None, params=None):
        """读取元素定位配置文件locator.ini中的值，若定位内容中有要传入的值，通过匹配$$进行替换"""
        try:
            if option is None:
                value = dict(self[section])
                return value
            value = self.config.get(section, option)
            if not params is None:
                if '$$' in value:
                    value = value.replace('$$', params)
            if '->' in value:
                value = tuple(value.split("->"))
            return value
        except (configparser.NoOptionError, configparser.NoSectionError) as e:
            raise e


# if __name__ == '__main__':
    # print('**************')
    # p_path = ProjectPath(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))   # 项目中的路径类ProjectPath
    # file_path = os.path.join(p_path.CONFIG_PATH, 'config.ini')
    # my_config = ConfigHandler(file_path)
    # host = my_config.read('log', 'format').replace('@', '%')
    # print(host)
    # locator_path = os.path.join(p_path.LOCATOR_PATH, 'locator.ini')
    # locator_config = ConfigHandler(locator_path)
    # ### [common_page]
    # ### menu = xpath->//div[@class ='menu-node']/span[contains(text(), '$$')]
    # locator = locator_config.get_locator_value('common_page', 'menu'， '采购价格')
    # print(locator)
    # locator = locator_config.get_locator_value('common_page', 'test')
    # print(locator)
