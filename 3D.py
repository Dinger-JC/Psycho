# Программа представляет из себя проекцию куба, созданную с помощью матрицы

import pygame as PG
import math as M
import numpy as NP



## Основное
def Main():
    tick_rate.tick(fps) # Заданная скорость симуляции
    PG.draw.rect(window, colors[16], [0, 0, size_window[0], size_window[1]]) # Задний фон

    for close in PG.event.get(): # Закрытие на клавишу 'Esc'
        if close.type == PG.QUIT:
            PG.quit()
            exit()
        if close.type == PG.KEYDOWN:
            if close.key == PG.K_ESCAPE:
                PG.quit()
                exit()



## Вращение вокруг осей в матрице
def RotationMatrix(angle_x, angle_y, angle_z) -> int | float:
    # Матрица вращения вокруг оси абсциссы X
    rotation_x = NP.matrix([
            [1, 0, 0],
            [0, M.cos(angle_x), -M.sin(angle_x)],
            [0, M.sin(angle_x), M.cos(angle_x)]
    ])

    # Матрица вращения вокруг оси ординаты Y
    rotation_y = NP.matrix([
            [M.cos(angle_y), 0, M.sin(angle_y)],
            [0, 1, 0],
            [-M.sin(angle_y), 0, M.cos(angle_y)]
    ])

    # Матрица вращения вокруг оси аппликаты Z
    rotation_z = NP.matrix([
            [M.cos(angle_z), -M.sin(angle_z), 0],
            [M.sin(angle_z), M.cos(angle_z), 0],
            [0, 0, 1]
    ])

    return rotation_x, rotation_y, rotation_z



## Вращение по осям по клавишам
def RotationControl(speed_rotation: float, key):
    rotations: dict[str, tuple[int, ...]] = {
            'x': (PG.K_w, PG.K_s, 'angle_rotation_x'),
            'y': (PG.K_a, PG.K_d, 'angle_rotation_y'),
            'z': (PG.K_e, PG.K_q, 'angle_rotation_z')
    }

    for axis, (key_minus, key_plus, angle_rotation) in rotations.items():
        if key[key_plus]: # Поворот против часовой стрелки
            globals()[angle_rotation] += speed_rotation
            if axis == 'x':
                Titles().Title("'S'", colors[2], size_window[0] - 187, 5)
            elif axis == 'y':
                Titles().Title("'D'", colors[2], size_window[0] - 184, 25)
            elif axis == 'z':
                Titles().Title("'Q'", colors[2], size_window[0] - 184, 45)

        elif key[key_minus]: # Поворот по часовой стрелки
            globals()[angle_rotation] -= speed_rotation
            if axis == 'x':
                Titles().Title("'W'", colors[2], size_window[0] - 153, 5)
            elif axis == 'y':
                Titles().Title("'A'", colors[2], size_window[0] - 149, 25)
            elif axis == 'z':
                Titles().Title("'E'", colors[2], size_window[0] - 148, 45)



## Надписи
class Titles:
    @staticmethod
    def Title(text: str, color: tuple[int, ...], place_x: int, place_y: int): # Отображение и расположение надписи
        area = font.render(text, True, color)
        window.blit(area, [place_x, place_y])

    def DrawTitles(self, color: tuple[int, ...]): # Надписи
        # Общая информация
        self.Title(f"Длина ребра куба: {scale_matrix} пикселей (2)", color, 5, 5)
        self.Title(f"Скорость симуляции: {fps} FPS", color, 5, 25)

        # Управление
        self.Title("'Esc' чтобы закрыть", color, size_window[0] - 173, 65)
        self.Title("'S' / 'W' - поворот по X", color, size_window[0] - 187, 5)
        self.Title("'D' / 'A' - поворот по Y", color, size_window[0] - 184, 25)
        self.Title("'Q' / 'E' - поворот по Z", color, size_window[0] - 184, 45)


