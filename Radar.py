# Пограмма "Симуляции радара" написанная на Python 3.12
# Автор: Dinger

# Библиотеки
import pygame as PG # Сокращаем pygame до PG
import math as M # Сокращаем math до M
import pyautogui as PAG # Сокращаем pyautogui до PAG



# Вычислительные функции
def sin(value): # Вычисляет синус
    sin = M.sin(value)
    return sin

def cos(value): # Вычисляет косинус
    cos = M.cos(value)
    return cos

def SqRt(value): # Вычисляет квадратный корень
    SqRt = M.sqrt(value)
    return SqRt

def flr(value): # Вычисляет округление до целого числа
    flr = M.floor(value)
    return flr

def rads(value): # Переводит углы в радианы
    rads = M.radians(value)
    return rads

def LenVctr(x, y): # Вычисляет длина вектора
    LenVctr = SqRt(x ** 2 + y ** 2)
    return LenVctr

def ActAng(number, value): # Вычисляет активный угол
    if number == 0: # Если number = 0, то
        ang2 = CtrWin[0] + DynRad * cos(ang - rads(value))
        return ang2

    if number == 1: # Если number = 1, то
        ang2 = CtrWin[1] + DynRad * sin(ang - rads(value))
        return ang2

# Функции рисования
def DrawCir(): # Рисует круги сетки
    PG.draw.circle(win, Clr4, CtrWin, lrg, WidGrid) # Большой круг
    PG.draw.circle(win, Clr4, CtrWin, med, WidGrid) # Средний круг
    PG.draw.circle(win, Clr4, CtrWin, sml, WidGrid) # Малый круг

def DrawLin30(): # Рисует линии под углом 30°
    PG.draw.line(win, Clr4, CtrWin, [X0, Y0], WidGrid) # Линия правого нижнего сектора
    PG.draw.line(win, Clr4, CtrWin, [X1, Y1], WidGrid) # Линия правого верхнего сектора
    PG.draw.line(win, Clr4, CtrWin, [X2, Y2], WidGrid) # Линия левого нижнего сектора
    PG.draw.line(win, Clr4, CtrWin, [X3, Y3], WidGrid) # Линия левого верхнего сектора

def DrawLin60(): # Рисует линии под углом 60°
    PG.draw.line(win, Clr4, CtrWin, [X4, Y4], WidGrid) # Линия правого нижнего сектора
    PG.draw.line(win, Clr4, CtrWin, [X5, Y5], WidGrid) # Линия правого верхнего сектора
    PG.draw.line(win, Clr4, CtrWin, [X6, Y6], WidGrid) # Линия левого нижнего сектора
    PG.draw.line(win, Clr4, CtrWin, [X7, Y7], WidGrid) # Линия левого верхнего сектора

def DrawLin90(): # Рисует линии под углом 90°
    PG.draw.line(win, Clr4, [CtrWin[0], 0], [CtrWin[0], SizeWin[0]], WidGrid) # Вертикальная линия
    PG.draw.line(win, Clr4, [0, CtrWin[0]], [SizeWin[0], CtrWin[0]], WidGrid) # Горизонтальная линия

