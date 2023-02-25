import arcade

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Snake"
PLAYER_MOVEMENT_SPEED = 5


class MyGame(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color((10, 242, 157))

        self.scene = None
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        self.scene = arcade.Scene()

    def on_draw(self):
        self.clear()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
