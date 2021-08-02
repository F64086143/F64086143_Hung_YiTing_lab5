import pygame
import os

MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))


class UpgradeMenu:
    def __init__(self, x, y):
        #命名＆設定三張圖片大小
        self.menu_image = pygame.transform.scale(MENU_IMAGE, (200, 200))
        self.upgrade_images = pygame.transform.scale(UPGRADE_IMAGE, (60, 40))
        self.sell_images = pygame.transform.scale(SELL_IMAGE, (40, 40))

        self.rect = self.menu_image.get_rect()
        self.rect.center = (x, y)#center of menu_image

        self.__buttons = [Button(self.upgrade_images, 'upgrade', self.rect.centerx, self.rect.centery-75),
                          Button(self.sell_images, 'sell', self.rect.centerx, self.rect.centery+75)]  # (Q2) Add buttons here

        pass

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu_image, (self.rect.centerx-110, self.rect.centery-110))

        # draw button
        # (Q2) Draw buttons here
        win.blit(self.upgrade_images, (self.rect.centerx - 35, self.rect.centery - 100))
        win.blit(self.sell_images, (self.rect.centerx - 25, self.rect.centery + 50))
        pass

    def get_buttons(self, x, y):
        """
        (Q1) Return the button list.
        (This method is call in get_click() method in class TowerGroup)
        :return: list
        """
        if self.rect.collidepoint(x, y):
            return self.__buttons

class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is call in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        # 判斷有沒有點在upgrade和sell內
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False

        pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name
        pass






