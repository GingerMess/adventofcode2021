import dataclasses

import common


@dataclasses.dataclass
class FishTracker:
    fish_by_timer_value: dict

    def add_fish(self, timer_value):
        self.fish_by_timer_value[timer_value] = self.fish_by_timer_value.get(timer_value, 0) + 1

    def tick(self):
        # number of new fish = number of fish at timer 0. this also represents number of fish that just had offspring.
        new_fish = self.fish_by_timer_value.get(0, 0)
        # decrement all fish timers
        for timer_value in range(0, 8):
            self.fish_by_timer_value[timer_value] = self.fish_by_timer_value.get(timer_value+1, 0)
        # spawn new fish
        self.fish_by_timer_value[8] = new_fish
        # insert fish that just had offspring into timer 6
        self.fish_by_timer_value[6] = self.fish_by_timer_value.get(6, 0) + new_fish

    def total_fish(self):
        return sum(pair[1] for pair in self.fish_by_timer_value.items())


data = ''.join(common.read_all_data("input/day6.txt")).strip()
data = [int(num) for num in data.split(',')]
tracker = FishTracker({})
# existing fish
for existing_fish_timer in data:
    tracker.add_fish(existing_fish_timer)
# part 1 - 80 days
days = 80
for day in range(0, days):
    tracker.tick()
print(f"Fish after {days} days: {tracker.total_fish()}")
# part 2 - 256 days (actually 256-80)
days = 256-80
for day in range(0, days):
    tracker.tick()
print(f"Fish after 256 days: {tracker.total_fish()}")
