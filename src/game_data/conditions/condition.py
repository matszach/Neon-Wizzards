

# parent class to all Conditions
class Condition:

    # ===== lifecycle =====
    # called every frame by it's subject
    def tick(self, subject):

        # TODO check if not expired here ?
        #  probably unnecessary as player should remove any expired conditions before this is called again

        # expire on duration end
        self.duration_left -= 1
        if self.duration_left < 0:
            self.end(subject)

        # manage ongoing effects
        self.curr_increment += 1
        if self.curr_increment >= self.max_increment:
            self.curr_increment = 0
            self.affect_self()
            self.ongoing_effect(subject)

    # called every increment, ongoing condition my change as it progresses (reduce/increase in power, change increment)
    def affect_self(self):
        pass

    # ===== condition starting =====
    # this should be called by characters ~"apply_condition" method todo
    def start(self, subject):
        pass

    # ===== condition ongoing effect =====
    # this may take a form of an actual effect lke taking damage
    # or of an animation (sow particles appearing over a slowed target
    def ongoing_effect(self, subject):
        pass

    # ===== condition ending =====
    # some effect may have different effects on dispel and on natural end
    def dispel(self, subject):
        self.on_dispel(subject)
        self.expired = True

    def on_dispel(self, subject):
        pass

    def end(self, subject):
        self.on_end(subject)
        self.expired = True

    def on_end(self, subject):
        pass

    # constructor
    def __init__(self, icon, duration=600, increment=30):

        # effect icon
        self.icon = icon

        # duration left, in frames
        self.duration_left = duration

        # increment between ongoing effects
        self.max_increment = increment
        self.curr_increment = 0

        # marks the condition as finished, ready to be removed from character's condition lists
        self.expired = False
