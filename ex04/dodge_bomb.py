import pygame as pg
import sys
from random import randint


def main():
    pg.display.set_caption("逃げろ！こうかとん")
    scrn_width = 1600
    scrn_height = 900
    scrn_sfc = pg.display.set_mode((scrn_width, scrn_height))

    bg_sfc = pg.image.load("fig/pg_bg.jpg")
    bg_rct = bg_sfc.get_rect()

    tori_sfc = pg.image.load("fig/5.png")
    tori_sfc = pg.transform.rotozoom(tori_sfc, 0, 2.0)
    tori_rct = tori_sfc.get_rect()
    tori_rct.center = 900, 400

    bomb_sfc = pg.Surface((20, 20))
    bomb_sfc.set_colorkey((0, 0, 0))
    pg.draw.circle(bomb_sfc, (255, 0, 0), (10, 10), 10)
    bomb_rct = bomb_sfc.get_rect()
    bomb_rct.centerx = randint(10, scrn_width-10)
    bomb_rct.centery = randint(10, scrn_height-10)

    clock = pg.time.Clock()

    while True:
        scrn_sfc.blit(bg_sfc, bg_rct)
        scrn_sfc.blit(tori_sfc, tori_rct)
        scrn_sfc.blit(bomb_sfc, bomb_rct)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                key_status = pg.key.get_pressed()
                if key_status[pg.K_UP]:
                    tori_rct.centery -= 1
                elif key_status[pg.K_DOWN]:
                    tori_rct.centery += 1
                elif key_status[pg.K_RIGHT]:
                    tori_rct.centerx += 1
                elif key_status[pg.K_LEFT]:
                    tori_rct.centerx -= 1

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()