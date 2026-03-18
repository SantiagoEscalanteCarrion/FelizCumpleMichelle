#!/usr/bin/env python3
"""
Feliz Cumpleanos Michelle <3
Un regalo de Santi

Ejecutar:
    pip install pygame
    python feliz_cumple.py

La imagen 'michelle.jpg' debe estar en la misma carpeta que este script.
"""

import pygame
import sys
import random
import math
import os

pygame.init()

# ─────────────────────────────────────────────────────────────────
#  CONFIGURACION
# ─────────────────────────────────────────────────────────────────
WIDTH, HEIGHT     = 1300, 750
FPS               = 60
CHAR_DELAY_MS     = 22      # ms por caracter

# Brush stroke reveal
TOTAL_STROKES     = 900     # trazos totales para revelar imagen
STROKES_PER_FRAME = 1.6     # trazos por frame  → ~9-10 segundos

# Colores
BG          = (10, 8, 20)
TURQUOISE   = (75, 210, 200)      # texto principal
LIGHT_GREEN = (140, 225, 140)     # resaltados (FELIZ CUMPLE, BYEEEEEEE)
GOLD        = (255, 210, 80)      # firma
LAVENDER    = (190, 165, 255)     # primera linea
CAPTION_COL = (150, 140, 185)     # pie de foto
SCROLL_BG   = (30, 25, 50)
SCROLL_THUMB= (100, 90, 145)

# ─────────────────────────────────────────────────────────────────
#  PANTALLA
# ─────────────────────────────────────────────────────────────────
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Feliz Cumpleanios Michelle")
clock  = pygame.time.Clock()

# ─────────────────────────────────────────────────────────────────
#  FUENTES
# ─────────────────────────────────────────────────────────────────
def load_font(size, bold=False):
    for name in ["Segoe UI", "Ubuntu", "DejaVu Sans", "Liberation Sans", "Arial"]:
        try:
            f = pygame.font.SysFont(name, size, bold=bold)
            if f:
                return f
        except Exception:
            pass
    return pygame.font.Font(None, size)

FONT_TEXT    = load_font(16)
FONT_TITLE   = load_font(22, bold=True)
FONT_CAPTION = load_font(13)
LINE_H       = FONT_TEXT.get_linesize() + 3

