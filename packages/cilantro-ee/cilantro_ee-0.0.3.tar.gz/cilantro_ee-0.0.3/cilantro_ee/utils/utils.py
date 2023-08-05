def is_valid_hex(hex_str: str, length=0) -> bool:
    """
    Returns true if hex_str is valid hex. False otherwise
    :param hex_str: The string to check
    :param length: If set, also verify that hex_str is the valid length
    :return: A bool, true if hex_str is valid hex
    """
    try:
        assert isinstance(hex_str, str)
        int(hex_str, 16)
        if length:
            assert len(hex_str) == length
        return True
    except:
        return False


def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

