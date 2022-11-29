import tkinter as tk
import tkinter.messagebox as tkm
import matplotlib.pyplot as plt


def calc_graph(siki):
    graph_label = siki
    siki = list(siki)
    # 傾きの値
    katamuki = ""
    seppen = ""
    num = 2

    if "+" in siki:
        seppen_place = siki.index("+")
        seppen = siki[seppen_place+1:]
        seppen = int("".join(seppen))

    while True:
        if siki[num].isdecimal():
            katamuki += siki[num]
            num += 1
        else:
            break

    # デバッグ用
    print(f"katamuki {katamuki}")
    print(f"seppen {seppen}")

    katamuki = int(katamuki)

    # グラフ描画
    # グラフ画像保存先
    filepath = "./ex02/graph.png"

    # グラフ座標情報取得
    x = [i for i in range(-10, 11, 1)]
    try:
        y = [(i*katamuki) + seppen for i in range(-10, 11, 1)]
    except:
        y = [i*katamuki for i in range(-10, 11, 1)]

    plt.figure(figsize=(3, 3))
    plt.plot(x, y, label=graph_label)
    plt.savefig(filepath)


if __name__ == "__main__":
    calc_graph("y=10x+3")
