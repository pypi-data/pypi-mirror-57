"""Decorators used for adding functionality to the library."""


def ignore(property_name):
    """A decorator function for marking keys as those which should be ignored."""

    def store_key_map(class_reference):
        """Store the key map."""
        if not hasattr(class_reference, "__deserialize_ignore_map__"):
            setattr(class_reference, "__deserialize_ignore_map__", {})

        class_reference.__deserialize_ignore_map__[property_name] = True

        return class_reference

    return store_key_map


def _should_ignore(class_reference, property_name):
    """Check if a property should be ignored."""

    if not hasattr(class_reference, "__deserialize_ignore_map__"):
        return False

    return class_reference.__deserialize_ignore_map__.get(property_name, False)


def key(property_name, key_name):
    """A decorator function for mapping key names to properties."""

    def store_key_map(class_reference):
        """Store the key map."""
        if not hasattr(class_reference, "__deserialize_key_map__"):
            setattr(class_reference, "__deserialize_key_map__", {})

        class_reference.__deserialize_key_map__[property_name] = key_name

        return class_reference

    return store_key_map


def _get_key(class_reference, property_name):
    """Get the key for the given class and property name."""

    if not hasattr(class_reference, "__deserialize_key_map__"):
        return property_name

    return class_reference.__deserialize_key_map__.get(property_name, property_name)


def parser(key_name, parser_function):
    """A decorator function for mapping parsers to key names."""

    def store_parser_map(class_reference):
        """Store the parser map."""

        if not hasattr(class_reference, "__deserialize_parser_map__"):
            setattr(class_reference, "__deserialize_parser_map__", {})

        class_reference.__deserialize_parser_map__[key_name] = parser_function

        return class_reference

    return store_parser_map


def _get_parser(class_reference, key_name):
    """Get the parser for the given class and keu name."""

    def identity_parser(value):
        """This parser does nothing. It's simply used as the default."""
        return value

    if not hasattr(class_reference, "__deserialize_parser_map__"):
        return identity_parser

    return class_reference.__deserialize_parser_map__.get(key_name, identity_parser)
