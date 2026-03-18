#!/usr/bin/env python3
"""
Feliz Cumpleaños Michelle ♡
Un mensaje especial de Santi

Cómo correr:
    pip install pygame
    python feliz_cumple.py

Asegúrate de que 'michelle.jpg' esté en la misma carpeta que este script.
"""

import pygame
import sys
import random
import math
import os

pygame.init()

# ─────────────────────────────────────────────────────────────────
#  CONFIGURACIÓN
# ─────────────────────────────────────────────────────────────────
WIDTH, HEIGHT = 1300, 750
FPS = 60

IMG_REVEAL_SPEED = 0.0014   # fracción revelada por frame (~12s para imagen completa)
CHAR_DELAY_MS    = 22       # ms entre cada carácter del texto

# Colores
BG       = (10, 8, 20)
TEXT_COL = (240, 230, 220)
PINK     = (255, 150, 180)
GOLD     = (255, 210, 80)
LAVENDER = (190, 165, 255)
WHITE    = (255, 255, 255)
TEAL     = (100, 220, 210)

# ─────────────────────────────────────────────────────────────────
#  PANTALLA
# ─────────────────────────────────────────────────────────────────
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Feliz Cumpleanios Michelle")
clock = pygame.time.Clock()

# ─────────────────────────────────────────────────────────────────
#  FUENTES
# ─────────────────────────────────────────────────────────────────
def load_font(size, bold=False):
    candidates = ["Segoe UI", "Ubuntu", "DejaVu Sans", "Liberation Sans", "Arial"]
    for name in candidates:
        try:
            f = pygame.font.SysFont(name, size, bold=bold)
            if f:
                return f
        except Exception:
            pass
    return pygame.font.Font(None, size)

FONT_TEXT  = load_font(16)
FONT_TITLE = load_font(22, bold=True)
FONT_SIGN  = load_font(17, bold=True)
LINE_H     = FONT_TEXT.get_linesize() + 3

# ─────────────────────────────────────────────────────────────────
#  MENSAJE
# ─────────────────────────────────────────────────────────────────
MESSAGE = """\
Micheeeelle, hiiii jeje. Primero que nada, FELIZ CUMPLEEEE. Lamento no estar en tu librito, pero luego de estar sobreviviendo en Pforzheim juntos por un semestre mas con los demas, considero que mereces un esfuerzo mayor de mi parte a mandarle mi texto a Miriam para que ella lo transcriba (que se aprecia mucho porque es un chambon).

Ahora, no tenia ni fokin idea de que hacerte. Veia a Naye avanzando el librito, a Sebas dibujando tremendo cartel y yo ahi con mi nula habilidad para las manualidades como wbn sin hacer nada :').

Entonces se me ocurrio hacerte algo en lo que si soy bueno, que es con la computadora basicamente (un poco geek de mi parte? puede ser, pero ya me conoces ya).

Asi que nada, este codiguito es para ti. Espero que te guste. Ahora si se viene el textazo ehhhhhh (aviso que probablemente me vaya en floro. Voy escribiendo sobre la marcha):

Bueno, incluso antes de conocerte, yo ya sabia la increible persona que eras. Me acuerdo que Naye llego una madrugada a contarme que habia ido a patinar con un grupo de chicas muy divertidas y que la habia pasado increible. Me alegro verla llegar feliz y dije: ojala conocerlas algun dia (no se volvieron a ver en todo el semestre).

Ya el segundo semestre cada vez llegaba con mas historias con ustedes, ya por fin les puse nombre y me hablaba de lo especialmente bien que se entendia con una tal Michelle, una chica super linda, muy graciosa, con una gran personalidad y que le hacia sentir comoda de nuevo (en Pforzheim ps). Y asi me iba contando de ti, de sus planes y de como le ayudaba y le alegraba tu mera existencia. Ya desde ahi te agarre carino sin haber interactuado contigo si quiera, por lo buena persona y excelente amiga que le demostrabas ser. Yo solo escuchaba y pensaba: mrd, que linda persona, quisiera conocerla.

Ya cuando me toco conocerte pude ir confirmando poco a poco todo lo que Naye me conto en algun momento: la muy linda personalidad que tienes, lo graciosa que eres y la increible amiga que puedes llegar a ser. Y este ultimo semestre, me siento muy afortunado de haber podido conocer y conectar aun mas con esta increible mujer, ver lo inteligente y capa que es, los grandes valores que mantiene, lo mucho que se puede llegar a presionar y lo valiente que es para seguir adelante y cumplir lo que se ha propuesto.

Eeeesa Michelle demorona, que le encanta fregar con cualquier cosa y hacer los chistes mas desubicados (no cambies nunca, me haces reir demasiado), que se pone de malas cuando tiene sueno, que escucha playlists de lluvia para estudiar y que le cuesta mucho hablar en camara. Todas esas cosas, y muchas mas que seguro ahora mismo se me pasan, que te convierten en esa persona que todos queremos demasiado.

Realmente espero que pases un muy feliz cumpleanos, vacilate, divierte y sonrie muchisimo. Te mereces todo lo bueno del mundo verdaderamente. Se que estos ultimos meses han sido especialmente dificiles (y para que enganarnos? No se hace mas facil con el tiempo), pero ya te has demostrado a ti misma y a todos lo que puedes lograr. Y uno se derrumba a veces, pero te aseguro que nunca te va a faltar gente dispuesta a apoyarte siempre que lo necesites: tu familia, las chicas, Sebas, yo, etc, etc, etc.

Y bueno, en realidad no se que mas decirte Michelle, se me fue la inspiracion, solo que te quiero muchisimo, estoy muy orgulloso de ti, te admiro demasiado y te mando mis mejores deseos para este dia y para el resto de tu vida y un FUERTE FUERTE ABRAZO. Te debo el estar presente en alguno de tus cumples jajsajjs y si Dios quiere nos volveremos a ver pronto. Por mientras ya estamos hablando estos dias seguramente (a tu ritmo claro esta JAJJAJA).

Sinceramente, no se que tan largo me quedo esto ni cuanto tardare en compilarlo, pero esperemos que salga bien, yo confio. Y eso seria todo creo, pasala lindo Michelle, me despido. BYEEEEEEE

                                                      Te quiere, Santi <3"""