def DrawSpinTri(): # Рисует вращающиеся треугольники с шагом 2°
    PG.draw.polygon(win, (0, 255, 0), [CtrWin, [Xa, Ya], [Xb, Yb]]) # Вращающийся треугольник 2°
    PG.draw.polygon(win, (0, 238, 0), [CtrWin, [Xb, Yb], [Xc, Yc]]) # Вращающийся треугольник 4°
    PG.draw.polygon(win, (0, 221, 0), [CtrWin, [Xc, Yc], [Xd, Yd]]) # Вращающийся треугольник 6°
    PG.draw.polygon(win, (0, 204, 0), [CtrWin, [Xd, Yd], [Xe, Ye]]) # Вращающийся треугольник 8°
    PG.draw.polygon(win, (0, 187, 0), [CtrWin, [Xe, Ye], [Xf, Yf]]) # Вращающийся треугольник 10°
    PG.draw.polygon(win, (0, 170, 0), [CtrWin, [Xf, Yf], [Xg, Yg]]) # Вращающийся треугольник 12°
    PG.draw.polygon(win, (0, 153, 0), [CtrWin, [Xg, Yg], [Xh, Yh]]) # Вращающийся треугольник 14°
    PG.draw.polygon(win, (0, 136, 0), [CtrWin, [Xh, Yh], [Xi, Yi]]) # Вращающийся треугольник 16°
    PG.draw.polygon(win, (0, 119, 0), [CtrWin, [Xi, Yi], [Xj, Yj]]) # Вращающийся треугольник 18°
    PG.draw.polygon(win, (0, 102, 0), [CtrWin, [Xj, Yj], [Xk, Yk]]) # Вращающийся треугольник 20°
    PG.draw.polygon(win, (0, 85, 0), [CtrWin, [Xk, Yk], [Xl, Yl]]) # Вращающийся треугольник 22°
    PG.draw.polygon(win, (0, 68, 0), [CtrWin, [Xl, Yl], [Xm, Ym]]) # Вращающийся треугольник 24°
    PG.draw.polygon(win, (0, 51, 0), [CtrWin, [Xm, Ym], [Xn, Yn]]) # Вращающийся треугольник 26°
    PG.draw.polygon(win, (0, 34, 0), [CtrWin, [Xn, Yn], [Xo, Yo]]) # Вращающийся треугольник 28°
    PG.draw.polygon(win, (0, 17, 0), [CtrWin, [Xo, Yo], [Xp, Yp]]) # Вращающийся треугольник 30°

def DrawClsCir(): # Рисует закрывающие круги
    PG.draw.circle(win, Clr2, CtrWin, 320, 81) # Круг закрывающий торчащие углы
    PG.draw.circle(win, MainClr, CtrWin, rad, 4) # Граница

def DrawPol(): # Рисует рамки для надписей
    PG.draw.polygon(win, Clr4, [[0, SizeWin[1] - 36], [75, SizeWin[1] - 36], [110, SizeWin[1]], [0, SizeWin[1]]]) # Рамка для degrees
    PG.draw.polygon(win, Clr4, [[SizeWin[0], SizeWin[1] - 36], [SizeWin[0] - 118, SizeWin[1] - 36], [SizeWin[0] - 153, SizeWin[1]], [SizeWin[0], SizeWin[1]]]) # Рамка для Mainlabel
    PG.draw.polygon(win, Clr4, [[CtrWin[0] + 155, 0], [CtrWin[0] - 155, 0], [CtrWin[0] - 120, 36], [CtrWin[0] + 120, 36]]) # Рамка для fov

def DrawTit(): # Рисует надписи
    win.blit(MainLbl, (183, 8)) # Вывод на окно названия программы
    win.blit(deg, (10, SizeWin[1] - 30)) # Вывод на окно области обнаружения
    win.blit(fov, (SizeWin[0] - 115, SizeWin[1] - 30)) # Вывод на окно активного угла обзора
    win.blit(deg0, (CtrWin[0] - 4, 40)) # Вывод угла 0°
    win.blit(deg30, (X5 + 12, Y5 - 17)) # Вывод угла 30°
    win.blit(deg60, (X1 + 12, Y1 - 17)) # Вывод угла 60°
    win.blit(deg90, (546, CtrWin[1] - 6)) # Вывод угла 90°
    win.blit(deg120, (X0 + 4, Y0 + 4)) # Вывод угла 120°
    win.blit(deg150, (X4 + 4, Y4 + 4)) # Вывод угла 150°
    win.blit(deg180, (CtrWin[0] - 15, 546)) # Вывод угла 180°
    win.blit(deg210, (X6 - 38, Y6 + 4)) # Вывод угла 210°
    win.blit(deg240, (X2 - 38, Y2 + 4)) # Вывод угла 240°
    win.blit(deg270, (20, CtrWin[1] - 6)) # Вывод угла 270°
    win.blit(deg300, (X3 - 38, Y3 - 17)) # Вывод угла 300°
    win.blit(deg330, (X7 - 38, Y7 - 17)) # Вывод угла 330°

