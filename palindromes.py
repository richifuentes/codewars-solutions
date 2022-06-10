from collections import deque, Counter


def palindrome_from(letters):
    """
    Forms a palindrome by rearranging :letters: if possible,
    throwing a :ValueError: otherwise.
    :param letters: a suitable iterable, usually a string
    :return: a string containing a palindrome
    """
    counter = Counter(letters)
    sides = []
    center = deque()
    for letter, occurrences in counter.items():
        repetitions, odd_count = divmod(occurrences, 2)
        if not odd_count:
            sides.append(letter * repetitions)
            continue
        if center:
            raise ValueError("no palindrome exists for '{}'".format(letters))
        center.append(letter * occurrences)
    center.extendleft(sides)
    center.extend(sides)
    return ''.join(center)
