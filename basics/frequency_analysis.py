import string


def frequency_analysis(file_directory: str) -> dict[str, int]:
    alphabet = string.ascii_lowercase
    alphabet_dict = {}
    for i in alphabet:
        alphabet_dict[i] = 0
    with open(file_directory, "r") as fh:
        for i in fh:
            if i.lower() in alphabet_dict:
                alphabet_dict[i.lower()] += 1
    return alphabet_dict
    pass
