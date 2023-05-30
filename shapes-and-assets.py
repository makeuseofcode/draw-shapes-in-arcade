import arcade

WIDTH = 800
HEIGHT = 600
blue = arcade.color.BLUE
red = arcade.color.RED
green = arcade.color.GREEN
yellow = arcade.color.YELLOW
orange = arcade.color.ORANGE
aqua = arcade.color.AQUA
texture = arcade.load_texture("texture.png")
points = ((400, 400), (500, 500), (600, 400), (500, 300))

def draw_shapes():
    arcade.draw_rectangle_filled(400, 300, 200, 100, blue)
    arcade.draw_circle_filled(600, 400, 50, red)
    arcade.draw_ellipse_filled(200, 500, 80, 40, green)

def draw_complex_shapes():
    arcade.draw_polygon_filled(points, yellow)
    arcade.draw_line(100, 100, 700, 500, orange, 5)

def draw_nested_shapes():
    arcade.draw_rectangle_filled(400, 300, 200, 100, blue)
    arcade.draw_circle_filled(400, 300, 50, yellow)
    arcade.draw_rectangle_filled(400, 300, 80, 20, red)

def draw_color_and_texture():
    arcade.draw_rectangle_filled(400, 300, 200, 100, aqua)
    arcade.draw_texture_rectangle(600, 400, 100, 100, texture)

def setup():
    arcade.open_window(WIDTH, HEIGHT, "Simple Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()

def main():
    setup()
    draw_shapes()
    draw_complex_shapes()
    draw_nested_shapes()
    draw_color_and_texture()
    arcade.finish_render()
    arcade.run()

if __name__ == "__main__":
    main()
