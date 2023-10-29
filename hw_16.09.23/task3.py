CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channel):
        self.channel = channel
        self.channel_now = 0

    def first_channel(self):
        self.channel_now = 0
        return self.channel[0]

    def last_channel(self):
        self.channel_now = len(self.channel) - 1
        return self.channel[-1]

    def turn_channel(self, number):
        if 1 <= number <= len(self.channel):
            self.channel_now = number - 1
            return self.channel[self.channel_now]
        else:
            return "There is no such channel"

    def next_channel(self):
        if self.channel_now == len(self.channel) - 1:
            self.channel_now = 0
        else:
            self.channel_now = self.channel_now + 1
        return self.channel[self.channel_now]

    def previous_channel(self):
        if self.channel_now == (len(self.channel) - 1):
            self.channel_now = (len(self.channel) - 1)
            print(self.channel_now)
        else:
            self.channel_now = self.channel_now - 1
        return self.channel[self.channel_now]

    def current_channel(self):
        return self.channel[self.channel_now]

    def is_exist(self, n):
        if isinstance(n, int):
            if 1 <= n <= len(self.channel):
                return "Yes"
            else:
                return "No"
        elif isinstance(n, str):
            if n in self.channel:
                return "Yes"
            else:
                return "No"


controller = TVController(CHANNELS)

print(controller.first_channel())  # == "BBC"

print(controller.last_channel())  # == "TV1000"

print(controller.turn_channel(1))  # == "BBC"

print(controller.next_channel())  # == "Discovery"

print(controller.previous_channel())  # == "BBC"

print(controller.current_channel())  # == "BBC"

print(controller.is_exist(4))  # == "No"

print(controller.is_exist("BBC"))  # == "Yes"
