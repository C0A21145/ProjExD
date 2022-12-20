import pygame as pg
import random
import sys

# ----------------------------------------------------------------
guard_status = False


class Screen:
    def __init__(self, title, WideHeight, bgImgPath):
        pg.display.set_caption(title)
        self.sfc = pg.display.set_mode((WideHeight))
        self.rct = self.sfc.get_rect()
        self.bgi_sfc = pg.image.load(bgImgPath)
        self.bgi_rct = self.bgi_sfc.get_rect()

    def blit(self):
        self.sfc.blit(self.bgi_sfc, self.bgi_rct)


class Bird():
    key_delta = {
        pg.K_UP:    [0, -1],
        pg.K_DOWN:  [0, +1],
        pg.K_LEFT:  [-1, 0],
        pg.K_RIGHT: [+1, 0],
    }

    def __init__(self, imgPath, zoom, firstXY):
        self.sfc = pg.image.load(imgPath)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 2.0)
        self.rct = self.sfc.get_rect()

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        key_dct = pg.key.get_pressed()
        for key, delta in Bird.key_delta.items():
            if key_dct[key]:
                self.rct.centerx += delta[0]
                self.rct.centery += delta[1]
            if check_bound(self.rct, self.rct) != (+1, +1):
                self.rct.centerx -= delta[0]
                self.rct.centery -= delta[1]
        self.blit(scr)


class Bomb():
    def __init__(self, colors, radius, speedXY, scr: Screen):
        self.sfc = pg.Surface((radius*2, radius*2))
        pg.draw.circle(self.sfc, colors, (radius, radius), radius)
        self.sfc.set_colorkey((0, 0, 0))
        self.rct = self.sfc.get_rect()
        self.rct.centerx = random.randint(0, scr.rct.width)
        self.rct.centery = random.randint(0, scr.rct.height)
        self.speedX, self.speedY = speedXY

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen):
        self.rct.move_ip(self.speedX, self.speedY)
        yoko, tate = check_bound(self.rct, scr.rct)
        self.speedX *= yoko
        self.speedY *= tate
        self.blit(scr)


class Attack(pg.sprite.Sprite):
    def __init__(self, img, speed):
        pg.sprite.Sprite.__init__(self)
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.1)
        self.rct = self.sfc.get_rect()
        self.speed = speed
        self.status = False

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def shot(self, bird: Bird, scr: Screen):
        self.rct.centerx = bird.rct.centerx
        self.rct.centery = bird.rct.centery
        self.blit(scr)
        self.status = True

    def update(self, scr: Screen):
        if self.status == True:
            self.rct.centery -= self.speed
            if self.rct.top <= 0:
                self.kill()
            self.blit(scr)


class Guard:
    global guard_status

    def __init__(self, img):
        self.sfc = pg.image.load(img)
        self.sfc = pg.transform.rotozoom(self.sfc, 0, 0.2)
        self.rct = self.sfc.get_rect()

    def blit(self, scr: Screen):
        scr.sfc.blit(self.sfc, self.rct)

    def update(self, scr: Screen, bird: Bird):
        if guard_status == True:
            self.rct.centerx = bird.rct.centerx
            self.rct.centery = bird.rct.centery
            self.blit(scr)


def check_bound(obj_rct, scr_rct):
    """
    第1引数：こうかとんrectまたは爆弾rect
    第2引数：スクリーンrect
    範囲内：+1／範囲外：-1
    """
    yoko, tate = +1, +1
    if obj_rct.left < scr_rct.left or scr_rct.right < obj_rct.right:
        yoko = -1
    if obj_rct.top < scr_rct.top or scr_rct.bottom < obj_rct.bottom:
        tate = -1
    return yoko, tate


def main():
    global guard_status

    scr = Screen("逃げろ！こうかとん", (1600, 900), "fig/pg_bg.jpg")
    kkt = Bird("fig/6.png", 2.0, (900, 400))
    bkd = Bomb((255, 0, 0), 15, (+1, +1), scr)
    bkd2 = Bomb((255, 0, 0), 15, (+1, +1), scr)
    atk = Attack("fig/ball.png", 1)
    shield = Guard("fig/shield.png")

    clock = pg.time.Clock()
    while True:
        keystate = pg.key.get_pressed()
        if keystate[pg.K_SPACE]:
            atk.shot(kkt, scr)
        if keystate[pg.K_z]:
            guard_status = True
        else:
            guard_status = False

        scr.blit()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

        kkt.update(scr)
        atk.update(scr)
        shield.update(scr, kkt)

        bkd.update(scr)
        bkd2.update(scr)

        if kkt.rct.colliderect(bkd.rct) or kkt.rct.colliderect(bkd2.rct):
            if not guard_status:
                return

        pg.display.update()
        clock.tick(1000)


if __name__ == "__main__":
    pg.init()  # 初期化
    main()    # ゲームの本体
    pg.quit()  # 初期化の解除
    sys.exit()
