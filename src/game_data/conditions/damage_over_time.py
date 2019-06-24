from src.game_data.conditions.condition import Condition


# parent class to all damage over time effects
class DamageOverTime(Condition):

    def ongoing_effect(self, subject):
        subject.take_damage(self.dmg_amount, self.dmg_type)

    # constructor
    def __init__(self, dmg_amount, dmg_type, icon, duration=600, increment=30):

        # super constructor
        Condition.__init__(self, icon, duration, increment)

        # damage amount and type that's dealt to the subject every increment
        self.dmg_amount = dmg_amount
        self.dmg_type = dmg_type


# TODO Bleeding, Burning etc - here
