import pygame
import sys
import time

from display import Display
from grid import Grid
from engine import Engine

def main():
    display = Display()
    grid = Grid()
    engine = Engine()

    running = True

    while running:
        running = engine.handle_events(grid, display)
        display.render(grid.get_grid_data())
        display.tick()

if __name__ == "__main__":
    main()