# ─────────────────────────────────────────────────────────────────
#  MENSAJE
# ─────────────────────────────────────────────────────────────────
MESSAGE = """\
Micheeeelle, hiiii jeje. Primero que nada, FELIZ CUMPLEEEE. Lamento no estar en tu librito, pero luego de estar sobreviviendo en Pforzheim juntos por un semestre mas con los demas, considero que mereces un esfuerzo mayor de mi parte a mandarle mi texto a Miriam para que ella lo transcriba (que se aprecia mucho porque es un chambon).

Ahora, no tenia ni fokin idea de que hacerte. Veia a Naye avanzando el librito, a Sebas dibujando tremendo cartel y yo ahi con mi nula habilidad para las manualidades como wbn sin hacer nada :').

Entonces se me ocurrio hacerte algo en lo que si soy bueno, que es con la computadora basicamente (un poco geek de mi parte? puede ser, pero ya me conoces ya).

Asi que nada, este codiguito es para ti, un regalo mucho mas a mi estilo jeje. Espero que te guste. Ahora si se viene el textazo ehhhhhh (aviso que probablemente me vaya en floro. Voy escribiendo sobre la marcha):

Bueno, incluso antes de conocerte, yo ya sabia la increible persona que eras. Me acuerdo que Naye llego una madrugada a contarme que habia ido a patinar con un grupo de chicas muy divertidas y que la habia pasado increible. Me alegro verla llegar feliz y dije: ojala conocerlas algun dia (no se volvieron a ver en todo el semestre).

Ya el segundo semestre cada vez llegaba con mas historias con ustedes, ya por fin les puse nombre y me hablaba de lo especialmente bien que se entendia con una tal Michelle, una chica super linda, muy graciosa, con una gran personalidad y que le hacia sentir comoda de nuevo (en Pforzheim ps). Y asi me iba contando de ti, de sus planes y de como le ayudaba y le alegraba tu mera existencia. Ya desde ahi te agarre carino sin haber interactuado contigo si quiera, por lo buena persona y excelente amiga que le demostrabas ser. Yo solo escuchaba y pensaba: mrd, que linda persona, quisiera conocerla.

Ya cuando me toco conocerte pude ir confirmando poco a poco todo lo que Naye me conto en algun momento: la muy linda personalidad que tienes, lo graciosa que eres y la increible amiga que puedes llegar a ser. Y este ultimo semestre, me siento muy afortunado de haber podido conocer y conectar aun mas con esta increible mujer, ver lo inteligente y capa que es, los grandes valores que mantiene, lo mucho que se puede llegar a presionar y lo valiente que es para seguir adelante y cumplir lo que se ha propuesto.

Eeeesa Michelle demorona, que le encanta fregar con cualquier cosa y hacer los chistes mas desubicados (no cambies nunca, me haces reir demasiado), que se pone de malas cuando tiene sueno, que escucha playlists de lluvia para estudiar y que le cuesta mucho hablar en camara. Todas esas cosas, y muchas mas que seguro ahora mismo se me pasan, que te convierten en esa persona que todos queremos demasiado.

Realmente espero que pases un muy feliz cumpleanos, vacilate, divierte y sonrie muchisimo. Te mereces todo lo bueno del mundo verdaderamente. Se que estos ultimos meses han sido especialmente dificiles (y para que enganarnos? No se hace mas facil con el tiempo), pero ya te has demostrado a ti misma y a todos lo que puedes lograr. Y uno se derrumba a veces, pero te aseguro que nunca te va a faltar gente dispuesta a apoyarte siempre que lo necesites: tu familia, las chicas, Sebas, yo, etc, etc, etc.

Y bueno, en realidad no se que mas decirte Michelle, se me fue la inspiracion, solo que te quiero muchisimo, estoy muy orgulloso de ti, te admiro demasiado y te mando mis mejores deseos para este dia y para el resto de tu vida y un FUERTE FUERTE ABRAZO. Te debo el estar presente en alguno de tus cumples jajsajjs y si Dios quiere nos volveremos a ver pronto. Por mientras ya estamos hablando estos dias seguramente (a tu ritmo claro esta JAJJAJA).

Sinceramente, no se que tan largo me quedo esto ni cuanto tardare en compilarlo, pero esperemos que salga bien, yo confio. Y eso seria todo creo, pasala lindo Michelle, me despido. BYEEEEEEE

                                                      Te quiere, Santi <3"""

# ─────────────────────────────────────────────────────────────────
#  PATH HELPER (compatible con PyInstaller --onefile)
# ─────────────────────────────────────────────────────────────────
def resource_path(rel):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, rel)
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), rel)

# ─────────────────────────────────────────────────────────────────
#  IMAGEN + BRUSH STROKE MASK
# ─────────────────────────────────────────────────────────────────
IMG_AREA_W = 490
IMG_AREA_H = HEIGHT - 115
IMG_AREA_X = 15
IMG_AREA_Y = 38

image = None
iw, ih = IMG_AREA_W, IMG_AREA_H
img_x, img_y = IMG_AREA_X, IMG_AREA_Y

try:
    raw   = pygame.image.load(resource_path("michelle.jpg"))
    rw, rh = raw.get_size()
    scale  = min(IMG_AREA_W / rw, IMG_AREA_H / rh)
    iw, ih = int(rw * scale), int(rh * scale)
    image  = pygame.transform.smoothscale(raw, (iw, ih))
    img_x  = IMG_AREA_X + (IMG_AREA_W - iw) // 2
    img_y  = IMG_AREA_Y + (IMG_AREA_H - ih) // 2
    print(f"Imagen cargada: {iw}x{ih}")