def DrawExtLin(): # Рисует внешние линии для углов
    PG.draw.line(win, MainClr, [X5, Y5], [X5 + 40, Y5], WidGrid) # Внешняя линия для угла 30°
    PG.draw.line(win, MainClr, [X1, Y1], [X1 + 40, Y1], WidGrid) # Внешняя линия для угла 60°
    PG.draw.line(win, MainClr, [X0, Y0], [X0 + 40, Y0], WidGrid) # Внешняя линия для угла 120°
    PG.draw.line(win, MainClr, [X4, Y4], [X4 + 40, Y4], WidGrid) # Внешняя линия для угла 150°
    PG.draw.line(win, MainClr, [X6, Y6], [X6 - 40, Y6], WidGrid) # Внешняя линия для угла 210°
    PG.draw.line(win, MainClr, [X2, Y2], [X2 - 40, Y2], WidGrid) # Внешняя линия для угла 240°
    PG.draw.line(win, MainClr, [X3, Y3], [X3 - 40, Y3], WidGrid) # Внешняя линия для угла 300°
    PG.draw.line(win, MainClr, [X7, Y7], [X7 - 40, Y7], WidGrid) # Внешняя линия для угла 330°

# Функция закрытия окна
def ClsRdr():
    PG.quit() # Выход
    exit()

# Функция поиска цели
def GoalSrch():
    global TgtDet # Глобальная переменная

    if alpha in range(0, 1): # Если
        TgtDet = True # Цель найдена

    if TgtDet: # Если
        PG.draw.circle(win, (255, 255, 255), (XCir, YCir), 2, 2) # Цель на радаре

    if alpha in range(90, 180): # Если
        TgtDet = False # Цель не найдена

def Btn():
    PG.draw.rect(win, MainClr, [0, 0, 30, 30], WidGrid, 5)
    PG.draw.line(win, MainClr, [5, 5], [23, 23], WidGrid)
    PG.draw.line(win, MainClr, [23, 5], [5, 23], WidGrid)

# Главная функция
def Main():
    DrawCir()
    DrawLin30()
    DrawLin60()
    DrawLin90()
    DrawSpinTri()
    DrawClsCir()
    DrawPol()
    DrawTit()
    DrawExtLin()
    GoalSrch()
    Btn()

    PG.display.flip() # Обновление окна



# Инициация всех модулей библиотеки pygame
PG.init()

# Основные переменные
SizeWin: list[int] = [600, 600] # Размеры окна [Ширина, Высота]
CtrWin: tuple = (SizeWin[0] / 2, SizeWin[1] / 2) # Центр окна (Ширина, Высота)

HD: list[int] = [1280, 720] # Разрешение HD [Ширина, Высота]
FullHD: list[int] = [1920, 1080] # Разрешение FullHD [Ширина, Высота]
QuadHD: list[int] = [2560, 1440] # Разрешение QuadHD 2K [Ширина, Высота]
UltraHD: list[int] = [3840, 2160] # Разрешение UltraHD 4K [Ширина, Высота]

MainClr: tuple = (0, 255, 0) # Главный цвет (Красный, Зелёный, Синий)
Clr2: tuple = (0, 0, 0) # Второй цвет (Красный, Зелёный, Синий)
Clr3: tuple = (0, 125, 0) # Третий цвет (Красный, Зелёный, Синий)
Clr4: tuple = (0, 30, 0) # Четвёртый цвет (Красный, Зелёный, Синий)

rad: int = 240 # Радиус
sml: int = 180 # Большой радиус
med: int = 120 # Средний радиус
lrg: int = 60 # Малый радиус
DynRad: int = 300 # Динамический радиус
dmtr: int = rad * 2 # Диаметр

WidGrid: int = 2 # Толщина сетки

ang: float = 0 # Активный угол обзора
spd: float = 0.025 # Скорость активных треугольников
ratio: float = 1 # Соотношение сторон
TgtDet: bool = False # Обнаружение цели

# Координаты углов при угле 30°
X0: int = CtrWin[0] + rad * cos(rads(30)) # X0
Y0: int = CtrWin[1] + rad * sin(rads(30)) # Y0

X1: int = CtrWin[0] + rad * cos(rads(30)) # X1
Y1: int = CtrWin[1] + rad * sin(-rads(30)) # Y1

X2: int = CtrWin[0] - rad * cos(rads(30)) # X2
Y2: int = CtrWin[1] - rad * sin(-rads(30)) # Y2

X3: int = CtrWin[0] - rad * cos(rads(30)) # X3
Y3: int = CtrWin[1] - rad * sin(rads(30)) # Y3

