import ujson as json
import csv
from django.utils.text import slugify
from csv2json.funciones import read_file, add_list
# elem : (model_name, source_file, main_field_to_slug, conditions)


class CSV2JSON:
    def __init__(self,
                 *args,
                 **kwargs):
        self.origin = kwargs.get('origin', './csv')
        self.destiny = kwargs.get('destiny', './json')
        self.files = kwargs.get('files',
                                (None, None, None, {}))
        for model, file_name, field, condition in self.files:
            data_list = self.read_file(
                model,
                file_name,
                field,
                condition)
            self.write_json(file_name, data_list)

    def read_file(self,
                  model: str = "",
                  file_name: str = "",
                  field: str = "",
                  condition: dict = {}):
        path = "%s/%s" % (self.origin, file_name)
        data_list = []
        with open(path, 'r') as read:
            reader = csv.DictReader(read, delimiter=';')
            for row in reader:
                field_slug = "slug_%s" % field
                dict_data = {}
                for key, value in row.items():
                    if not key == "id":
                        if condition.get(key):
                            value = condition.get(key)(value)
                        else:
                            value = value.strip()
                        print("(())")
                        print(key, value)
                        dict_data.update({key: value})
                if field:
                    main_field = row.get(field)
                    dict_data.update({field_slug: slugify(main_field)})
                new_data = {
                    "model": model,
                    "pk": int(row.get('id', "0 ").strip()),
                    "fields": dict_data}
                data_list.append(new_data)
        return data_list

    def write_json(self, file_name, data_list):
        new_file_path = "%s/%s.json" % (
            self.destiny, file_name.split('.')[0])
        with open(new_file_path, 'w') as write_json:
            write_json.write("[\n")
            len_list = len(data_list)
            for i, elem in enumerate(data_list):
                elem_txt = json.dumps(elem)
                write_json.write(elem_txt)
                if i < len_list-1:
                    write_json.write(',\n')
                else:
                    write_json.write('\n')
            write_json.write("]")
