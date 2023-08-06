from spectre.generation import utils

def generate(entities, config):
    for ent in entities.keys():
        entity = generate_entity(entities[ent], ent)
        write_entity(ent, entity, config)
    #utils.write_to_file("".join(lines), f'jhipster/{schema_info["name"]}.jdl')

def write_entity(name, entity, config):
    utils.write_to_file("".join(entity), f'jhipster/{name}.jdl', config)

def convert_type(t, name):

    int_type = 'Integer'
    string_type = 'String'
    timestamp_type = 'Instant'
    float_type = 'Double'
    id_type = 'UUID'

    #if utils.is_id(name):
    #    return id_type
    type_map = {
        'int': int_type,
        'string': string_type,
        'datetime': timestamp_type,
        'timestamp': timestamp_type,
        'long': float_type,
        'double': float_type,
        'binary': id_type,
        'GUID': id_type,
        'UUID': id_type
    }

    return type_map.get(t, f'TYPE_MISSING: {t}')

def generate_entity(entity, name):
    output = [f'entity {utils.to_pascal(name)} {{\n']
    for field in entity['fields']:
        field_name = field["name"]
        member = f'\t{field_name} {convert_type(field["type"], field_name)}\n'
        output.append(member)
    output.append('}\n')
    return output