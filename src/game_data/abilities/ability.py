

# parent class to all abilities
class Ability:

    # ===== lifecycle =====
    def continue_usage(self):

        # if the ability is marked as in use ( meaning that is has been used and is now in the process of resolving)
        if self.in_use:

            # animates through stages
            self.current_animation_counter += 1
            if self.current_animation_counter >= self.frame_counters[self.stage]:
                self.stage += 1

            # activates ability's effect on "3"
            if self.stage == 3:
                self.effect()

            # resets ability on "4"
            elif self.stage >= 4:
                self.reset()

    # ===== actual effect ====
    def effect(self):
        pass

    # ===== cooldown =====
    def tick_cooldown(self):
        if self.curr_cd > 0:
            self.curr_cd -= 1

    def start_cooldown(self):
        self.curr_cd = self.max_cd

    # ===== reset =====
    def reset(self):
        self.current_animation_counter = 0
        self.curr_cd = 0
        self.stage = 0
        self.in_use = False

    # constructor
    def __init__(self, sprite_row_num=1, frame_counters=(2, 5, 5, 2), cooldown=0, mp_cost=0, hp_cost=0):

        # row in character sprite set that the ability calls for
        self.sprite_row_num = sprite_row_num

        # frames between each sprite in ability sprite row
        self.frame_counters = frame_counters
        self.current_animation_counter = 0

        # time that needs to pass between usages of the ability
        self.max_cd = cooldown
        self.curr_cd = 0

        # cost of ability usage
        self.mp_cost = mp_cost
        self.hp_cost = hp_cost

        # marks the ability as in-use (this blocks ability switching mid-usage)
        self.in_use = False

        # current ability stage (defines the sprite that should be used for display)
        # 0 - default, 1,2,3 - stages of usage
        self.stage = 0