## Кнопки
class Buttons:
    def __init__(self): # Параметры мыши и курсора
        self.x_cursor, self.y_cursor = PG.mouse.get_pos()
        self.Prsd = PG.mouse.get_pressed()
        self.PrsdLBM: bool = self.Prsd[0]

    def ButtonLogs(self): # Кнопка переключения логов
        PG.draw.rect(window, colors[2], [1233, 85, 21, 20]) # Зелёная часть
        PG.draw.rect(window, colors[0], [1254, 85, 21, 20]) # Красная часть
        Titles().Title("Logs", colors[16], size_window[0] - 46, 86)
        global logs

        # Смена режима логов
        if self.y_cursor in range(85, 105) and self.PrsdLBM:
            if self.x_cursor in range(1233, 1254):
                logs = True
            elif self.x_cursor in range(1254, 1275):
                logs = False

    def ButtonImitationShadow(self): # Кнопка переключения имитации теней
        PG.draw.rect(window, colors[2], [1131, 110, 72, 20]) # Зелёная часть
        PG.draw.rect(window, colors[0], [1203, 110, 72, 20]) # Красная часть
        Titles().Title("Imitation shadow", colors[16], size_window[0] - 148, 112)
        global switch

        if self.y_cursor in range(110, 130) and self.PrsdLBM:
            if self.x_cursor in range(1131, 1203):
                switch = True
            if self.x_cursor in range(1203, 1275):
                switch = False



## Грани
class Faces:
    def __init__(self): # Грани
        projection_indices = [
                [1, 5, 6, 2], # Грань B-F-G-C, центр X
                [4, 5, 1, 0], # Грань E-F-B-A, центр Y
                [0, 1, 2, 3], # Грань A-B-C-D, центр Z
                [4, 0, 3, 7], # Грань E-A-D-H, центр X1
                [3, 2, 6, 7], # Грань D-C-G-H, центр Y1
                [4, 5, 6, 7] # Грань E-F-G-H, центр Z1
        ]

        self.faces = [(coordinate_matrix[i], colors[i], *(projection_points[j] for j in indices))
            for i, indices in zip(range(8, 14), projection_indices)]

    def Face(self, center: float, color: tuple[int, ...], *points: list[int]): # Отрисовка грани
        if center[2] > 0:
            PG.draw.polygon(window, color, points)

    def ImitationRTX(self, center: float, color: tuple[int, ...], *points: list[int]): # Имитация RTX
        light: int = M.floor(center[2] * 150) + 100
        color: tuple[int, ...] = (light, light, light)
        self.Face(center, color, *points)

    def Mode(self): # Режим отображения граней
        if switch == False:
            for face in self.faces:
                self.Face(*face)

        elif switch == True:
            for face in self.faces:
                self.ImitationRTX(*face)



class Points:
    def __init__(self): # Названия
        self.vertexes: list[str] = ["A", "B", "C", "D", "E", "F", "G", "H"] # Вершины
        self.help_points: list[str] = ["X", "Y", "Z", "X1", "Y1", "Z1"] # Вспомогательные точки

    def Point(self, number: list[int], color: tuple[int, ...], name: str, indent: int): # Отрисовка точки
        PG.draw.circle(window, color, number, 7)
        Titles().Title(name, color, number[0] + indent, number[1] + indent)

    def InformationPoint(self, name: str, number_point: list[float], color: str, place_x: int, place_y: int): # Информация о точке
        Titles().Title(f"Point: {name}", color, place_x, place_y)
        for number, axis in enumerate(['X', 'Y', 'Z']):
            Titles().Title(
                    f"{axis}: {float(number_point[number]):.3f}"
                    .replace('[', '')
                    .replace(']', ''),
                    color, place_x, place_y + 20 * (number + 1)
            )

    def DrawPoints(self): # Отрисовка точек
        for number, point in enumerate(self.vertexes): # Вершины куба
            self.Point(projection_points[number], colors[number], point, 5)
        for number, point in enumerate(self.help_points): # Вспомогательные точки
            self.Point(projection_points[8 + number], colors[14], point, 5)

    def DrawInformationPoints(self): # Отрисовка информации точек
        for number, point in enumerate(self.vertexes): # Информация о вершинах
            self.InformationPoint(point, coordinate_matrix[0 + number], colors[number], 5, 45 + 80 * number)
        for number, point in enumerate(self.help_points): # Информация о вспомогательных точках
            self.InformationPoint(point, coordinate_matrix[8 + number], colors[14], 90, 45 + 80 * number)



class Edges:
    def Edge(self, first_point: list[int], second_point: list[int]): # Ребро
        PG.draw.line(window, colors[14], first_point, second_point, 3)

    def DrawEdges(self): # Отрисовка рёбер
        for number in range(4): # Последовательное соединение точек A-B-C-D
            self.Edge(projection_points[number], projection_points[(number + 1) % 4])
        for number in range(4): # Последовательное соединение точек A-E, B-F, C-G, D-H
            self.Edge(projection_points[number], projection_points[number + 4])
        for number in range(4, 8): # Последовательное соединение точек E-F-G-H
            self.Edge(projection_points[number], projection_points[(number + 1) % 4 + 4])



