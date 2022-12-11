class Word:
    def __init__(self, quantity, emotion, priority, nature, pronouns, pos_x,
                 pos_y, pos_z, family, context):
        self.quantity = quantity
        self.emotion = emotion
        self.priority = priority
        self.nature = nature
        self.pronouns = pronouns
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.family = family
        self.context = context

    def content(self):
        word_matrix = {
            "qty": self.quantity,
            "emotion": self.emotion,
            "priority": self.priority,
            "nature": self.nature,
            "pronouns": self.pronouns,
            "pos_x": self.pos_x,
            "pos_y": self.pos_y,
            "pos_z": self.pos_z,
            "family": self.family,
            "context": self.context
        }

        return word_matrix
