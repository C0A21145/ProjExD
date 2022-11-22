import time
from random import randint
import copy

#文字数、欠損文字数、繰り返し回数
quiz_length = 10
kesson_num = 2
maximum_count = 3

#対象文字列、欠損文字、表示文字
taisyou_string = []
kesson_string = []
hyouzi_string = []

#解答回数
count = 0

def make_quiz():
    global taisyou_string, kesson_string, hyouzi_string, kesson_num
    kesson_string.clear()

    taisyou_string = [chr(randint(65, 90)) for i in range(quiz_length)]
    hyouzi_string = copy.copy(taisyou_string)

    for i in range(kesson_num):
        kesson = hyouzi_string.pop(randint(0, len(hyouzi_string)-1))
        kesson_string.append(kesson)

    print("対象文字：")
    print(" ".join(taisyou_string))
    #問題解答(デバッグ用)
    #print("欠損文字：")
    #print(" ".join(kesson_string))
    print("表示文字：")
    print(" ".join(hyouzi_string))
    print()

def kesson_kaitou(ans):
    global kesson_num
    if ans == kesson_num:
        print("正解です。それでは具体的に欠損文字を1つずつ入力してください")
        return True  
    else:
        print("不正解です。またチャレンジしてください")
        return False

def kesson_string_kaitou(ans):
    global kesson_string, count
    if ans in kesson_string:
        kesson_string.remove(ans)
        count += 1

if __name__ == "__main__":
    start_time = time.time()
    for i in range(maximum_count):
        #出題データの作成
        make_quiz()

        #欠損文字数の回答・判定
        kesson_ans = int(input("欠損文字はいくつあるでしょうか？："))
        judge = kesson_kaitou(kesson_ans)
        if judge == False:
            continue
        
        #欠損文字の入力・判定
        for i in range(kesson_num):
            kesson_string_kaitou(input((f"{i+1}つ目の文字を入力してください：")))
        if count == kesson_num:
            print("正解です！おめでとうございます！")
            break
        else:
            print("不正解ですまたチャレンジしてください")
            print("-"*20)
            continue

    #所要時間の表示
    end_time = time.time()
    print(f"所要時間：{end_time-start_time}")