## Структура окна
PG.init() # Инициация всех модулей библиотеки pygame
size_window: list[int] = [1280, 720] # Размеры окна
window = PG.display.set_mode(size_window) # Окно
PG.display.set_caption("3D in python by Dinger") # Название окна
tick_rate = PG.time.Clock() # Симуляция времени
fps: int = 360 # Скорость симуляции

## Основные переменные
scale_matrix: int = 150 # Размер матрицы
center_window: list[int] = [size_window[0] / 2, size_window[1] / 2] # Центр вращения куба
font = PG.font.Font(None, 25) # Шрифт
logs: bool = False # Дополнительная информация
switch: bool = False # Переключение режимов отрисовки
angle_rotation_x, angle_rotation_y, angle_rotation_z = 0.0, 0.0, 0.0 # Углы поворота по осям

## Цвета
colors: list[tuple[int, ...]] = [
        # Цвета вершин
        (255, 0, 0), # Красный цвет; 1
        (255, 255, 0), # Жёлтый цвет; 2
        (0, 255, 0), # Зелёный цвет; 3
        (0, 0, 255), # Синий цвет; 4
        (155, 0, 0), # Тёмно-красный цвет; 5
        (155, 155, 0), # Тёмно-жёлтый цвет; 6
        (0, 155, 0), # Тёмно-зелёный цвет; 7
        (0, 0, 155), # Тёмно-синий цвет; 8
        # Цвета сторон
        (255, 0, 155), # Малиновый цвет; 9
        (155, 255, 0), # Лаймовый цвет; 10
        (0, 255, 255), # Бирюзовый цвет; 11
        (155, 0, 100), # Тёмно-малиновый цвет; 12
        (100, 155, 0), # Тёмно-лаймовый цвет; 13
        (0, 155, 155), # Тёмно-бирюзовый цвет; 14
        # Другие цвета
        (100, 100, 100), # Серый цвет; 15
        (50, 50, 50), # Тёмно-серый цвет; 16
        (0, 0, 0) # Чёрный цвет; 17
]

# Точки в матрице
points: list[list[int]] = [
        # Вершины куба
        [-1, 1, 1], # Вершина A
        [1, 1, 1], # Вершина B
        [1, -1, 1], # Вершина C
        [-1, -1, 1], # Вершина D
        [-1, 1, -1], # Вершина E
        [1, 1, -1], # Вершина F
        [1, -1, -1], # Вершина G
        [-1, -1, -1], # Вершина H
        # Вспомогательные точки
        [1, 0, 0], # Точка X
        [0, 1, 0], # Точка Y
        [0, 0, 1], # Точка Z
        [-1, 0, 0], # Точка X1
        [0, -1, 0], # Точка Y1
        [0, 0, -1] # Точка Z1
]
points_matrix = NP.matrix(points) # Точки
projection_points: list[int] = [0 for b in range(len(points_matrix))] # Проекция точек
coordinate_matrix = [0 for b in range(len(points_matrix))] # Координаты точек в матрице

## Шаблон матрицы
matrix: list[list[int]] = [
        [1, 0, 0],
        [0, -1, 0],
        [0, 0, 0]
]
projection_matrix = NP.matrix(matrix) # Матрица



while True:
    Main()
    Titles().DrawTitles(colors[14])

    rotation_x, rotation_y, rotation_z = RotationMatrix(angle_rotation_x, angle_rotation_y, angle_rotation_z)
    RotationControl(0.005, PG.key.get_pressed())

    number: int = 0
    for point in points_matrix:
        rotate = NP.dot(rotation_z, NP.dot(rotation_y, NP.dot(rotation_x, point.reshape((3, 1)))))
        projection_2d = NP.dot(projection_matrix, rotate) # Проекция матрицы на экран
        coordinate_matrix[number] = rotate
        projection_points[number] = [
                int(projection_2d[0][0] * scale_matrix) + center_window[0], # X точки
                int(projection_2d[1][0] * scale_matrix) + center_window[1] # Y точки
        ]
        number += 1

    Faces().Mode()
    Buttons().ButtonLogs()
    Buttons().ButtonImitationShadow()

    if logs == True:
        Edges().DrawEdges()
        Points().DrawPoints()
        Points().DrawInformationPoints()

    PG.display.flip() # Обновление окна
