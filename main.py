import words


def check():
    result = None
    recommend_words = words.check("_____", "_____", result)[1]
    print("如果是綠色輸入g,橘色輸入o,灰色輸入-")
    m, n = set(), set()
    for i in range(5):
        print(recommend_words[i][0])
    while True:
        word = str(input("輸入單字"))
        if word == "end":
            print("重設中")
            break
        color = str(input("輸入顏色"))
        if color == "end":
            print("重設中")
            break
        result, recommend_words, m, n = words.check(word, color, result, m, n)
        size = 5 if len(recommend_words) > 5 else len(recommend_words)
        for i in range(size):
            print(recommend_words[i][0])


while True:
    check()
