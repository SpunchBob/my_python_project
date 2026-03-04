from my_package.parser import Parser

if __name__ == "__main__":
    parser = Parser()
    dict_ = {
        "age" : "int",
        "name" : "str",
        "course" : "int"
        }
    json_str = parser.parse_dict_to_json(dict_)
    print(f"{json_str}")
