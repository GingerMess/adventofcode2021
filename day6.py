import dataclasses
import common


@dataclasses.dataclass
class LanternFish:
    timer: int = 8

    def tick(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return self.spawn()
        return None

    def spawn(self):
        return LanternFish()

    def __str__(self):
        return str(self.timer)

    def __repr__(self):
        return self.__str__()


data = ''.join(common.read_all_data("input/day6.txt")).strip()
data = [int(num) for num in data.split(',')]
fish = []
# existing fish
for existing_fish_timer in data:
    fish.append(LanternFish(existing_fish_timer))
days = 80
for day in range(0, days):
    new_fish = []
    for f in fish:
        result = f.tick()
        if result is not None:
            new_fish.append(result)
    fish.extend(new_fish)

print(f"Fish after {days} days: {len(fish)}")
