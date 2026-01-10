# 6AU1(Index:Game in Galgame)
# By CelestialAspirePeak(Tian Mufei/Xing Wangshan)
# https://github.com/CelestialAsPeak/6AU1
# Released under a "SD 2-Clause" license
#
# SD 2-Clause License
#
# Copyright (c) 2026, CelestialAsPeak
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import pygame,sys,time
from pygame.locals import *

# //////////////////////////////////////////////变量区//////////////////////////////////////

# 速度类型变量
GameSystemTitleFadeSpeed = 0.5  # 开屏动画淡入淡出速度（秒）->0.5
GameSystemMenuFadeSpeed = 1.0   # 主菜单淡入速度（秒）     ->1.0
GameSystemTitleStayTime = 2.0   # 开屏动画停留时间（秒）    ->2.0
GameSystemMenuWaitTime = 0.5    # 主菜单等待时间（秒）     ->0.5

# 整数类型变量
GameSystemSettingVariable_fps = FPS = 60
GameSystemSettingVariable_WindowWidth = WindowWidth = 1400
GameSystemSettingVariable_WindowHeight = WindowHeight = 800
## 开屏动画变量
GameSystemTitleStartTime = 0
GameSystemTitleAlpha = 0
GameSystemTitleState = 0         # 0:淡入 1:停留 2:淡出 3:结束
GameSystemTitleImageSpacing = 100 # 开屏的图片间距
## 主菜单相关变量
GameSystemMenuState = 0  # 0:开屏动画 1:主菜单
GameSystemMenuItems = ['开始游戏', '退出游戏']
GameSystemMenuItemSelected = 0
GameSystemMenuFont = None
GameSystemMenuStartTime = 0
GameSystemMenuAlpha = 0
GameSystemMenuButtonRects = []  # 存储按钮矩形区域
GameSystemMenuButtons = ['新的故事', '读取存档', '流程图', '鉴赏模式', '设置', '退出游戏']


# 字符串类型变量
GameSystemSettingVariable_WindowsName = GameName = '6AU1'

# 路径变量
GameSystem6AU1title1PG = "picture/6AU1titlePG.png"  #标题图片变量1
GameSystem6AU1title2PG = "picture/CASP_Newyear.jpg" #标题图片变量1
GameSystemFontPath = "ttf/msyhbd.ttc" #字体路径变量

# 颜色类型变量
#          R     G     B
WHITE = ( 255 , 255 , 255 )
BLACK = (  0  ,  0  ,  0 )
BLUE  = (  0  ,  0  , 255 )
PINK =  ( 255 , 152 , 193 )
GRAY =  ( 100 , 100 , 100 )

# //////////////////////////////////////////////简便函数区//////////////////////////////////////
def DrewRectangle(x, y, width, height, color):
    """绘制矩形函数：在游戏窗口的指定位置绘制一个填充矩形"""
    # 使用pygame的draw.rect函数直接绘制矩形到游戏窗口
    # 使用示例（不在实际代码中，仅演示用法）：
    # DrewRectangle(100, 100, 200, 50, BLUE)  # 在坐标(100,100)处绘制一个200x50像素的蓝色矩形
    pygame.draw.rect(GAMEWINDOW, color, (x, y, width, height))

def MouseGowhere(event):
    """鼠标坐标打印函数：打印鼠标点击事件的坐标位置"""
    # event.pos 是鼠标点击事件的坐标位置，格式为 (x, y)
    # 如果事件类型是鼠标按下，则打印坐标
    # 使用示例（在事件循环中调用）：
    # for event in pygame.event.get():
    #     if event.type == QUIT:
    #         pygame.quit()
    #         sys.exit()
    #     MouseGowhere(event)  # 添加这一行即可
    if event.type == MOUSEBUTTONDOWN:
        print(f"鼠标点击坐标: {event.pos}")
    # 如果事件类型不是鼠标按下，则什么也不做
# //////////////////////////////////////////////模块代码区//////////////////////////////////////

