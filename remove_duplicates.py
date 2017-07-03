def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target