except Exception as e:
    print(f"[!] No se pudo cargar 'michelle.jpg': {e}")

CAPTION_TEXT = "La unica foto que tenemos juntos dio mio"

# Preparar mascara de reveal y trazos
reveal_mask        = None
strokes_data       = []
strokes_done_f     = 0.0
strokes_done       = 0
img_fully_revealed = False

if image:
    reveal_mask = pygame.Surface((iw, ih), pygame.SRCALPHA)
    reveal_mask.fill((0, 0, 0, 255))   # negro opaco = imagen oculta

    random.seed(42)   # seed fijo para consistencia
    for _ in range(TOTAL_STROKES):
        x  = random.randint(-35, iw + 35)
        y  = random.randint(-35, ih + 35)
        roll = random.random()
        if roll < 0.12:
            r = random.randint(4, 16)     # trazos finos (detalle)
        elif roll < 0.82:
            r = random.randint(16, 48)    # trazos medios (cuerpo)
        else:
            r = random.randint(48, 85)    # trazos grandes (relleno)
        aspect = random.uniform(0.45, 1.9)
        wr = max(3, int(r * aspect))
        hr = max(3, int(r / aspect))
        strokes_data.append((x, y, wr, hr))
    random.seed()   # restaurar semilla aleatoria

# ─────────────────────────────────────────────────────────────────
#  AREA DE TEXTO
# ─────────────────────────────────────────────────────────────────
SCROLLBAR_W = 7
SCROLLBAR_X = WIDTH - 16
TEXT_X = IMG_AREA_X + IMG_AREA_W + 28
TEXT_W = WIDTH - TEXT_X - SCROLLBAR_W - 20
TEXT_Y = 52
TEXT_H = HEIGHT - TEXT_Y - 20

def wrap_text(text, font, max_width):
    result = []
    for para in text.split('\n'):
        if not para.strip():
            result.append('')
            continue
        words = para.split(' ')
        line  = ''
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

all_lines    = wrap_text(MESSAGE, FONT_TEXT, TEXT_W - 6)
total_chars  = sum(len(ln) + 1 for ln in all_lines)
total_text_h = len(all_lines) * LINE_H

def get_revealed_lines(char_count):
    result    = []
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

def line_color(line):
    up = line.upper()
    if 'FELIZ CUMPLE' in up or 'BYEEEEEEE' in up:
        return LIGHT_GREEN
    if 'TE QUIERE, SANTI' in up or line.strip().endswith('<3'):
        return GOLD
    if line.startswith('Micheeeelle'):
        return LAVENDER
    return TURQUOISE

# ─────────────────────────────────────────────────────────────────
#  PARTICULAS FLOTANTES
# ─────────────────────────────────────────────────────────────────
PCOLS = [LIGHT_GREEN, GOLD, LAVENDER, (255, 255, 255), TURQUOISE, (200, 255, 200)]

class Particle:
    def __init__(self):
        self.x     = random.uniform(0, WIDTH)
        self.y     = random.uniform(0, HEIGHT)
        self.size  = random.randint(1, 3)
        self.color = random.choice(PCOLS)
        self.life  = random.randint(70, 160)
        self.max_l = self.life
        self.vx    = random.uniform(-0.3, 0.3)
        self.vy    = random.uniform(-0.7, -0.15)
        self.phase = random.uniform(0, math.pi * 2)

    def update(self):
        self.x += self.vx + 0.25 * math.sin(self.life * 0.08 + self.phase)
        self.y += self.vy
        self.life -= 1
        return self.life > 0

    def draw(self, surface):
        alpha = int(200 * (self.life / self.max_l) *
                    (0.5 + 0.5 * math.sin(self.life * 0.15 + self.phase)))
        s = pygame.Surface((self.size * 2 + 2, self.size * 2 + 2), pygame.SRCALPHA)
        pygame.draw.circle(s, (*self.color, alpha),
                           (self.size + 1, self.size + 1), self.size)
        surface.blit(s, (int(self.x) - self.size - 1, int(self.y) - self.size - 1))

