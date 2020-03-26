class Json:

    def to_json(self, obj):
        if isinstance(obj, (list, tuple)):
            return self.to_json_list_tuple(obj)
        elif isinstance(obj, (str, bool, type(None), int, float)):
            return self.to_json_str_bool_None_int_float(obj)
        elif isinstance(obj, dict):
            return self.to_json_dict(obj)
        elif isinstance(obj, (int, str, bool, type(None), float)):
            return self.to_json_str_bool_None_int_float(obj)

    def to_json_list_tuple(self, obj):
        data = []
        for arg in obj:
            if isinstance(arg, (int, str, bool, type(None), float)):
                data.append(self.to_json_str_bool_None_int_float(arg))
            if isinstance(arg, (list, tuple)):
                data.append(self.to_json_list_tuple(arg))
            if isinstance(arg, dict):
                data.append(self.to_json_dict(arg))
        string = ', \n'.join(data)
        return '[\n' + string + '\n]'

    def to_json_str_bool_None_int_float(self, obj):
        if isinstance(obj, bool):
            if obj:
                return 'true'
            else:
                return 'false'
        elif isinstance(obj, (int, float)):
            return '{}'.format(obj)
        elif isinstance(obj, str):
            return '"{}"'.format(obj)
        elif isinstance(obj, bool):
            if obj:
                return 'true'
            else:
                return 'false'
        elif isinstance(obj, type(None)):
            return 'null'

    def to_json_dict(self, obj):
        data = []
        for key, value in obj.items():
            if isinstance(value, (str, bool,      type(None), int, float)):
                data.append(self.to_json_record(key, self.to_json_str_bool_None_int_float(value)))
            if isinstance(value, (list, tuple)):
                data.append(self.to_json_record(key, self.to_json_list_tuple(value)))
            if isinstance(value, dict):
                data.append(self.to_json_record(key, self.to_json_dict(value)))
        string = ',\n'.join(data)
        return '{\n' + string + '\n}'
    def to_json_record(self, key, value):
        return f'"{key}": {value}'

my_json = Json()
set = [228, False,14.82,True, {5: "BSUIR1", 0: 28}, [88, 55]]
print(my_json.to_json(set))