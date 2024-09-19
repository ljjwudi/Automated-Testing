import configparser


def read_section_key_value_dict(file_path, section):
    config = configparser.ConfigParser()
    config.read(file_path)
    if section in config.sections():
        section_dict = {}
        for key, value in config.items(section):
            section_dict[key] = value
        return section_dict

    else:
        print(f"Section '{section}' not found in {file_path}")
        return None


# if __name__ == '__main__':
#     section_dict = read_section_key_value_dict('../config/config.ini', 'default')
#     print(section_dict['cookie'])
