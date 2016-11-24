from urllib import parse

def URLConverter(convertThis):
    converted = parse.quote_plus(convertThis)
    return converted