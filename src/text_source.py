class StdinTextSource:
    def has_next(self) -> bool:
        self.line = input('Write something (or .quit to quit): ')
        return self.line != '.quit'
    
    def next(self) -> str:
        return self.line
