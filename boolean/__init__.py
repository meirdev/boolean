Value = str | int | bool


def boolean(value: Value) -> bool:
    error = ValueError(f"invalid truth value {value!r}")

    if isinstance(value, bool):
        return value

    if isinstance(value, int):
        if value == 1:
            return True
        elif value == 0:
            return False
        else:
            raise error

    if isinstance(value, str):
        value = value.lower()

        if value in ["y", "yes", "t", "true", "on", "1"]:
            return True
        elif value in ["n", "no", "f", "false", "off", "0"]:
            return False
        else:
            raise error

    raise error


def is_true(value: Value) -> bool:
    return boolean(value) is True


def is_false(value: Value) -> bool:
    return boolean(value) is False
