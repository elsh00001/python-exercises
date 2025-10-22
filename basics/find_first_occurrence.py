def find_first_occurrence(haystack: str, needle: str):
    offset = haystack.find(needle)
    if offset == -1:
        return False
    return offset

    pass
