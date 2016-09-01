def reverse(s):
    split_str = s.split(' ')
    r = ''
    for word in split_str:
        r += word[:: -1]
        r += ' '
    return r


if __name__ == '__main__':
    s = 'agata neltz'
    print reverse(s)
