from random import randint
import time

def shutudai():
    #quiz_ans
    #各配列の0番目に問題それ以降は答え
    quiz_ans = [
        ["サザエの旦那の名前は？", "マスオ", "ますお"], 
        ["カツオの妹の名前は？", "ワカメ", "わかめ"], 
        ["タラオはカツオから見てどんな関係？", "甥", "おい", "甥っ子", "おいっこ"]]

    num = randint(0,2)
    print(f"問題：\n{quiz_ans[num][0]}")
    return quiz_ans[num]

def kaitou(quiz_ans):
    ans = input("答えるんだ：")
    print("正解！！！" if ans in quiz_ans else "出直してこい")

if __name__ == "__main__":
    start_time = time.time()
    kaitou(shutudai())
    end_time = time.time()
    print(f"所要時間は{(end_time-start_time):.2f}です。")