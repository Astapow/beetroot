import random


class Boss:
    def __init__(self, name: str, company: str):
        self.id = random.randint(1, 999)
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        self._workers.append(worker)

    def __repr__(self):
        return f"Boss: {self.id} {self.name}"


class Worker:
    def __init__(self, name: str, boss: Boss):
        self.id = random.randint(1, 999)
        self.name = name
        self.boss = boss
        boss.add_worker(self)

    def __repr__(self):
        return f"Worker: {self.id} {self.name}"


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
