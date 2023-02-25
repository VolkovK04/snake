import arcade

class MyWindow(arcade.Window):
    """
Move Sprite With Keyboard

Simple program to show moving a sprite with the keyboard.
The sprite_move_keyboard_better.py example is slightly better
in how it works, but also slightly more complex.

Artwork from https://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_keyboard
"""

import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5



class Node(arcade.Sprite):

    def update(self):

        self.center_x += self.change_x

        self.center_y += self.change_y

        if self.left < 0:

            self.left = 0

        elif self.right > SCREEN_WIDTH - 1:

            self.right = SCREEN_WIDTH - 1


        if self.bottom < 0:

            self.bottom = 0

        elif self.top > SCREEN_HEIGHT - 1:

            self.top = SCREEN_HEIGHT - 1



class MyGame(arcade.Window):
    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player_list = None

        self.player_sprite = None

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()

        self.player_sprite = Node(":resources:images/animated_characters/female_person/"
                                    "femalePerson_idle.png", SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

    def on_draw(self):

        self.clear()

        self.player_list.draw()

    def on_update(self, delta_time):

        # Move the player

        self.player_list.update()



    def on_key_press(self, key, modifiers):

        if key == arcade.key.UP:

            self.player_sprite.change_y = MOVEMENT_SPEED

        elif key == arcade.key.DOWN:

            self.player_sprite.change_y = -MOVEMENT_SPEED

        elif key == arcade.key.LEFT:

            self.player_sprite.change_x = -MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:

            self.player_sprite.change_x = MOVEMENT_SPEED



    def on_key_release(self, key, modifiers):

        if key == arcade.key.UP or key == arcade.key.DOWN:

            self.player_sprite.change_y = 0

        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:

            self.player_sprite.change_x = 0



def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()