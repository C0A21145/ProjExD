import pygame as pg
import sys
import random
import time
import math

# ----------------------------------------------------------------
# 設定項目

# screen 0: gameplay画面
# screen 1: gameover画面
screen = 0

# アイテム出現可能回数
item_num = 1
# アイテム出現回数
item_count = 0

# こうかとんがアイテムを所持しているか
item_status = 0

# 残り時間
limit_time = 30

# 爆弾の初期速度
vx, vy = 1, 1


# ----------------------------------------------------------------


def main():
    global screen, item_count, item_status, vx, vy

    # 初期設定
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_width = 1600
    scrn_height = 900
    scrn_sfc = pg.display.set_mode((scrn_width, scrn_height))

    # 背景描画設定
    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    # こうかとん描画設定
    tori_sfc = pg.image.load("fig/5.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    # こうかとんの盾
    have_item_sfc = pg.Surface((100, 100))
    have_item_sfc.set_colorkey((0, 0, 0))
    pg.draw.rect(have_item_sfc, (192, 192, 192), (0, 0, 100, 70))
    pg.draw.polygon(have_item_sfc, (192, 192, 192),
                    ([0, 70], [100, 70], [50, 100]))
    have_item_rct = have_item_sfc.get_rect()

    # 爆弾描画設定
    bomb_sfc = pg.Surface((40, 40))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (20, 20), 20)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = random.randint(10, scrn_width-10)
    bomb_rct.centery = random.randint(10, scrn_height-10)

    # GameOver・GameClear文字のフォント設定
    fonto = pg.font.Font(None, 200)
    small_fonto = pg.font.Font(None, 100)

    # GameOverの文字設定
    gameover_text = fonto.render(str("Game Over"), True, (0, 0, 0))
    continue_text = small_fonto.render(
        str("Please press SPACE Key"), True, (0, 0, 0))
    gameover_text_rct = gameover_text.get_rect(
        center=(scrn_width//2, scrn_height//2))
    continue_text_rct = gameover_text.get_rect(
        center=(scrn_width//2, scrn_height//2+300))

    # GameClearの文字設定
    gameclear_text = fonto.render(str("Game Clear!!"), True, (0, 0, 0))
    gameclear_text_rct = gameover_text.get_rect(
        center=(scrn_width//2, scrn_height//2))

    # アイテム(盾)の描画設定
    item_sfc = pg.Surface((100, 100))
    item_sfc.set_colorkey((0, 0, 0))
    pg.draw.rect(item_sfc, (192, 192, 192), (0, 0, 100, 70))
    pg.draw.polygon(item_sfc, (192, 192, 192), ([0, 70], [100, 70], [50, 100]))
    item_rct = item_sfc.get_rect()
    item_rct.centerx = random.randint(50, scrn_width-50)
    item_rct.centery = random.randint(50, scrn_height-50)

    clock = pg.time.Clock()
    start_time = time.time()

    while True:
        # xボタンの有効化
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        # ゲームプレイ画面
        if screen == 0:
            scrn_sfc.blit(bg_sfc, bg_rct)
            scrn_sfc.blit(tori_sfc, tori_rct)
            scrn_sfc.blit(bomb_sfc, bomb_rct)

            # 残り制限時間
            deadline = limit_time - (time.time() - start_time)
            txt = small_fonto.render(
                str(math.floor(deadline)), True, (0, 0, 0))
            scrn_sfc.blit(txt, (1500, 0))

            # itemを所持していたら盾の表示
            if item_status == 1:
                have_item_rct.centerx = tori_rct.centerx
                have_item_rct.centery = tori_rct.centery + 30
                scrn_sfc.blit(have_item_sfc, have_item_rct)
            if event.type == pg.KEYDOWN:
                key_status = pg.key.get_pressed()
                old_place = [tori_rct.centerx, tori_rct.centery]
                if key_status[pg.K_UP]:
                    tori_rct.centery -= 1
                elif key_status[pg.K_DOWN]:
                    tori_rct.centery += 1
                elif key_status[pg.K_RIGHT]:
                    tori_rct.centerx += 1
                elif key_status[pg.K_LEFT]:
                    tori_rct.centerx -= 1
                if tori_rct.centerx < 48 or tori_rct.centerx > scrn_width-48 or tori_rct.centery < 68 or tori_rct.centery > scrn_height-68:
                    tori_rct.centerx = old_place[0]
                    tori_rct.centery = old_place[1]

            # 爆弾の動き処理
            bomb_rct.centerx += vx
            bomb_rct.centery += vy
            if bomb_rct.centerx < 20 or bomb_rct.centerx > scrn_width-20:
                vx *= -1
            if bomb_rct.centery < 20 or bomb_rct.centery > scrn_height-20:
                vy *= -1

            # item出現
            if item_num > item_count:
                scrn_sfc.blit(item_sfc, item_rct)

            # Game Clear判定
            if deadline < 0:
                screen = 2

            # GameOver判定
            if tori_rct.colliderect(bomb_rct):
                if item_status == 1:
                    vx *= -1
                    vy *= -1
                    item_status = 0
                else:
                    screen = 1

            # アイテム取得処理
            if tori_rct.colliderect(item_rct):
                if item_num > item_count:
                    item_status = 1
                    item_count = 99

        # ゲームオーバー時間
        elif screen == 1:
            scrn_sfc.blit(gameover_text, gameover_text_rct)
            scrn_sfc.blit(continue_text, continue_text_rct)
            key_status = pg.key.get_pressed()
            if key_status[pg.K_SPACE]:
                bomb_rct.centerx = random.randint(10, scrn_width-10)
                bomb_rct.centery = random.randint(10, scrn_height-10)
                screen = 0

        # ゲームクリア画面
        elif screen == 2:
            scrn_sfc.blit(gameclear_text, gameclear_text_rct)

        pg.display.update()
        clock.tick(10000)


# ----------------------------------------------------------------
if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
