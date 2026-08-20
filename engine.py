import pygame
import time

class Engine:
    def __init__(self):
        self.click_mode = 1 # 1: add 0: delete
        self.is_in_simulation = False
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0

        self.simulation_speed = 500 #milliseconds per gen
        self.current_time = 0
        self.last_gen_time = 0
        
    def handle_events(self, grid, display):
        """Handle pygame inputs and game events"""
        #ended up doing everything for the game loop, lol
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not self.is_in_simulation:
                    x, y = pygame.mouse.get_pos()
                    print(f"Left Clicked at {x, y}")
                    grid_index = display.get_index(x, y)
                    if grid_index:
                        row, col = grid_index
                        grid.edit_cell(row, col, self.click_mode)

                elif event.button == 3:
                    # print("Drag Start")
                    self.drag_start_x, self.drag_start_y = event.pos
                    self.is_dragging = True

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:
                    # print("Drag Stop")
                    self.is_dragging = False

            elif event.type == pygame.MOUSEMOTION:
                if self.is_dragging:
                    # print("Mouse Drag")
                    dx = event.pos[0] - self.drag_start_x
                    dy = event.pos[1] - self.drag_start_y

                    display.camera_x += dx
                    display.camera_y += dy

                    self.drag_start_x, self.drag_start_y = event.pos

            elif event.type == pygame.MOUSEWHEEL:
                mouse_x, mouse_y = pygame.mouse.get_pos()

                cell_x = (mouse_x - display.camera_x) / display.pixel_len
                cell_y = (mouse_y - display.camera_y) / display.pixel_len

                if event.y > 0:
                    display.pixel_len *= 1.1
                else:
                    display.pixel_len /= 1.1
                display.pixel_len = max(2, min(100, display.pixel_len))
                
                display.camera_x = mouse_x - (cell_x * display.pixel_len)
                display.camera_y = mouse_y - (cell_y * display.pixel_len)
                    
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.click_mode = 1
                elif event.key == pygame.K_d:
                    self.click_mode = 0
                elif event.key == pygame.K_SPACE:
                    if not self.is_in_simulation: 
                        print("Simulation Started; Edit Blocked")
                        self.is_in_simulation = True
                    else:
                        print("Simulation Stopped; Edit Mode")
                        self.is_in_simulation = False
                elif event.key == pygame.K_n:
                    grid.next_gen()
                    print("Step Forward Once")
                elif event.key == pygame.K_c and not self.is_in_simulation:
                    grid.clear_grid()
                    print("Board Cleared")

                elif event.key == pygame.K_ESCAPE:
                    return False
        if pygame.key.get_pressed()[pygame.K_s]:
            self.simulation_speed += 5
            self.simulation_speed = max(25, min(2000, self.simulation_speed))
        elif pygame.key.get_pressed()[pygame.K_f]:
            self.simulation_speed -= 5
            self.simulation_speed = max(25, min(2000, self.simulation_speed))
        
        if self.is_in_simulation:
            self.current_time = pygame.time.get_ticks()
            if self.current_time - self.last_gen_time >= self.simulation_speed:
                grid.next_gen()
                self.last_gen_time = self.current_time

        return True