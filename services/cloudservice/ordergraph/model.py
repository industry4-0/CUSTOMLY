from neomodel import StructuredNode, RelationshipTo, StringProperty, RelationshipFrom


class Product(StructuredNode):
    name = StringProperty(required=True)
    required_features = RelationshipTo("Feature", "REQUIRED_FEATURE")
    optional_features = RelationshipTo("Feature", "OPTIONAL_FEATURE")
    produced_by = RelationshipFrom('Subassembly', 'PRODUCES')


class Property(StructuredNode):
    name = StringProperty(required=True)
    type = StringProperty(required=True)


class Feature(StructuredNode):
    name = StringProperty(required=True)
    properties = RelationshipTo("Property", "HAS_PROPERTY")
    implemented_by = RelationshipFrom('Subassembly', 'IMPLEMENTS')


class Subassembly(StructuredNode):
    name = StringProperty(required=True)
    requires = RelationshipTo("Subassembly", "REQUIRES")
    implements = RelationshipTo("Feature", "IMPLEMENTS")
    produces = RelationshipTo(Product, "PRODUCES")


class Task(StructuredNode):
    name = StringProperty(required=True)
    implements = RelationshipTo("Subassembly", "IMPLEMENTS")
    use = RelationshipTo("Requires", "USE")


class Service(StructuredNode):
    name = StringProperty(required=True)
