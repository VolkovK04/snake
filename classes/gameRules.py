from dataclasses import dataclass


@dataclass
class GameRules:
    map_size: int = 30
    wall_size: int = 5
    all_food_count: int = 10
    snake_spawn_size: int = 4

    square_wall_count_max: int = 5
    straight_wall_count_max: int = 10
    single_wall_count_max: int = 15
