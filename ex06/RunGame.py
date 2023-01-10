import pygame as pg
import sys
import random
import time
import math

# ----------------------------------------------------------------
# 設定項目

# 自分の座標
mx = 120
my = 600

# マップ情報リスト
map_info = [random.randint(0, 1) for _ in range(160)]

# インデックス番号(default=0)
box_index = 0

# 1ブロックのサイズ
BLOCK_SIZE = 120

# プレイヤースピード
V = 10

# フレームレート
F_RATE = 100

# 経過時間
wait_time = 0
# ----------------------------------------------------------------
# ブロッククラス


class Block(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # ブロック座標設定
        self.x = x
        self.y = y

        # ブロック画像読み込み(後で)
        # self.img = pg.image.load(~~).convert()

        self.image = pg.Surface((1920, 1080))
        self.image.set_colorkey((0, 0, 0))
        pg.draw.rect(self.image, (0, 128, 0), (self.x, self.y, 120, 40))
        pg.draw.rect(self.image, (184, 134, 11), (self.x, self.y+40, 120, 200))
        self.rect = self.image.get_rect()

    def update(self):
        pass


class Hole(pg.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        # ブロック座標設定
        self.x = x
        self.y = y

        # ブロック画像読み込み(後で)
        # self.img = pg.image.load(~~).convert()

        self.image = pg.Surface((120, 240))
        self.image.set_colorkey((0, 0, 0))
        pg.draw.rect(self.image, (0, 0, 0),
                     (self.x, self.y, self.x+120, self.y+240))
        self.rect = self.image.get_rect()

    def update(self):
        pass


class Player():
    def __init__(self, x, y):
        # ブロック座標設定
        self.x = x
        self.y = y

        self.player_sfc = pg.image.load("ex06/img/girl.png")
        self.player_sfc = pg.transform.scale(self.player_sfc, (120, 240))
        self.player_rct = self.player_sfc.get_rect()

    def blit(self):
        self.player_sfc.blit(self.player_sfc, self.player_rct)


def main():
    global box_index, wait_time
    # 初期設定
    pg.display.set_caption("走るゲーム")
    scrn_width = 1920
    scrn_height = 1080
    scrn_sfc = pg.display.set_mode((scrn_width, scrn_height))

    # 背景画像設定
    bg_sfc = pg.image.load("ex06/img/background.jpg")
    bg_sfc = pg.transform.scale(bg_sfc, (1920, 1080))
    bg_rct = bg_sfc.get_rect()

    # player作成
    player_sfc = pg.image.load("ex06/img/girl.png")
    player_sfc = pg.transform.rotozoom(player_sfc, 0, 0.7)
    player_rct = player_sfc.get_rect()
    player_rct.centerx = 180
    player_rct.centery = 700

    # ゲーム進行処理
    while True:
        # xボタンの有効化
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        # 時間
        clock = pg.time.Clock()

        # 無限ループ処理
        blocks = pg.sprite.Group()
        for i in range(17):
            if map_info[(box_index+i) % 160] == 0:
                blocks.add(Hole(wait_time+120*i, 840))
            elif map_info[(box_index+i) % 160] == 1:
                blocks.add(Block(wait_time+120*i, 840))

        box_index += 1
        wait_time += 1

        # フレームレート設定
        clock.tick(F_RATE)

        # 描画
        scrn_sfc.blit(bg_sfc, bg_rct)
        blocks.draw(scrn_sfc)
        scrn_sfc.blit(player_sfc, player_rct)

        # 画面更新
        pg.display.update()
        blocks.update()

        time.sleep(0.3)

        for event in pg.event.get():

            # 終了処理
            if event.type == pg.QUIT:
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()