# ─────────────────────────────────────────────────────────────────
#  UTILIDAD: WRAP DE TEXTO
# ─────────────────────────────────────────────────────────────────
def wrap_text(text, font, max_width):
    result = []
    for paragraph in text.split('\n'):
        if not paragraph.strip():
            result.append('')
            continue
        words = paragraph.split(' ')
        line = ''
        for word in words:
            test = (line + ' ' + word).strip()
            if font.size(test)[0] <= max_width:
                line = test
            else:
                if line:
                    result.append(line)
                line = word
        if line:
            result.append(line)
    return result

# ─────────────────────────────────────────────────────────────────
#  IMAGEN
# ─────────────────────────────────────────────────────────────────
IMG_AREA_W = 490
IMG_AREA_H = HEIGHT - 80
IMG_AREA_X = 15
IMG_AREA_Y = 40

script_dir = os.path.dirname(os.path.abspath(__file__))
img_path   = os.path.join(script_dir, "michelle.jpg")

image = None
iw, ih = IMG_AREA_W, IMG_AREA_H
img_x, img_y = IMG_AREA_X, IMG_AREA_Y

try:
    raw = pygame.image.load(img_path)
    rw, rh = raw.get_size()
    scale = min(IMG_AREA_W / rw, IMG_AREA_H / rh)
    iw, ih = int(rw * scale), int(rh * scale)
    image = pygame.transform.smoothscale(raw, (iw, ih))
    img_x = IMG_AREA_X + (IMG_AREA_W - iw) // 2
    img_y = IMG_AREA_Y + (IMG_AREA_H - ih) // 2
    print(f"Imagen cargada: {iw}x{ih}")
except Exception as e:
    print(f"[!] No se pudo cargar 'michelle.jpg': {e}")
    print("    Asegurate de que el archivo esta en la misma carpeta que el script.")

# ─────────────────────────────────────────────────────────────────
#  AREA DE TEXTO
# ─────────────────────────────────────────────────────────────────
TEXT_X = IMG_AREA_X + IMG_AREA_W + 28
TEXT_W = WIDTH - TEXT_X - 18
TEXT_Y = 55
TEXT_H = HEIGHT - TEXT_Y - 20