def GameSystemBodyOpen():
    """开屏动画"""
    global GameSystemSettingVariable_fps
    global GameSystemSettingVariable_WindowWidth
    global GameSystemSettingVariable_WindowHeight
    global GameSystemSettingVariable_WindowsName
    global WHITE, GRAY
    global GameSystemTitleStartTime, GameSystemTitleAlpha, GameSystemTitleState
    global GameSystemTitleImageSpacing
    global GameSystemGlobalState, GameSystemMenuStartTime
    global GameSystemTitleFadeSpeed, GameSystemTitleStayTime

    # 每次循环开始时清空窗口
    GAMEWINDOW.fill(BLACK)

    # 加载并缩放两张图片为350*350
    title_image1 = pygame.image.load(GameSystem6AU1title1PG)
    title_image1 = pygame.transform.scale(title_image1, (350, 350))

    title_image2 = pygame.image.load(GameSystem6AU1title2PG)
    title_image2 = pygame.transform.scale(title_image2, (330, 330))

    # 初始化开始时间
    if GameSystemTitleStartTime == 0:
        GameSystemTitleStartTime = time.time()

    # 计算经过的时间
    current_time = time.time()
    elapsed_time = current_time - GameSystemTitleStartTime

    # 根据状态和经过的时间更新透明度
    if GameSystemTitleState == 0:  # 淡入
        if elapsed_time < GameSystemTitleFadeSpeed:
            GameSystemTitleAlpha = int((elapsed_time / GameSystemTitleFadeSpeed) * 255)
        else:
            GameSystemTitleAlpha = 255
            GameSystemTitleStartTime = time.time()
            GameSystemTitleState = 1

    elif GameSystemTitleState == 1:  # 停留
        if elapsed_time >= GameSystemTitleStayTime:
            GameSystemTitleStartTime = time.time()
            GameSystemTitleState = 2

    elif GameSystemTitleState == 2:  # 淡出
        if elapsed_time < GameSystemTitleFadeSpeed:
            GameSystemTitleAlpha = 255 - int((elapsed_time / GameSystemTitleFadeSpeed) * 255)
        else:
            GameSystemTitleAlpha = 0
            GameSystemTitleStartTime = time.time()
            GameSystemTitleState = 3

    # 计算两张图片的位置（窗口1200*800，每张图片350*350）
    # 使用变量控制图片间距
    total_width = 350 + GameSystemTitleImageSpacing + 350  # 两张图片宽度加间距
    start_x = (WindowWidth - total_width) // 2
    y = (WindowHeight - 350) // 2  # (800-350)/2 = 225

    x1 = start_x  # 第一张图片的x坐标
    x2 = start_x + 350 + GameSystemTitleImageSpacing  # 第二张图片的x坐标

    # 根据状态绘制图片
    if GameSystemTitleState < 3:  # 状态0,1,2时绘制图片
        # 设置图片透明度并绘制
        title_image1.set_alpha(GameSystemTitleAlpha)
        title_image2.set_alpha(GameSystemTitleAlpha)
        GAMEWINDOW.blit(title_image1, (x1, y))
        GAMEWINDOW.blit(title_image2, (x2, y))

    # 如果动画结束，切换到主菜单状态
    if GameSystemTitleState == 3:
        # 设置全局状态为主菜单
        GameSystemGlobalState = 1
        # 初始化主菜单开始时间
        GameSystemMenuStartTime = time.time()

    pygame.display.update()

