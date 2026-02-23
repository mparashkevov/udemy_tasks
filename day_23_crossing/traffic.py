import random
from turtle import Turtle



class Traffic:
	def __init__(self, lane_height=40, spawn_chance=0.08, base_speed=5):
		self.lane_height = lane_height
		self.spawn_chance = spawn_chance  # spawn probability per lane per tick
		self.base_speed = base_speed
		self.vehicle_colors = [
			"#e74c3c", "#3498db", "#f1c40f", "#2ecc71", "#9b59b6", "#e67e22", "#1abc9c",
		]
		# Stretch lengths approximate different vehicle sizes
		self.vehicle_lengths = {"car": 2, "bus": 3.5, "truck": 4.5}
		self.vehicles = []
		self.lanes = self._build_lanes()

	def _build_lanes(self):
		lanes = []
		pattern = ["road", "road", "road", "grass"]
		current_y = 330
		finish_y = -350
		index = 0
		while current_y - self.lane_height >= finish_y:
			lane_type = pattern[index % len(pattern)]
			if lane_type == "road":
				direction_left = len(lanes) % 2 == 0  # alternate directions per road lane
				center_y = current_y - (self.lane_height / 2)
				speed = self.base_speed + (len(lanes) % 3)  # slight variation per lane
				lanes.append({"y": center_y, "direction_left": direction_left, "speed": speed})
			current_y -= self.lane_height
			index += 1
		return lanes

	def _spawn_clear(self, lane, buffer_distance=140):
		start_x = 320 if lane["direction_left"] else -320
		for vehicle in self.vehicles:
			vy = vehicle["turtle"].ycor()
			if abs(vy - lane["y"]) < (self.lane_height / 2):
				vx = vehicle["turtle"].xcor()
				if lane["direction_left"] and vx > start_x - buffer_distance:
					return False
				if not lane["direction_left"] and vx < start_x + buffer_distance:
					return False
		return True

	def _create_vehicle(self, lane):
		kind = random.choice(list(self.vehicle_lengths.keys()))
		length = self.vehicle_lengths[kind]
		vehicle = Turtle("square")
		vehicle.penup()
		vehicle.color(random.choice(self.vehicle_colors))
		vehicle.shapesize(stretch_wid=1.2, stretch_len=length)
		vehicle.setheading(180 if lane["direction_left"] else 0)
		start_x = 320 if lane["direction_left"] else -320
		vehicle.goto(start_x, lane["y"])
		self.vehicles.append({"turtle": vehicle, "speed": lane["speed"]})

	def maybe_spawn(self):
		for lane in self.lanes:
			if random.random() < self.spawn_chance and self._spawn_clear(lane):
				self._create_vehicle(lane)

	def move(self):
		for vehicle in list(self.vehicles):
			vehicle["turtle"].forward(vehicle["speed"])
			x = vehicle["turtle"].xcor()
			if x < -340 or x > 340:
				vehicle["turtle"].hideturtle()
				self.vehicles.remove(vehicle)

	def clear_vehicles(self):
		"""Hide and remove all active vehicles (useful between levels)."""
		for vehicle in self.vehicles:
			vehicle["turtle"].hideturtle()
		self.vehicles.clear()

	def set_level(self, level: int, min_speed=3.0, max_speed=10.0, min_spawn=0.04, max_spawn=0.18):
		"""Scale speeds and spawn chance based on level (1-10)."""
		level = max(1, min(10, level))
		ratio = (level - 1) / 9  # 0 at level 1, 1 at level 10
		self.base_speed = min_speed + (max_speed - min_speed) * ratio
		self.spawn_chance = min_spawn + (max_spawn - min_spawn) * ratio
		# Update lane speeds
		for idx, lane in enumerate(self.lanes):
			lane["speed"] = self.base_speed + (idx % 3)
		# Update active vehicle speeds to match new lane base
		for vehicle in self.vehicles:
			vy = vehicle["turtle"].ycor()
			for lane in self.lanes:
				if abs(vy - lane["y"]) <= (self.lane_height / 2):
					vehicle["speed"] = lane["speed"]
					break

