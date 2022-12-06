data = {
    'body': [
        {
            "field_name": "transaction_id",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "name",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "data.id",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "data.information.address",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "data.name",
            "data_type": "string",
            "required": True
        }
    ],
    'path': [
        {
            "field_name": "phone_number",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "full_name",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "province_id",
            "data_type": "string",
            "required": True
        },
    ],
    'query': [
        {
            "field_name": "phone_number",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "full_name",
            "data_type": "string",
            "required": True
        },
        {
            "field_name": "province_id",
            "data_type": "string",
            "required": True
        },
    ]
}



# def construct_function(excecuted_func: str, field_name: list):
#     try:
#         len_data = len(field_name)
#         for h, i in enumerate(field_name):
#             excecuted_func += f"['{i}']"
#             if h == len_data + 1:
#                 excecuted_func += " = {}"
#                 exec(excecuted_func)
#         exec(excecuted_func)
#     except KeyError as e:
#         structure[e.args[0]] = {}
#         construct_function(excecuted_func='structure', field_name=field_name)
        


# for i in data:
#     if i['parameter_type'] == 'body':
#         field_name = i['field_name'].split('.')
#         total_field = len(field_name)
#         if  total_field > 1:
#             for i in range(0, total_field-1):
#                 next_data =  {}
#                 curr[field_name[i]] = next_data
#                 curr = next_data
#         structure[i['field_name']] = {}
                    
                    
        # excecuted_func = 'structure'
        # construct_function(excecuted_func, field_name)
        
from mergedeep import merge

def construct_body_and_query_parameter(param: dict, parameter_type: str):
    for i in data[parameter_type]:   
        structure = {}
        curr = structure
        field_name = i['field_name'].split('.')
        for index, j in enumerate(field_name):
            next_data =  {}
            if index == len(field_name) -1: 
                curr[j] = "value"
            else:
                curr[j] = next_data
            curr = next_data
        merge(param,structure)
    return param

for key in data.keys():
    result = {}
    result[key] = construct_body_and_query_parameter(param={}, parameter_type=key)
    print(result)        
            