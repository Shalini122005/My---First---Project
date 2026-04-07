class Robot:

    def __init__(self, width: int, height: int):
        self.w = width
        self.h = height
        self.x = 0
        self.y = 0
        self.dir = 0  # 0=East, 1=North, 2=West, 3=South
        self.perimeter = 2 * (width + height) - 4
        self.started = False

    def step(self, num: int) -> None:
        if self.perimeter == 0:
            return
        
        num %= self.perimeter
        
        if num == 0 and self.started:
            num = self.perimeter
        
        self.started = True
        
        while num > 0:
            if self.dir == 0:  # East
                move = min(num, self.w - 1 - self.x)
                self.x += move
            elif self.dir == 1:  # North
                move = min(num, self.h - 1 - self.y)
                self.y += move
            elif self.dir == 2:  # West
                move = min(num, self.x)
                self.x -= move
            else:  # South
                move = min(num, self.y)
                self.y -= move
            
            num -= move
            
            if num > 0:
                self.dir = (self.dir + 1) % 4

    def getPos(self) -> list:
        return [self.x, self.y]

    def getDir(self) -> str:
        dirs = ["East", "North", "West", "South"]
        return dirs[self.dir]
        
