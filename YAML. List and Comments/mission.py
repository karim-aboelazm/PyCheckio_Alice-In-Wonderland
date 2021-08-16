def yaml(a):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(yaml('- write some\n- "Alex Chii"\n- 89'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- write some\n- "Alex Chii"\n- 89') == ['write some', 'Alex Chii', 89]
    assert yaml('# comment\n'
 '- write some # after\n'
 '# one mor\n'
 '- "Alex Chii #sir "\n'
 '- 89 #bl') == ['write some', 'Alex Chii #sir ', 89]
    assert yaml('- 1\n- 2\n- 3\n\n- 4\n\n\n\n- 5') == [1, 2, 3, 4, 5]
    assert yaml('-\n-\n-\n- 7') == [None, None, None, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
