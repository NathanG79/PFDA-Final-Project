import csv
import pygame



class Upgrade():

    def __init__(self, name="special\\The_Void", size_mult=1/3,
                 center_pos=(0,0), is_active=False):
        self.name = name
        self.size = (270 * size_mult, 315 * size_mult)
        self.orig_pos = (center_pos[0] - self.size[0] / 2,
                         center_pos[1] - self.size[1] / 2)
        self.pos = self.orig_pos
        self.image, self.highlight_image = self._init_image()
        self.is_active = is_active
        self.off_alpha = 50
        self.update_alpha()

    def _init_image(self):
        image = pygame.image.load(f"icons\\{self.name}.webp")
        image = pygame.transform.scale(image, self.size)
        highlight_image = pygame.image.load(f"icons\\Special\\Highlight.png")
        highlight_image = pygame.transform.scale(highlight_image, self.size)
        return image, highlight_image

    def draw(self, surface):
        surface.blit(self.image, self.pos)
        if self.is_active:
            surface.blit(self.highlight_image, self.pos)

    def scroll(self, scroll_pos):
        self.pos = (self.orig_pos[0],
                    self.orig_pos[1] + scroll_pos)

    def toggle(self):
        self.is_active = not self.is_active
        self.update_alpha()

    def set_activity(self, new_state):
        self.is_active = new_state
        self.update_alpha()

    def update_alpha(self):
        if self.is_active:
            alpha = 255
        else:
            alpha = self.off_alpha
        self.image.set_alpha(alpha)

    def return_rect(self):
        rect = self.image.get_rect()
        rect = pygame.Rect(self.pos[0], self.pos[1],
                           rect[2], rect[3])
        return rect


class AllUpgrades():

    def __init__(self):
        self.mods = []        
        with open('mods.csv') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None) # skip header
            for (name, category, category_num, subcategory, subcategory_num,
            group_num, num_in_group, exclusive, parent, child) in csv_reader:
                x,y = self._get_position(category, int(subcategory_num),
                                         int(group_num), int(num_in_group))
                is_active = category == "gear" and int(num_in_group) == 0
                upgrade_object = Upgrade(name, 1/5, (x, y), is_active)
                rect = upgrade_object.return_rect()
                mutually_exclusive = list_from_csv_item(exclusive)
                parents = list_from_csv_item(parent)
                children = list_from_csv_item(child)
                self.mods.append([name, upgrade_object, rect,
                                  mutually_exclusive, parents,
                                  children])

    def _get_position(self, category, subcategory_num,
                      group_num, num_in_group):
        x, y = 0, 0
        x_diffs = (30, 0, 60, 30)
        y_diffs = (0, 50, 50, 100)
        if category == "gear":
            x = num_in_group * 60 + 50
            y = subcategory_num * 75
        elif category == "mod":
            x = 50 + 150 * (group_num % 7) + x_diffs[num_in_group - 1]
            y = 325 + 200 * (group_num // 7) + y_diffs[num_in_group - 1]
        elif category == "super":
            x = 50 + num_in_group * 30
            y = 1150 + (num_in_group % 2) * 50
        elif category == "wild":
            x = 50 + num_in_group * 30
            y = 1200 + subcategory_num * 125 + (num_in_group % 2) * 50
        return x, y

    def draw(self, surface):
        for mod in self.mods:
            mod[1].draw(surface)

    def scroll(self, scroll_pos):
        for mod in self.mods:
            mod[1].scroll(scroll_pos)
            mod[2] = mod[1].return_rect()

    def click(self):
        for mod in self.mods:
            rect = mod[2]
            mouse_pos = pygame.mouse.get_pos()
            was_clicked_on = rect.collidepoint(mouse_pos)
            if was_clicked_on:
                mod[1].toggle()
                if mod[3] != ['']:
                    for exclusive in mod[3]:
                        if exclusive != mod[0]:
                            index = self._find_index(exclusive)
                            self.mods[index][1].set_activity(False)
                return

    def _find_index(self, target):
        # This wouldn't be necessary if I used a dictionary instead.
        # However, to my understanding, iterating through a dictionary
        # is less efficient than through a list. Since iterating through
        # the set has to happen more often, I figure a list is overall
        # better.
        for index, mod in enumerate(self.mods):
            if mod[0] == target:
                return index




def limit_value(min, target, max):
    if target < min:
        return min
    elif target > max:
        return max
    else:
        return target


def list_from_csv_item(item):
    return item.split(";")




def main():
    pygame.init()
    pygame.display.set_caption("Nova Drift Build Planner")
    resolution = (1200, 900)
    screen = pygame.display.set_mode(resolution)

    clock = pygame.time.Clock()
    dt = 0
    bg_color = pygame.Color(50, 50, 50)

    running = True
    scroll_direction = 0
    scroll_pos = 0
    min_scroll = -1000
    max_scroll = 0
    allUpgrades = AllUpgrades()
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
            scroll_pos += dt * scroll_direction * 2
            scroll_pos = limit_value(min_scroll, scroll_pos, max_scroll)
            allUpgrades.scroll(scroll_pos)

        if pygame.mouse.get_just_pressed()[0]:
            allUpgrades.click()

        # Render & Display
        screen.fill(bg_color)
        allUpgrades.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)
        scroll_direction = 0

    pygame.quit()


if __name__ == "__main__":
    main()