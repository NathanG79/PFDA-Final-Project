import pygame



class Upgrade():

    def __init__(self, name="special\\The_Void", size_mult=1/3, center_pos=(0,0), ):
        self.name = name
        self.size = self._init_size(size_mult)
        self.pos = self._init_pos(center_pos)
        self.image = self._init_image()

    def _init_size(self, size_mult):
        scaled_size = (270 * size_mult, 315 * size_mult)
        return scaled_size

    def _init_pos(self, center):
        x_pos = center[0] - self.size[0]
        y_pos = center[1] - self.size[1]
        return (x_pos, y_pos)

    def _init_image(self):
        image = pygame.image.load(f"icons\\{self.name}.webp")
        image = pygame.transform.scale(image, self.size)
        return image

    def draw(self, surface):
        surface.blit(self.image, self.pos)



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
    while running:
        # Event Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic
        
        # Render & Display
        screen.fill(bg_color)
        volley.draw(screen)
        mines.draw(screen)
        pygame.display.flip()
        dt = clock.tick(12)

    pygame.quit()


if __name__ == "__main__":
    main()