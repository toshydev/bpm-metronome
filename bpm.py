import time
import pygame as pg

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

def run():
    pg.init()
    icon = pg.image.load('data/bpm_icon.png')
    pg.display.set_icon(icon)
    bpm = 0
    default_font = "Caskaydia Cove Nerd Font Complete Mono Windows Compatible"

    screen = pg.display.set_mode(size=(300,300))
    pg.display.set_caption("BPM-Calculator")
    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill("gray10")

    if pg.font:
        font = pg.font.SysFont(default_font, 24)
        text = font.render("tap 'SPACE' to begin, 'q' to quit", True, "white")
        textpos = text.get_rect(centerx=background.get_width()/2, centery=background.get_height()/2)
        background.blit(text, textpos)

    screen.blit(background, (0, 0))
    pg.display.flip()

    clock = pg.time.Clock()

    start = time.time()
    
    going = True
    while going:
        clock.tick(60)
        if pg.key.get_pressed()[pg.K_SPACE]:
            bpm = round(60/(time.time()-start))
            if pg.font:
                font_instr = pg.font.SysFont(default_font, 24)
                text_instr = font_instr.render("tap 'SPACE' to calculate, 'q' to quit", True, "white")
                font_bpm = pg.font.SysFont(default_font, 64)
                text_bpm = font_bpm.render(f"{bpm}", True, "turquoise1")
                textpos = text_bpm.get_rect(centerx=background.get_width() / 2, centery=background.get_height() / 2)
                background.fill("gray10")
                background.blit(text_instr, (10, 10))
                background.blit(text_bpm, textpos)
            start = time.time()
            time.sleep(0.15)
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_q] or pg.key.get_pressed()[pg.K_ESCAPE]:
                going = False
        
        screen.blit(background, (0, 0))
        pg.display.flip()
        
    pg.quit()
        

if __name__ == "__main__":
    run()