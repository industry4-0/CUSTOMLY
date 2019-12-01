import yaml
from neomodel import db

from model import *

db.set_connection('bolt://neo4j:123456@localhost:7687')


def reset_db():
    for f in Feature.nodes.all():
        f.delete()

    for p in Product.nodes.all():
        p.delete()

    for s in Subassembly.nodes.all():
        s.delete()


def load_db(filename):
    with open(filename) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    # Add features
    for f in data['features']:
        if not isinstance(f, dict):
            Feature(name=f).save()
            continue
        name = list(f.keys())[0]
        feature = Feature(name=name).save()
        for p in f[name]['properties']:
            property_name = list(p.keys())[0]
            property_type = p[property_name]
            property = Property.nodes.get_or_none(name=property_name, type=property_type)
            if property is None:
                property = Property(name=property_name, type=property_type).save()
            feature.properties.connect(property)

    # Add products
    for p in data['products']:
        assert len(p) == 1
        name = list(p.keys())[0]
        product = Product(name=name).save()
        for f in p[name].get('required_features', list()):
            feature = Feature.nodes.get(name=f)
            product.required_features.connect(feature)
        for f in p[name].get('optional_features', list()):
            feature = Feature.nodes.get(name=f)
            product.optional_features.connect(feature)

    # Add Subassmeblies
    for s in data['subassemblies']:
        assert len(p) == 1
        name = list(s.keys())[0]
        subassembly = Subassembly(name=name).save()
        if s[name] is None:
            continue
        for f in s[name].get('implements', list()):
            feature = Feature.nodes.get(name=f)
            subassembly.implements.connect(feature)
        for ps in s[name].get('requires', list()):
            parent_subassembly = Subassembly.nodes.get(name=ps)
            subassembly.requires.connect(parent_subassembly)
        for p in s[name].get('produces', list()):
            product = Product.nodes.get(name=p)
            subassembly.produces.connect(product)


if __name__ == '__main__':
    reset_db()
    load_db('cell.yml')
