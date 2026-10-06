"""
make_icon.py — упрощённая иконка: змея обвивает букву P.
- Фон: изумрудный градиент
- Буква P: однотонная светлая, белая обводка, тень
- Змея: тень, глаза с бликами справа, простые пятна, толстый язык
- Безопасная зона: ~12% от краёв
"""
from PIL import Image, ImageDraw, ImageFont
import math
import os
import random


def make_icon(output_path="icon.png", size=512, seed=7):
    random.seed(seed)

    # --- 1. Градиентный фон ---
    img = Image.new("RGB", (size, size))
    px = img.load()
    c1 = (12, 45, 35)
    c2 = (20, 160, 105)
    for y in range(size):
        for x in range(size):
            t = (x * 0.6 + y) / (size * 1.6)
            r = int(c1[0] + (c2[0] - c1[0]) * t)
            g = int(c1[1] + (c2[1] - c1[1]) * t)
            b = int(c1[2] + (c2[2] - c1[2]) * t)
            px[x, y] = (r, g, b)

    draw = ImageDraw.Draw(img, "RGBA")

    # --- Параметры тени ---
    SH_DX = int(size * 0.012)
    SH_DY = int(size * 0.016)
    SHADOW_RGBA = (0, 0, 0, 95)

    # --- 2. Буква P ---
    font = None
    for fn in ["arialbd.ttf", "Arial Bold.ttf", "DejaVuSans-Bold.ttf"]:
        try:
            font = ImageFont.truetype(fn, int(size * 0.52))
            break
        except (OSError, IOError):
            continue
    if font is None:
        font = ImageFont.load_default()

    text = "P"
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    tx = (size - w) / 2 - bbox[0]
    ty = (size - h) / 2 - bbox[1]

    # 2.1. Тень буквы P
    mask_sh = Image.new("L", (size, size), 0)
    d_sh = ImageDraw.Draw(mask_sh)
    d_sh.text((tx + SH_DX, ty + SH_DY), text, fill=110, font=font,
              stroke_width=12, stroke_fill=110)
    img.paste((0, 0, 0), mask=mask_sh)

    # --- Параметры змеи ---
    cx = size * 0.50
    cy = size * 0.50

    body_color = (124, 179, 66)
    body_dark = (46, 90, 30)
    outline = (15, 45, 20)

    spiral_r = size * 0.33
    turns = 300 / 360
    start_angle = 90
    end_angle = start_angle - 360 * turns

    N_sp = 400
    spiral_pts = []
    for i in range(N_sp):
        t = i / (N_sp - 1)
        a = math.radians(start_angle + (end_angle - start_angle) * t)
        r = spiral_r - t * size * 0.05
        y_off = -t * size * 0.03
        x = cx + r * math.cos(a)
        y = cy + r * math.sin(a) + y_off
        spiral_pts.append((x, y))

    # --- Хвост ---
    entry_x, entry_y = spiral_pts[0]
    tail_start_pt = (size * 0.16, size * 0.78)
    tail_end_pt = (entry_x, entry_y)

    N_tail = 90
    tail_pts = []
    for i in range(N_tail):
        t = i / (N_tail - 1)
        bx = tail_start_pt[0] + (tail_end_pt[0] - tail_start_pt[0]) * t
        by = tail_start_pt[1] + (tail_end_pt[1] - tail_start_pt[1]) * t
        bx += math.sin(t * 2.2 * math.pi) * size * 0.012 * (1 - t)
        by += math.cos(t * 2.6 * math.pi) * size * 0.022 * (1 - t)
        tail_pts.append((bx, by))

    all_pts = tail_pts + spiral_pts
    n = len(all_pts)

    BODY_R = size * 0.036

    def thickness(i):
        t = i / (n - 1)
        if t < 0.25:
            return size * 0.006 + (t / 0.25) * (BODY_R - size * 0.006)
        return BODY_R

    # --- 3. Тень змеи ---
    for i in range(n):
        x, y = all_pts[i]
        r = thickness(i) + 3
        draw.ellipse([x - r + SH_DX, y - r + SH_DY,
                      x + r + SH_DX, y + r + SH_DY],
                     fill=SHADOW_RGBA)

    # --- 4. Белая обводка буквы P ---
    mask_outer = Image.new("L", (size, size), 0)
    d_out = ImageDraw.Draw(mask_outer)
    d_out.text((tx, ty), text, fill=255, font=font,
               stroke_width=12, stroke_fill=255)
    img.paste((255, 255, 255), mask=mask_outer)

    # --- 5. Однотонная заливка P ---
    mask_inner = Image.new("L", (size, size), 0)
    d_in = ImageDraw.Draw(mask_inner)
    d_in.text((tx, ty), text, fill=255, font=font)
    img.paste((175, 235, 130), mask=mask_inner)

    # --- 6. Тело змеи ---
    # 6.1. Контур
    for i in range(n):
        x, y = all_pts[i]
        r = thickness(i) + 3
        draw.ellipse([x - r, y - r, x + r, y + r], fill=outline)
    # 6.2. Заливка
    for i in range(n):
        x, y = all_pts[i]
        r = thickness(i)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=body_color)

    # --- 7. Пятна ---
    spiral_start_idx = len(tail_pts) + 30
    spiral_end_idx = n - 35
    step = max(1, (spiral_end_idx - spiral_start_idx) // 6)

    side = 1
    for i in range(spiral_start_idx, spiral_end_idx, step):
        x_, y_ = all_pts[i]
        th = thickness(i)
        x2, y2 = all_pts[min(i + 5, n - 1)]
        dx, dy = x2 - x_, y2 - y_
        ang = math.atan2(dy, dx)
        perp = ang + math.pi / 2 * side

        off = th * 0.45
        bcx = x_ + math.cos(perp) * off
        bcy = y_ + math.sin(perp) * off

        br = th * 0.55
        draw.ellipse([bcx - br, bcy - br, bcx + br, bcy + br],
                     fill=body_dark)
        side = -side

    # --- 8. Голова ---
    hx, hy = all_pts[-1]
    head_w = size * 0.100
    head_h = size * 0.110

    # 8.1. Тень головы
    draw.ellipse(
        [hx - head_w + SH_DX, hy - head_h * 0.55 + SH_DY,
         hx + head_w + SH_DX, hy + head_h * 1.35 + SH_DY],
        fill=SHADOW_RGBA,
    )
    # 8.2. Овал головы
    draw.ellipse(
        [hx - head_w, hy - head_h * 0.55,
         hx + head_w, hy + head_h * 1.35],
        fill=body_color, outline=outline, width=4,
    )

    # --- 9. Глаза с бликами — оба блика справа ---
    eye_r = size * 0.038
    for sign in (-1, 1):
        ex = hx + sign * head_w * 0.42
        ey = hy + head_h * 0.35

        # Белок
        draw.ellipse(
            [ex - eye_r, ey - eye_r * 1.05,
             ex + eye_r, ey + eye_r * 1.05],
            fill="white", outline="black", width=3,
        )

        # Зрачок
        pup = eye_r * 0.55
        draw.ellipse(
            [ex - pup, ey - pup, ex + pup, ey + pup],
            fill="black",
        )

        # Блик — всегда справа от зрачка (и у левого, и у правого глаза)
        hl_r = pup * 0.42
        hl_x = ex + pup * 0.35   # всегда вправо
        hl_y = ey - pup * 0.45   # чуть выше центра
        draw.ellipse(
            [hl_x - hl_r, hl_y - hl_r,
             hl_x + hl_r, hl_y + hl_r],
            fill="white",
        )

    # --- 10. Улыбка ---
    sm_w = head_w * 0.45
    mouth_top = hy + head_h * 0.70
    mouth_bottom = mouth_top + sm_w * 1.1

    draw.arc(
        [hx - sm_w, mouth_top, hx + sm_w, mouth_bottom],
        0, 180, fill="black", width=3,
    )

    # --- 11. Толстый язычок ---
    ty1 = mouth_bottom
    ty2 = ty1 + size * 0.028
    draw.line([(hx, ty1), (hx, ty2)], fill=(220, 20, 60), width=6)
    draw.line([(hx, ty2), (hx - size * 0.014, ty2 + size * 0.020)],
              fill=(220, 20, 60), width=6)
    draw.line([(hx, ty2), (hx + size * 0.014, ty2 + size * 0.020)],
              fill=(220, 20, 60), width=6)

    img.save(output_path, "PNG")
    print(f"OK: {os.path.abspath(output_path)}")


if __name__ == "__main__":
    make_icon()
    for s in (192, 144, 96, 72, 48):
        make_icon(f"icon_{s}.png", size=s)
        