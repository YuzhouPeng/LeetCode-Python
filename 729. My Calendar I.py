class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start, end):
        for s, e in self.intervals:
            if start < e and end > s: return False # From condition if not (start >= e or end <= s)
        self.intervals.append((start, end))
        return True