# Координаты углов при угле 60°
X4: int = CtrWin[0] + rad * cos(rads(60)) # X4
Y4: int = CtrWin[1] + rad * sin(rads(60)) # Y4

X5: int = CtrWin[0] + rad * cos(rads(60)) # X5
Y5: int = CtrWin[1] + rad * sin(-rads(60)) # Y5

X6: int = CtrWin[0] - rad * cos(rads(60)) # X6
Y6: int = CtrWin[1] - rad * sin(-rads(60)) # Y6

X7: int = CtrWin[0] - rad * cos(rads(60)) # X7
Y7: int = CtrWin[1] - rad * sin(rads(60)) # Y7

# Шрифты
font40 = PG.font.Font(None, 40) # Шрифт основной
font25 = PG.font.Font(None, 25) # Шрифт для углов

# Основные надписи
MainLbl = font40.render("Radar simulation", True, MainClr) # Название программы
deg = font40.render("360°", True, MainClr) # Область обнаружения
fov = font40.render("FOV 30°", True, MainClr) # Активный угл обзора

# Надписи углов
deg0 = font25.render("0°", True, MainClr) # Угол 0°
deg30 = font25.render("30°", True, MainClr) # Угол 30°
deg60 = font25.render("60°", True, MainClr) # Угол 60°
deg90 = font25.render("90°", True, MainClr) # Угол 90°
deg120 = font25.render("120°", True, MainClr) # Угол 120°
deg150 = font25.render("150°", True, MainClr) # Угол 150°
deg180 = font25.render("180°", True, MainClr) # Угол 180°
deg210 = font25.render("210°", True, MainClr) # Угол 210°
deg240 = font25.render("240°", True, MainClr) # Угол 240°
deg270 = font25.render("270°", True, MainClr) # Угол 270°
deg300 = font25.render("300°", True, MainClr) # Угол 300°
deg330 = font25.render("330°", True, MainClr) # Угол 330°

# Структура окна
win = PG.display.set_mode(SizeWin, PG.NOFRAME, 32) # Окно
TickRate = PG.time.Clock() # Симуляция времени
field = PG.surface.Surface(SizeWin, PG.SRCALPHA) # Область экрана

UserRes = PG.display.get_desktop_sizes() # Размеры пользовательского экрана
WindWidComp: list[int] = [] # Ширины экрана
WinHgtComp: list[int] = [] # Высоты экрана
for size in UserRes: # Для size в UserResolution
    WindWidComp.append(size[0]) # Добавляется ширина экрана
for size in UserRes: # Для size в UserResolution
    WinHgtComp.append(size[1]) # Добавляется высота экрана
res: list[int] = [WindWidComp[0], WinHgtComp[0]] # Готовые размеры пользовательского экрана
FmtMon = res[0] / res[1] # Формат пользовательского экрана