all_lines   = wrap_text(MESSAGE, FONT_TEXT, TEXT_W - 12)
total_chars = sum(len(ln) + 1 for ln in all_lines)

# ─────────────────────────────────────────────────────────────────
#  PARTÍCULAS FLOTANTES
# ─────────────────────────────────────────────────────────────────
PARTICLE_COLORS = [PINK, GOLD, LAVENDER, WHITE, TEAL, (200, 255, 180)]

class Particle:
    def __init__(self):
        self.reset()

    def reset(self):
        self.x    = random.uniform(0, WIDTH)
        self.y    = random.uniform(0, HEIGHT)
        self.size = random.randint(1, 3)
        self.color = random.choice(PARTICLE_COLORS)
        self.life  = random.randint(70, 160)
        self.max_life = self.life
        self.vx   = random.uniform(-0.3, 0.3)
        self.vy   = random.uniform(-0.7, -0.15)
        self.phase = random.uniform(0, math.pi * 2)

    def update(self):
        self.x    += self.vx + 0.3 * math.sin(self.life * 0.08 + self.phase)
        self.y    += self.vy
        self.life -= 1
        return self.life > 0

    def draw(self, surface):
        ratio = self.life / self.max_life
        alpha = int(220 * ratio * (0.5 + 0.5 * math.sin(self.life * 0.15 + self.phase)))
        s = pygame.Surface((self.size * 2 + 2, self.size * 2 + 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha), (self.size + 1, self.size + 1), self.size)
        surface.blit(s, (int(self.x) - self.size - 1, int(self.y) - self.size - 1))

particles = [Particle() for _ in range(60)]

# ─────────────────────────────────────────────────────────────────
#  ESTADO DE ANIMACIÓN
# ─────────────────────────────────────────────────────────────────
img_reveal     = 0.0
chars_revealed = 0
last_char_tick = pygame.time.get_ticks()
text_scroll    = 0

# ─────────────────────────────────────────────────────────────────
#  HELPERS DE DIBUJO
# ─────────────────────────────────────────────────────────────────
def get_revealed_lines(all_lines, char_count):
    result = []
    remaining = char_count
    for line in all_lines:
        ll = len(line) + 1
        if remaining <= 0:
            break
        if remaining >= ll:
            result.append((line, len(line)))
            remaining -= ll
        else:
            result.append((line, remaining))
            break
    return result


