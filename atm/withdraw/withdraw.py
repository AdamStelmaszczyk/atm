notes = [1000, 500, 100, 50, 20, 10]


class NoteUnavailableException(Exception):
    pass


def calculate_change(money):
    assert isinstance(money, int) and money >= 0
    smallest = notes[-1]
    if money % smallest != 0:
        raise NoteUnavailableException("The smallest note is {} thus can't withdraw {}".format(smallest, money))
    result = []
    for note in notes:
        how_many = money // note
        money -= how_many * note
        result.append(how_many)
    return result


def unroll_change(change):
    assert len(change) == len(notes)
    result = []
    for i in range(len(notes)):
        for _ in range(change[i]):
            result.append(notes[i])
    return result
