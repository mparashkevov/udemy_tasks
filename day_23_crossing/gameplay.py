import time
from turtle import Turtle

from game_screen import GameScreen
from traffic import Traffic


LANE_HEIGHT = 40
PLAYER_START_POS = (0, -370)  # lane-aligned: 310 - 17*40
PLAYER_STEP = LANE_HEIGHT  # move one full lane per key press
START_LIVES = 3
TICK = 0.05
FINISH_Y = 350  # lane-aligned: 310 - (-1)*40; crossing the top line advances level
MAX_LEVEL = 10


def create_player():
	player = Turtle("turtle")
	player.color("green")
	player.penup()
	player.setheading(90)
	player.goto(PLAYER_START_POS)
	player.speed(0)
	return player


def bind_controls(screen: GameScreen, player: Turtle):
	def move_up():
		new_y = player.ycor() + PLAYER_STEP
		if new_y <= FINISH_Y:
			player.sety(new_y)

	def move_down():
		new_y = player.ycor() - PLAYER_STEP
		if new_y >= PLAYER_START_POS[1]:
			player.sety(new_y)

	screen.screen.listen()
	screen.screen.onkey(move_up, "Up")
	screen.screen.onkey(move_down, "Down")


def reset_player(player: Turtle):
	player.goto(PLAYER_START_POS)
	player.setheading(90)


def collision_with_vehicle(player: Turtle, traffic: Traffic, radius=25):
	for vehicle in traffic.vehicles:
		if player.distance(vehicle["turtle"]) < radius:
			return True
	return False


def main():
	screen = GameScreen()
	screen.draw_start_line()
	screen.draw_finish_line()
	screen.draw_lanes(lane_height=LANE_HEIGHT)

	traffic = Traffic(lane_height=LANE_HEIGHT)
	player = create_player()
	bind_controls(screen, player)

	lives = START_LIVES
	level = 1
	running = True
	traffic.set_level(level)
	screen.update_hud(level=level, lives=lives)

	while running:
		time.sleep(TICK)
		traffic.maybe_spawn()
		traffic.move()

		if collision_with_vehicle(player, traffic):
			lives -= 1
			screen.update_hud(level=level, lives=lives)
			if lives <= 0:
				screen.game_over()
				running = False
				continue
			reset_player(player)

		# Level up when reaching the top (near start line)
		if player.ycor() >= FINISH_Y:
			if level < MAX_LEVEL:
				level += 1
			traffic.clear_vehicles()
			traffic.set_level(level)
			screen.update_hud(level=level, lives=lives)
			reset_player(player)

		screen.update()

	screen.exitonclick()


if __name__ == "__main__":
	main()
