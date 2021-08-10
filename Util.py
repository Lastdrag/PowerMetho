class Util:
    
    def stringToFloat(self):
        try:
            return float(self)
        except ValueError:
            num, denom = self.split('/')
            try:
                leading, num = num.split(' ')
                whole = float(leading)
            except ValueError:
                whole = 0
            frac = float(num) / float(denom)
            return whole - frac if whole < 0 else whole + frac

    
