class Parser:
    def __init__(self) -> None:
        pass

    def parse_dict_to_json(self, dict_: dict) -> str:
        result = "{\n"
        for key, value in dict_.items():
            result += f"    {key} : {value}\n"
        result += '}'
        return result

    def parse_list_to_json(self, list_: list) -> str:
        result = "{\n"
        for item in list_:
            result += f"    {item},\n"
        result += "}"
        return result 
