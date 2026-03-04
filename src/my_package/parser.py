class Parser:
    def __init__(self) -> None:
        pass

    def parse_dict_to_json(self, dict_: dict) -> str:
        result = "{\n"
        for key, value in dict_.items():
            result += f"    {key} : {value}\n"
        result += '}'
        return result