particles = [Particle() for _ in range(55)]

# ─────────────────────────────────────────────────────────────────
#  ESTADO DE ANIMACION
# ─────────────────────────────────────────────────────────────────
chars_revealed = 0
last_char_tick = pygame.time.get_ticks()

scroll_target  = 0     # destino del scroll (pixeles)
scroll_current = 0.0   # valor suavizado actual
auto_scroll    = True  # seguir el texto nuevo

# ─────────────────────────────────────────────────────────────────
#  SCROLLBAR
# ─────────────────────────────────────────────────────────────────
def draw_scrollbar(surface, scroll, max_scroll):
    if max_scroll <= 0:
        return
    pygame.draw.rect(surface, SCROLL_BG,
                     (SCROLLBAR_X, TEXT_Y, SCROLLBAR_W, TEXT_H), border_radius=4)
    visible_ratio = min(1.0, TEXT_H / total_text_h)
    thumb_h = max(20, int(TEXT_H * visible_ratio))
    scroll_ratio = scroll / max_scroll
    thumb_y = TEXT_Y + int((TEXT_H - thumb_h) * scroll_ratio)
    pygame.draw.rect(surface, SCROLL_THUMB,
                     (SCROLLBAR_X, thumb_y, SCROLLBAR_W, thumb_h), border_radius=4)

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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key in (pygame.K_SPACE, pygame.K_RETURN):
                # Saltar animacion
                chars_revealed  = total_chars
                strokes_done_f  = float(TOTAL_STROKES)
            elif event.key == pygame.K_DOWN:
                scroll_target = min(max(0, total_text_h - TEXT_H),
                                    scroll_target + LINE_H * 3)
                auto_scroll   = False
            elif event.key == pygame.K_UP:
                scroll_target = max(0, scroll_target - LINE_H * 3)
                auto_scroll   = False

        elif event.type == pygame.MOUSEWHEEL:
            max_s         = max(0, total_text_h - TEXT_H)
            scroll_target = max(0, min(max_s, scroll_target - event.y * LINE_H * 3))
            # Si el usuario scrollea hacia abajo hasta el fondo, reactivar auto
            if scroll_target >= max_s - LINE_H:
                auto_scroll = True
            else:
                auto_scroll = False

    # ── Actualizar brush stroke reveal ───────────────────────────
    if not img_fully_revealed and image and reveal_mask:
        strokes_done_f += STROKES_PER_FRAME
        target_int = min(TOTAL_STROKES, int(strokes_done_f))
        while strokes_done < target_int:
            x, y, wr, hr = strokes_data[strokes_done]
            pygame.draw.ellipse(reveal_mask, (0, 0, 0, 0),
                                (x - wr, y - hr, wr * 2, hr * 2))
            strokes_done += 1
        if strokes_done >= TOTAL_STROKES:
            img_fully_revealed = True
            reveal_mask = None   # liberar memoria

    # ── Actualizar texto ──────────────────────────────────────────
    if chars_revealed < total_chars:
        elapsed = now - last_char_tick
        if elapsed >= CHAR_DELAY_MS:
            add            = max(1, elapsed // CHAR_DELAY_MS)
            chars_revealed = min(total_chars, chars_revealed + add)
            last_char_tick = now

    # ── Auto-scroll ───────────────────────────────────────────────
    rev_lines    = get_revealed_lines(chars_revealed)
    current_h    = len(rev_lines) * LINE_H
    max_scroll   = max(0, total_text_h - TEXT_H)

    if auto_scroll and chars_revealed < total_chars:
        scroll_target = max(0, current_h - TEXT_H)

    # Suavizado del scroll
    scroll_current += (scroll_target - scroll_current) * 0.14

    # ── Particulas ────────────────────────────────────────────────
    if random.random() < 0.32:
        particles.append(Particle())
    particles = [p for p in particles if p.update()]

    # ─────────────────────────────────────────────────────────────
    #  DIBUJAR
    # ─────────────────────────────────────────────────────────────
    screen.fill(BG)

    # Imagen
    if image:
        screen.blit(image, (img_x, img_y))
        if reveal_mask:
            screen.blit(reveal_mask, (img_x, img_y))
        # Marco que aparece a medida que se revela
        reveal_pct = min(1.0, strokes_done / TOTAL_STROKES)
        fa = min(255, int(255 * reveal_pct * 2))
        fc = tuple(int(c * fa / 255) for c in LIGHT_GREEN)
        pygame.draw.rect(screen, fc, (img_x - 2, img_y - 2, iw + 4, ih + 4), 2)
    else:
        pygame.draw.rect(screen, (28, 22, 45), (img_x, img_y, iw, ih))
        ph = FONT_TEXT.render("[ michelle.jpg no encontrada ]", True, LAVENDER)
        screen.blit(ph, (img_x + 10, img_y + ih // 2 - 10))

    # Caption debajo de la imagen
    reveal_pct  = min(1.0, strokes_done / TOTAL_STROKES) if TOTAL_STROKES else 1.0
    cap_alpha   = int(255 * reveal_pct)
    if cap_alpha > 0:
        cap_surf = FONT_CAPTION.render(CAPTION_TEXT, True, CAPTION_COL)
        if cap_alpha < 255:
            cap_surf.set_alpha(cap_alpha)
        cx_cap = img_x + (iw - cap_surf.get_width()) // 2
        screen.blit(cap_surf, (cx_cap, img_y + ih + 8))

    # Separador vertical
    pygame.draw.line(screen, (55, 45, 85),
                     (TEXT_X - 16, TEXT_Y), (TEXT_X - 16, HEIGHT - 20), 1)

    # Titulo con pulso
    pulse      = 0.85 + 0.15 * math.sin(now * 0.002)
    title_col  = tuple(int(c * pulse) for c in LIGHT_GREEN)
    title_surf = FONT_TITLE.render("<3  Feliz Cumpleanios Michelle  <3", True, title_col)
    screen.blit(title_surf, (TEXT_X, 14))

    # ── Panel de texto con clipping ───────────────────────────────
    clip_rect = pygame.Rect(TEXT_X, TEXT_Y, TEXT_W, TEXT_H)
    screen.set_clip(clip_rect)

    y_base = TEXT_Y - int(scroll_current)
    for i, (line, chars) in enumerate(rev_lines):
        yp = y_base + i * LINE_H
        if yp + LINE_H < TEXT_Y or yp > TEXT_Y + TEXT_H:
            continue
        display  = line[:chars]
        rendered = FONT_TEXT.render(display, True, line_color(line))
        screen.blit(rendered, (TEXT_X + 6, yp))

        # Cursor parpadeante en la ultima linea siendo escrita
        if i == len(rev_lines) - 1 and chars_revealed < total_chars:
            cx2 = TEXT_X + 6 + FONT_TEXT.size(display)[0]
            if (now // 500) % 2 == 0:
                pygame.draw.rect(screen, GOLD, (cx2 + 1, yp + 2, 2, LINE_H - 5))

    screen.set_clip(None)

    # Scrollbar
    draw_scrollbar(screen, int(scroll_current), max_scroll)

    # Particulas
    for p in particles:
        p.draw(screen)

    # Hint (desaparece a los 5s)
    if now < 5500:
        hint = FONT_TEXT.render(
            "ESC = salir  |  ESPACIO = saltar animacion  |  rueda del raton / flechas = scroll",
            True, (65, 58, 95))
        screen.blit(hint, (WIDTH - hint.get_width() - 10, HEIGHT - 22))

    pygame.display.flip()

pygame.quit()
sys.exit()
