from my_package.parser import Parser

if __name__ == "__main__":
    parser = Parser()
    dict_ = {
        "age" : "int",
        "name" : "str",
        "course" : "int"
        }
    list_ = [
        "aleks",
        "ivan",
        "max"
        ]
    json_str_dict = parser.parse_dict_to_json(dict_)
    json_str_list = parser.parse_list_to_json(list_)
    print(f"{json_str_dict}")
    print(f"{json_str_list}")

