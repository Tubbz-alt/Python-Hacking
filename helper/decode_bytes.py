def decode_bytes_with_special_character(bytes):
    result = bytes.replace(b"\x8e", b"Ae").replace(b"\x84", b"ae").replace(b"\x99", b"Oe").replace(b"\x94", b"oe").replace(b"\x9a", b"Ue").replace(b"\x81", b"ue").replace(b"\xe1", b"ss")
    return result.decode("utf-8")