# Главный цикл
while True: # Пока всегда
    TickRate.tick(60) # Скорость симуляции времени
    win.fill(Clr2) # Заполнение цветом
    win.blit(field, (0, 0))

    for close in PG.event.get(): # Для close в PG.event.get()
        if close.type == PG.QUIT: # Если close.type = PG.QUIT
            ClsRdr()

    # Движение угла
    ang = ang + spd # Движение активного угла обзора
    if ang > rads(360): # Если angle > 360°, то
        ang = 0 # Активный угол обзора сбрасывается

    # Активные координаты углов с шагом 2°
    Xa: int = CtrWin[0] + DynRad * cos(ang) # X 0°
    Ya: int = CtrWin[1] + DynRad * sin(ang) # Y 0°

    Xb: int = ActAng(0, 2) # X 2°
    Yb: int = ActAng(1, 2) # Y 2°

    Xc: int = ActAng(0, 4) # X 4°
    Yc: int = ActAng(1, 4) # Y 4°

    Xd: int = ActAng(0, 6) # X 6°
    Yd: int = ActAng(1, 6) # Y 6°

    Xe: int = ActAng(0, 8) # X 8°
    Ye: int = ActAng(1, 8) # Y 8°

    Xf: int = ActAng(0, 10) # X 10°
    Yf: int = ActAng(1, 10) # Y 10°

    Xg: int = ActAng(0, 12) # X 12°
    Yg: int = ActAng(1, 12) # Y 12°

    Xh: int = ActAng(0, 14) # X 14°
    Yh: int = ActAng(1, 14) # Y 14°

    Xi: int = ActAng(0, 16) # X 16°
    Yi: int = ActAng(1, 16) # Y 16°

    Xj: int = ActAng(0, 18) # X 18°
    Yj: int = ActAng(1, 18) # Y 18°

    Xk: int = ActAng(0, 20) # X 20°
    Yk: int = ActAng(1, 20) # Y 20°

    Xl: int = ActAng(0, 22) # X 22°
    Yl: int = ActAng(1, 22) # Y 22°

    Xm: int = ActAng(0, 24) # X 24°
    Ym: int = ActAng(1, 24) # Y 24°

    Xn: int = ActAng(0, 26) # X 26°
    Yn: int = ActAng(1, 26) # Y 26°

    Xo: int = ActAng(0, 28) # X 28°
    Yo: int = ActAng(1, 28) # Y 28°

    Xp: int = ActAng(0, 30) # X 30°
    Yp: int = ActAng(1, 30) # Y 30°

    # Вычисление координат цели
    Width, Height = PAG.position() # Координаты курсора

    # Определение формата пользовательского экрана
    if round(FmtMon, 3) == 1.778: # Если FormatMonitor = 1.778, то
        # Определение разрешение пользовательского экрана
        if res == UltraHD: # Если Resolution = UltraHD, то
            ratio = 9.378

        elif res == QuadHD: # Иначе если Resolution = QuadHD, то
            ratio = 6.231

        elif res == FullHD: # Иначе если Resolution = FullHD, то
            ratio = 4.682

        elif res == HD: # Иначе если Resolution = HD, то
            ratio = 3.122

        else: # Иначе Resolution не соответствует предложенным
            print("Ошибка отображения"
                "\nУ вас не соответствует дисплей нужному формату. Программа работает только с форматами:"
                  "\nHD - 1280 x 720"
                  "\nFullHD - 1920 x 1080"
                  "\nQuadHD - 2560 x 1440"
                  "\nUltraHD - 3840 x 2160"
            ) # Вывод ошибки
            ClsRdr()

    else: # Иначе FormatMonitor не соответствует формату 16:9
        print("Ошибка отображения."
            "\nУ вас не соответствует дисплей формату 16:9.") # Вывод ошибки
        ClsRdr()

    # Координаты точек области размеров экрана
    XXa: int = (0 * (res[0] / ratio)) / res[0] + 95 # X верхней левой точки
    YYa: int = (0 * (res[1] / ratio)) / res[1] + 185 # Y верхней левой точки
    XXb: int = (res[0] * (res[0] / ratio)) / res[0] # X нижней право точки
    YYb: int = (res[1] * (res[1] / ratio)) / res[1] # Y нижней право точки
    PG.draw.rect(field, (0, 255, 0, 15), [XXa, YYa, XXb, YYb]) # Область видимости экрана

    # Координаты цели
    XCir: int = (Width * (res[0] / ratio)) / res[0] + 95 # X цели
    YCir: int = (Height * (res[1] / ratio)) / res[1] + 185 # Y цели

    # Вычисление векторов их углов и градусов
    PosVctrFOV: list[int] = [Xa - CtrWin[0], Ya - CtrWin[1]] # Координаты вектора активного угла обзора
    PosVctrTgt: list[int] = [XCir - CtrWin[0], YCir - CtrWin[1]] # Координаты вектора цели
    VctrFOV = PG.Vector2(PosVctrFOV) # Вектор активного угла обзора
    VctrTgt = PG.Vector2(PosVctrTgt) # Вектор цели
    LenVctrFOV: float = LenVctr(VctrFOV[0], VctrFOV[1]) # Длина вектора активного угла обзора
    LenVctrTgt: float = LenVctr(VctrTgt[0], VctrTgt[1]) # Длина вектора цели

    alpha: int = flr(M.degrees(M.acos((VctrFOV[0] * VctrTgt[0] + VctrFOV[1] * VctrTgt[1]) / (LenVctrFOV * LenVctrTgt)))) # Угол α

    Main() # Вызов главной функции