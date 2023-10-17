import random


class Boss:
    def __init__(self, name: str, company: str):
        self.id = random.randint(1, 999)
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        text = f'Workers for {self.name} are:\n'
        for employee in self._workers:
            text += f'{employee["id_"]}, {employee["name"]}\n'

        return text

    @workers.setter
    def workers(self, worker):
        self._workers.append(worker)

    def __repr__(self):
        return f"Boss: {self.id} {self.name}"


class Worker:
    def __init__(self, name: str, boss: Boss):
        self.id_ = random.randint(1, 999)
        self.name = name
        self.boss = boss
        boss.workers = {"id_": self.id_, "name": name}

    def __repr__(self):
        return f"Worker: {self.id_} {self.name}"


# Example Usage:

boss1 = Boss("Richard", "Google")
boss2 = Boss("Nick", "Chrome")

workers1 = Worker("Steve", boss1)
workers2 = Worker("Franc", boss1)
workers3 = Worker("Dok", boss2)

print(boss1.workers)
print(boss2.workers)

print(boss1)
print(boss2)
