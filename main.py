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


import pygame
import sys
import time
from pygame.locals import *

# 整数类型变量
GameSystemSettingVariable_fps = FPS = 60                       #刷新率
GameSystemSettingVariable_WindowWidth = WindowWidth = 1200
GameSystemSettingVariable_WindowHeight = WindowHeight = 800
## 开屏动画变量
GameSystemTitleStartTime = 0
GameSystemTitleAlpha = 0
GameSystemTitleState = 0  # 0:淡入 1:停留 2:淡出 3:结束
## 主菜单相关变量
GameSystemMenuState = 0  # 0:开屏动画 1:主菜单
GameSystemMenuItems = ['开始游戏', '退出游戏']
GameSystemMenuItemSelected = 0
GameSystemMenuFont = None

# 字符串类型变量
GameSystemSettingVariable_WindowsName = GameName = '6AU1'

# 路径变量
GameSystem6AU1titlePG = "picture/6AU1titlePG.png" #标题图片变量

# 颜色类型变量
#          R     G     B
WHITE = ( 255 , 255 , 255 )
BLACK = (  0  ,  0  ,  0 )
BLUE  = (  0  ,  0  , 255 )
PINK =  ( 255 , 152 , 193 )
GRAY =  ( 100 , 100 , 100 )

# Function Setting
def GameSystemBodyOpen():
    """开屏动画"""
    global GameSystemSettingVariable_fps
    global GameSystemSettingVariable_WindowWidth
    global GameSystemSettingVariable_WindowHeight
    global GameSystemSettingVariable_WindowsName
    global WHITE, GRAY
    global GameSystemTitleStartTime, GameSystemTitleAlpha, GameSystemTitleState

    # 每次循环开始时清空窗口
    GAMEWINDOW.fill(BLACK)

    # 加载并缩放标题图片为450*450
    title_image = pygame.image.load(GameSystem6AU1titlePG)
    title_image = pygame.transform.scale(title_image, (450, 450))

    # 初始化开始时间
    if GameSystemTitleStartTime == 0:
        GameSystemTitleStartTime = time.time()

    # 计算经过的时间
    current_time = time.time()
    elapsed_time = current_time - GameSystemTitleStartTime

    # 根据状态和经过的时间更新透明度
    if GameSystemTitleState == 0:  # 淡入
        if elapsed_time < 1.0:
            GameSystemTitleAlpha = int((elapsed_time / 1.0) * 255)
        else:
            GameSystemTitleAlpha = 255
            GameSystemTitleStartTime = time.time()
            GameSystemTitleState = 1

    elif GameSystemTitleState == 1:  # 停留
        if elapsed_time >= 1.0:
            GameSystemTitleStartTime = time.time()
            GameSystemTitleState = 2

    elif GameSystemTitleState == 2:  # 淡出
        if elapsed_time < 1.0:
            GameSystemTitleAlpha = 255 - int((elapsed_time / 1.0) * 255)
        else:
            GameSystemTitleAlpha = 0
            GameSystemTitleStartTime = time.time()
            GameSystemTitleState = 3

    # 计算居中位置（窗口1200*800，图片450*450）
    x = (WindowWidth - 450) // 2  # (1200-450)/2 = 375
    y = (WindowHeight - 450) // 2  # (800-450)/2 = 175

    # 根据状态绘制图片
    if GameSystemTitleState < 3:  # 状态0,1,2时绘制图片
        # 设置图片透明度并绘制
        title_image.set_alpha(GameSystemTitleAlpha)
        GAMEWINDOW.blit(title_image, (x, y))

    # 如果动画结束，重置状态以便重新开始（如果需要）
    if GameSystemTitleState == 3:
        # 这里可以添加后续逻辑，或者保持黑屏
        # 如果需要循环播放，可以重置状态：
        # GameSystemTitleStartTime = 0
        # GameSystemTitleAlpha = 0
        # GameSystemTitleState = 0
        pass
    pygame.display.update()

def GameSystemBodyMain():
    """主菜单"""
    global GameSystemMenuState, GameSystemMenuItems, GameSystemMenuItemSelected, GameSystemMenuFont

    # 加载字体
    if GameSystemMenuFont is None:
        GameSystemMenuFont = pygame.font.SysFont(None, 48)

    # 清空窗口
    GAMEWINDOW.fill(BLACK)

    # 绘制菜单项
    for i, item in enumerate(GameSystemMenuItems):
        color = PINK if i == GameSystemMenuItemSelected else WHITE
        text = GameSystemMenuFont.render(item, True, color)
        text_rect = text.get_rect(center=(WindowWidth // 2, WindowHeight // 2 + i * 80 - 40))
        GAMEWINDOW.blit(text, text_rect)

    pygame.display.update()
# Main Body
# 创建窗口实例，实例名字为GAMEWINDOW
pygame.init()
pygame.font.init()
pygame.display.set_caption(GameSystemSettingVariable_WindowsName)
GAMEWINDOW = pygame.display.set_mode((GameSystemSettingVariable_WindowWidth, GameSystemSettingVariable_WindowHeight))
GAMEWINDOW.fill(BLACK)
while True:
    # 检查状态并执行相应功能
    if GameSystemTitleState < 3:
        GameSystemBodyOpen()
    else:
        GameSystemBodyMain()
        GameSystemMenuState = 1

    for event in pygame.event.get():
        if event.type == QUIT:  # 关闭窗口
            pygame.quit()
            sys.exit()

        if GameSystemMenuState == 1:  # 主菜单状态下
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    GameSystemMenuItemSelected = max(0, GameSystemMenuItemSelected - 1)
                elif event.key == K_DOWN:
                    GameSystemMenuItemSelected = min(len(GameSystemMenuItems) - 1, GameSystemMenuItemSelected + 1)
                elif event.key == K_RETURN:
                    if GameSystemMenuItemSelected == 0:
                        print("开始游戏")
                    elif GameSystemMenuItemSelected == 1:
                        pygame.quit()
                        sys.exit()