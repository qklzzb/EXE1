def replace_words(text, old_word, new_word1, new_word2):
    count = 1
    while old_word in text:
        # 偶数次替换
        if count % 2 == 0:
            text = text.replace(old_word, new_word1, 1)
        else:
        # 奇数次替换为marvellous
            text = text.replace(old_word, new_word2, 1)
        count += 1
        # print(text)
    return text


if __name__ == "__main__":
    # 读取文本字符串
    with open('file_to_read.txt', 'r') as f:
        line = ''
        value = ''
        for line in f:
            value += line
    print(value)

    # 计算次数
    num = value.count('terrible')
    print(num)
    # 调用函数替换单词，奇数次出现的换成marvellous，偶数次出现的换为pathetic
    new_value = replace_words(value, 'terrible', 'pathetic', 'marvellous')
    print(new_value)

    with open('result.txt', 'w') as f:
        f.write(new_value)
    pass
