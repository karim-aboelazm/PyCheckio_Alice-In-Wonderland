def yaml(a):
    # your code here
    return None


if __name__ == '__main__':
    print("Example:")
    print(yaml('- Alex\n'
 '-\n'
 '  - odessa\n'
 '  - dnipro\n'
 '- Li'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('- Alex\n'
 '-\n'
 '  - odessa\n'
 '  - dnipro\n'
 '- Li') == ['Alex', ['odessa', 'dnipro'], 'Li']
    assert yaml('- 67\n'
 '-\n'
 '  name: Irv\n'
 '  game: Mario\n'
 '-\n'
 '- 56') == [67,
 {'game': 'Mario', 'name': 'Irv'},
 None,
 56]
    assert yaml('name: Alex\n'
 'study:\n'
 '  type: school\n'
 '  number: 78\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': {'number': 78,
           'type': 'school'}}
    assert yaml('name: Alex\n'
 'study:\n'
 '  - 89\n'
 '  - 89\n'
 '  - "Hell"\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': [89, 89, 'Hell']}
    assert yaml('name: Alex\n'
 'study:\n'
 '  -\n'
 '    type: school\n'
 '    num: 89\n'
 '  -\n'
 '    type: school\n'
 '    num: 12\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': [{'num': 89,
            'type': 'school'},
           {'num': 12,
            'type': 'school'}]}
    assert yaml('name: Alex\n'
 'study:\n'
 '  -\n'
 '    type: school\n'
 '    nums:\n'
 '      - 12\n'
 '      - 67\n'
 '  -\n'
 '    type: school\n'
 '    num: 12\n'
 'age: 14') == {'age': 14,
 'name': 'Alex',
 'study': [{'nums': [12, 67],
            'type': 'school'},
           {'num': 12,
            'type': 'school'}]}
    print("Coding complete? Click 'Check' to earn cool rewards!")
