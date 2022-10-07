class MyCalendarThree:

    def __init__(self):
        self.bookings = [[float('-inf'), 0],[float('inf'), 0]]
        self.max_booking = 0        

    def book(self, start: int, end: int) -> int:
        index = bisect.bisect_left(self.bookings, [start,-1])

        if self.bookings[index][0] != start:
            count = self.bookings[index-1][1]
            self.bookings.insert(index, [start,count+1])
            self.max_booking = max(self.max_booking, count + 1)
            index += 1

        while end > self.bookings[index][0]:
            self.bookings[index][1] += 1
            self.max_booking = max(self.max_booking, self.bookings[index][1])
            index += 1

        if self.bookings[index][0] != end:
            count = self.bookings[index-1][1]
            self.bookings.insert(index, [end, count-1])

        return self.max_booking

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)