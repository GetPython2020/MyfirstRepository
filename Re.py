import re


def main():
    username = input('Enter your username: ')
    qq = input('Enter your qq number: ')
    # match函数的第一个参数是正则表达式字符串或正则表达式对象
    # 第二个参数是要跟正则表达式做匹配的字符串对象
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', username)  #[0-9a-zA-Z_]=\w
    if not m1:
        print('Please input a valid username.')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('Please input a valid qq number.')
    if m1 and m2:
        print('You input are valid!')


if __name__ == '__main__':
    main()

import re


def main():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。, .]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
    print(sentence_list)  # ['窗前明月光', '疑是地上霜', '举头望明月', '低头思故乡']


if __name__ == '__main__':
    main()
