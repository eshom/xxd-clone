import subprocess

def test_testfile():
    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', 'tests/testfile'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', 'tests/testfile'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c30', 'tests/testfile'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c30', 'tests/testfile'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c0', 'tests/testfile'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c0', 'tests/testfile'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c256', 'tests/testfile'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c256', 'tests/testfile'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

def test_bashrc():
    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', 'tests/bashrc'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', 'tests/bashrc'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c30', 'tests/bashrc'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c30', 'tests/bashrc'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c0', 'tests/bashrc'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c0', 'tests/bashrc'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c256', 'tests/bashrc'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c256', 'tests/bashrc'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

def test_random_bytes():
    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', 'tests/random_bytes'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', 'tests/random_bytes'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c30', 'tests/random_bytes'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c30', 'tests/random_bytes'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c0', 'tests/random_bytes'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c0', 'tests/random_bytes'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout

    actual = subprocess.run(['python3', '-m', 'my_xxd.xxd', '-c256', 'tests/random_bytes'], stdout=subprocess.PIPE)
    expected = subprocess.run(['xxd', '-c256', 'tests/random_bytes'], stdout=subprocess.PIPE)

    assert actual.stdout == expected.stdout
