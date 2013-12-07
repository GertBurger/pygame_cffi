
""" Mouse routines
"""

from pygame._sdl import sdl, ffi
from pygame.display import check_video

def get_pos():
    check_video()
    x = ffi.new("int[1]")
    y = ffi.new("int[1]")
    sdl.SDL_GetMouseState(x, y)
    return x[0], y[0]