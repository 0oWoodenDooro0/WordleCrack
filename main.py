import words
result = None
recommend_words = words.check("_____", "_____", result)[1]
for i in range(5):
    print(recommend_words[i][0])
while True:
    word = str(input("輸入單字"))
    if word == "end" :
        break
    color = str(input("輸入顏色"))
    if color == "end":
        break
    result, recommend_words = words.check(word, color, result)
    size = 5 if len(recommend_words) > 5 else len(recommend_words)
    for i in range(size):
        print(recommend_words[i][0])
