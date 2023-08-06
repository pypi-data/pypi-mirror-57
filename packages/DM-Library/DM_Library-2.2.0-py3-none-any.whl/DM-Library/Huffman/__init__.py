import zlib, base64

def get_uncompressed_file(filename):
    file = open(filename,'r')
    text = file.read()
    file.close()
    return text


def encode_text(file):
    code = base64.b64encode(zlib.compress(file.encode('utf-8'), 9))
    code = code.decode('utf-8')
    return code

def decode_text(code):
    decoded_txt = zlib.decompress(base64.b64decode(code))
    return decoded_txt
