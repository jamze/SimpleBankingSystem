class Lightbulb:
    def __init__(self):
        self.state = "on"

    def change_state(self):
        if self.state == "on":
            self.state = "off"
        else:
            self.state = "on"

        print(f"Turning the light {self.state}")



# Lightbulb().change_state()

