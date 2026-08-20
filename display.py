import pygame

class Display:
    def __init__(
        self,
        title = "ConMan6767",
        screen_width = 1000,
        screen_height = 1000,
        pixel_len = 20
        ):
        pygame.init()
        self.title = title
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.pixel_len = pixel_len

        self.camera_x = 0
        self.camera_y = 0

        self.bg_color = (51, 69, 79)
        self.live_cell_color = (214, 211, 167)

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()
        self.fps = 30
    
    def get_index(self, x, y):
        """Returns cell coordinates"""
        return (
                (x - self.camera_x)//self.pixel_len,
                (y - self.camera_y)//self.pixel_len
            )

    def render(self, grid_data):
        """Renders on screen pixels to save processing"""
        self.screen.fill(self.bg_color)

        for x, y in grid_data:
            x_pos = x * self.pixel_len + self.camera_x
            y_pos = y * self.pixel_len + self.camera_y
            color = self.live_cell_color

            if -self.pixel_len <= x_pos <= self.screen_width and -self.pixel_len <= y_pos <= self.screen_height:
                pygame.draw.rect(self.screen, color, (x_pos, y_pos, self.pixel_len, self.pixel_len))
        
        pygame.display.flip()

    def tick(self):
        """I dont know what this does honestly"""
        self.clock.tick(self.fps)