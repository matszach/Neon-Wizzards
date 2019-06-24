

# parent class to all abilities
class Ability:

    # ===== start =====
    def use(self):
        if not self.in_use:
            self.reset()
            self.in_use = True

    # ===== lifecycle =====
    def continue_usage(self):

        # if the ability is marked as in use ( meaning that is has been used and is now in the process of resolving)
        if self.in_use:

            # activates ability's take_effect on "3"
            if not self.executed and self.stage == 3:
                self.take_effect()
                self.executed = True

            # resets ability on "4"
            elif self.stage >= 4:
                self.reset()

            # animates through stages
            self.current_animation_counter += 1
            if self.current_animation_counter >= self.frame_counters[self.stage]:
                self.stage += 1

            # activates ability's take_effect on "3"
            if self.stage == 3:
                self.take_effect()

            # resets ability on "4"
            elif self.stage >= 4:
                self.reset()

    # ===== actual take_effect ====
    def take_effect(self):
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
        self.executed = False

    # constructor
    def __init__(self, user, sprite_row_num=1, frame_counters=(2, 5, 5, 2), cooldown=0, mp_cost=0, hp_cost=0):

        # user held for reference
        self.user = user

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

        # mark the ability s already executed in the current animation cycle
        self.executed = False

        # current ability stage (defines the sprite that should be used for display)
        # 0 - default, 1,2,3 - stages of usage
        self.stage = 0


