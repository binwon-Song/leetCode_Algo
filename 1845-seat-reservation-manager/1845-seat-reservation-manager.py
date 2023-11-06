import heapq

class SeatManager:

    def __init__(self, n: int):
        self.seats = [0] * (n + 1)
        self.del_points = []  # Use a min-heap for efficient retrieval of available seats
        self.reserve_point=0
    def reserve(self) -> int:
        if self.del_points:
            seat_number = heapq.heappop(self.del_points)
            self.seats[seat_number] = 1
            return seat_number
        else:
            self.reserve_point+=1
            self.seats[self.reserve_point]=1
            return self.reserve_point
        

    def unreserve(self, seatNumber: int) -> None:
        if self.seats[seatNumber] == 1:
            self.seats[seatNumber] = 0
            heapq.heappush(self.del_points, seatNumber)



# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)