def draw_image_reveal(surface, img, x, y, w, h, reveal):
    if img is None:
        # Placeholder si no hay imagen
        r = int(reveal * h)
        pygame.draw.rect(surface, (30, 25, 50), (x, y, w, r))
        msg = FONT_TEXT.render("[ michelle.jpg no encontrada ]", True, LAVENDER)
        surface.blit(msg, (x + 10, y + r // 2))
        return

    reveal_px = int(h * reveal)
    if reveal_px > 0:
        sub = img.subsurface((0, 0, w, reveal_px))
        surface.blit(sub, (x, y))

    # Línea de escaneo brillante
    if 0 < reveal < 1.0:
        scan_y = y + reveal_px
        for i in range(10):
            a = max(0, 160 - i * 17)
            gs = pygame.Surface((w, 2), pygame.SRCALPHA)
            glow_col = (200, 140, 255, a)
            gs.fill(glow_col)
            surface.blit(gs, (x, scan_y - i))
        # Destello más brillante en el frente
        bright = pygame.Surface((w, 3), pygame.SRCALPHA)
        bright.fill((240, 200, 255, 200))
        surface.blit(bright, (x, scan_y))


def draw_image_frame(surface, x, y, w, h, reveal):
    if reveal <= 0:
        return
    alpha_factor = min(1.0, reveal * 2)
    color = tuple(int(c * alpha_factor) for c in PINK)
    revealed_h = int(h * reveal)
    # Bordes del área revelada
    pygame.draw.rect(surface, color, (x - 2, y - 2, w + 4, revealed_h + 4), 2)


def draw_text_panel(surface, rev_lines, scroll_y, now, chars_done, total):
    clip_rect = pygame.Rect(TEXT_X, TEXT_Y, TEXT_W, TEXT_H)
    surface.set_clip(clip_rect)

    y_base = TEXT_Y - scroll_y

    for i, (line, chars) in enumerate(rev_lines):
        yp = y_base + i * LINE_H
        if yp + LINE_H < TEXT_Y or yp > TEXT_Y + TEXT_H:
            continue

        display = line[:chars]

        # Colores especiales según contenido
        upper = display.upper()
        if 'FELIZ CUMPLE' in upper or 'BYEEEEEEE' in upper:
            color = PINK
        elif 'TE QUIERE, SANTI' in upper or '<3' in display:
            color = GOLD
        elif display.startswith('Micheeeelle') or display.startswith('Asi que nada'):
            color = LAVENDER
        elif display.startswith('Eeeesa Michelle'):
            color = TEAL
        else:
            color = TEXT_COL

        rendered = FONT_TEXT.render(display, True, color)
        surface.blit(rendered, (TEXT_X + 6, yp))

        # Cursor parpadeante en la última línea
        if i == len(rev_lines) - 1 and chars_done < total:
            cx = TEXT_X + 6 + FONT_TEXT.size(display)[0]
            if (now // 500) % 2 == 0:
                pygame.draw.rect(surface, GOLD, (cx + 1, yp + 2, 2, LINE_H - 5))

    surface.set_clip(None)


def draw_title(surface, now):
    # Ligero efecto de pulso en el título
    pulse = 0.85 + 0.15 * math.sin(now * 0.002)
    base  = "  Feliz Cumpleanios Michelle  "
    hearts = "<3  " + base + "  <3"
    col   = tuple(int(c * pulse) for c in PINK)
    surf  = FONT_TITLE.render(hearts, True, col)
    x = TEXT_X
    y = 14
    surface.blit(surf, (x, y))


def draw_separator(surface, reveal):
    alpha = min(255, int(255 * reveal * 3))
    sep_x = TEXT_X - 16
    pygame.draw.line(
        surface,
        tuple(int(c * alpha / 255) for c in LAVENDER),
        (sep_x, TEXT_Y),
        (sep_x, HEIGHT - 20),
        1,
    )


# ─────────────────────────────────────────────────────────────────
#  LOOP PRINCIPAL
# ─────────────────────────────────────────────────────────────────
running = True

while running:
    clock.tick(FPS)
    now = pygame.time.get_ticks()

    # ── Eventos ──────────────────────────────────────────────────
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            # Espacio o Enter para saltar al final (por si es muy lento)
            if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                chars_revealed = total_chars
                img_reveal = 1.0

    # ── Actualizar imagen ─────────────────────────────────────────
    if img_reveal < 1.0:
        img_reveal = min(1.0, img_reveal + IMG_REVEAL_SPEED)

    # ── Actualizar texto ──────────────────────────────────────────
    if chars_revealed < total_chars:
        elapsed = now - last_char_tick
        if elapsed >= CHAR_DELAY_MS:
            add = max(1, elapsed // CHAR_DELAY_MS)
            chars_revealed = min(total_chars, chars_revealed + add)
            last_char_tick = now

    # ── Auto-scroll ───────────────────────────────────────────────
    rev_lines     = get_revealed_lines(all_lines, chars_revealed)
    total_text_h  = len(rev_lines) * LINE_H
    target_scroll = max(0, total_text_h - TEXT_H)
    # Suavizado del scroll
    text_scroll += (target_scroll - text_scroll) * 0.12

    # ── Partículas ────────────────────────────────────────────────
    if random.random() < 0.35:
        particles.append(Particle())
    particles = [p for p in particles if p.update()]

    # ── Dibujar ───────────────────────────────────────────────────
    screen.fill(BG)

    # Imagen
    draw_image_reveal(screen, image, img_x, img_y, iw, ih, img_reveal)
    draw_image_frame(screen, img_x, img_y, iw, ih, img_reveal)

    # Separador vertical
    draw_separator(screen, img_reveal)

    # Título
    draw_title(screen, now)

    # Texto
    draw_text_panel(screen, rev_lines, int(text_scroll), now, chars_revealed, total_chars)

    # Partículas
    for p in particles:
        p.draw(screen)

    # Hint de tecla (desaparece después de 5s)
    if now < 5000:
        hint = FONT_TEXT.render("ESC = salir  |  ESPACIO = saltar animacion", True, (80, 70, 100))
        screen.blit(hint, (WIDTH - hint.get_width() - 10, HEIGHT - 22))

    pygame.display.flip()

pygame.quit()
sys.exit()