def GameSystemBodyMain():
    """主菜单"""
    global GameSystemMenuState, GameSystemMenuItems, GameSystemMenuItemSelected, GameSystemMenuFont
    global GameSystemMenuStartTime, GameSystemMenuAlpha, GameSystemMenuButtonRects
    global GameSystemGlobalState
    global GameSystemMenuFadeSpeed, GameSystemMenuWaitTime  # 添加速度控制变量

    # 如果全局状态不是主菜单，直接返回
    if GameSystemGlobalState != 1:
        return

    # 加载中文字体
    GameSystemMenuFont = pygame.font.Font(GameSystemFontPath, 36)

    # 清空窗口
    GAMEWINDOW.fill(BLACK)

    # 计算经过的时间
    current_time = time.time()
    elapsed_time = current_time - GameSystemMenuStartTime

    # 等待指定时间后开始淡入
    if elapsed_time > GameSystemMenuWaitTime:
        if elapsed_time < (GameSystemMenuWaitTime + GameSystemMenuFadeSpeed):
            GameSystemMenuAlpha = int(((elapsed_time - GameSystemMenuWaitTime) / GameSystemMenuFadeSpeed) * 255)
        else:
            GameSystemMenuAlpha = 255
    else:
        GameSystemMenuAlpha = 0

    # 清空按钮矩形列表
    GameSystemMenuButtonRects = []

    # 绘制左侧矩形按钮
    button_width = 250
    button_height = 60
    button_spacing = 20
    start_x = 100

    # 计算总高度和起始y坐标
    total_height = len(GameSystemMenuButtons) * button_height + (len(GameSystemMenuButtons) - 1) * button_spacing
    start_y = (WindowHeight - total_height) // 2

    # 创建菜单表面用于透明度控制
    menu_surface = pygame.Surface((WindowWidth, WindowHeight), pygame.SRCALPHA)

    for a, button_text in enumerate(GameSystemMenuButtons):
        # 计算按钮位置
        y = start_y + a * (button_height + button_spacing)
        button_rect = pygame.Rect(start_x, y, button_width, button_height)

        # 存储按钮矩形用于后续交互
        GameSystemMenuButtonRects.append(button_rect)

        # 绘制按钮矩形
        pygame.draw.rect(menu_surface, GRAY, button_rect, 2)  # 边框

        # 绘制按钮文字
        text = GameSystemMenuFont.render(button_text, True, WHITE)
        text_rect = text.get_rect(center=button_rect.center)
        menu_surface.blit(text, text_rect)

    # 设置菜单透明度
    menu_surface.set_alpha(GameSystemMenuAlpha)

    # 绘制菜单表面到主窗口
    GAMEWINDOW.blit(menu_surface, (0, 0))

    pygame.display.update()

def GameSystemNewTalk(kinds):
    """对话框
    kinds -> 类型
    左上角：60,472
    左下角：60,746
    右上角：1333，472
    右下角：1333，746
    """
    DrewRectangle(60,472,1273,300,BLUE)
    pygame.display.update()

pygame.init()
pygame.font.init()
pygame.display.set_caption(GameSystemSettingVariable_WindowsName)
GAMEWINDOW = pygame.display.set_mode((GameSystemSettingVariable_WindowWidth, GameSystemSettingVariable_WindowHeight))
GAMEWINDOW.fill(BLACK)

#以下为调试模式：获取鼠标位置
#while True:
#    for event in pygame.event.get():
#        if event.type == QUIT:  # 关闭窗口
#            pygame.quit()
#            sys.exit()
#        MouseGowhere(event)

while True:
    # 检查状态并执行相应功能
    if GameSystemTitleState < 3:
        GameSystemBodyOpen()
    else:
        # 切换到主菜单状态
        GameSystemMenuState = 1
        GameSystemBodyMain()

    for event in pygame.event.get():
        if event.type == QUIT:  # 关闭窗口
            pygame.quit()
            sys.exit()

        if GameSystemMenuState == 1 and GameSystemMenuAlpha == 255:  # 主菜单完全显示后
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # 检查鼠标点击是否在按钮区域内
                for i, rect in enumerate(GameSystemMenuButtonRects):
                    if rect.collidepoint(mouse_pos):
                        # 按钮点击处理
                        if i == 0:  # 新的故事
                            print("点击了按钮: 新的故事")
                            # 这里可以添加开始新游戏的逻辑
                            GameSystemNewTalk(1)
                        elif i == 1:  # 读取存档
                            print("点击了按钮: 读取存档")
                            # 这里可以添加读取存档的逻辑
                        elif i == 2:  # 流程图
                            print("点击了按钮: 流程图")
                            # 这里可以添加查看流程图的逻辑
                        elif i == 3:  # 鉴赏模式
                            print("点击了按钮: 鉴赏模式")
                            # 这里可以添加鉴赏模式的逻辑
                        elif i == 4:  # 设置
                            print("点击了按钮: 设置")
                            # 这里可以添加设置菜单的逻辑
                        elif i == 5:  # 退出游戏
                            print("点击了按钮: 退出游戏")
                            pygame.quit()
                            sys.exit()
                        break