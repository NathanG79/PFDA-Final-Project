import math
import pygame



class Upgrade():

    def __init__(self, name="special\\The_Void", size_mult=1/3,
                 center_pos=(0,0)):
        self.name = name
        self.size = (270 * size_mult, 315 * size_mult)
        self.orig_pos = (center_pos[0] - self.size[0] / 2,
                         center_pos[1] - self.size[1] / 2)
        self.pos = self.orig_pos
        self.image = self._init_image()
        self.points = self._update_highlight_points()
        self.highlight_color = pygame.Color(250,250,250)
        self.is_active = False

    def _init_image(self):
        image = pygame.image.load(f"icons\\{self.name}.webp")
        image = pygame.transform.scale(image, self.size)
        return image

    def _update_highlight_points(self):
        radius = 60
        points = []
        center = (self.pos[0] + self.size[0] / 2,
                    self.pos[1] + self.size[1] / 2)
        for n in range(0,6):
            degrees = n * 60 + 30
            radians = degrees * math.pi / 180
            new_point = (center[0] + radius * math.cos(radians),
                         center[1] + radius * math.sin(radians))
            points.append(new_point)
        return points

    def draw(self, surface):
        if self.is_active:
            pygame.draw.polygon(surface, self.highlight_color, self.points)
        surface.blit(self.image, self.pos)

    def scroll(self, scroll_pos):
        self.pos = (self.orig_pos[0],
                    self.orig_pos[1] + scroll_pos)
        self.points = self._update_highlight_points()

    def click(self):
        rect = self.image.get_rect()
        rect = pygame.Rect(self.pos[0], self.pos[1],
                           rect[2], rect[3])
        mouse_pos = pygame.mouse.get_pos()
        was_clicked_on = rect.collidepoint(mouse_pos)
        if was_clicked_on:
            self.is_active = not self.is_active 





def limit_value(min, target, max):
    if target < min:
        return min
    elif target > max:
        return max
    else:
        return target




def main():
    pygame.init()
    pygame.display.set_caption("Nova Drift Build Planner")
    resolution = (800, 600)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()
    dt = 0
    bg_color = pygame.Color(50, 50, 50)

    running = True
    volley = Upgrade("Volley", 1/3, (200, 200))
    mines = Upgrade("Mines", 1/3, (300, 150))
    scroll_direction = 0
    scroll_pos = 0
    min_scroll = -1000
    max_scroll = 0
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    scroll_direction = 1
                elif event.button == 5:
                    scroll_direction = -1

        # Game logic
        if scroll_direction != 0:
            scroll_pos += dt * scroll_direction
            scroll_pos = limit_value(min_scroll, scroll_pos, max_scroll)
            volley.scroll(scroll_pos)
            mines.scroll(scroll_pos)

        if pygame.mouse.get_just_pressed()[0]:
            volley.click()
            mines.click()

        # Render & Display
        screen.fill(bg_color)
        volley.draw(screen)
        mines.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)
        scroll_direction = 0

    pygame.quit()


if __name__ == "__main__":
    main()