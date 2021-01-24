class dates:
    def set_name(self, name):
        #name of what date is for (test/assignment)
        self.name = name

    def set_year(self, n):
        #year
        self.year = n
    
    def set_month(self, m):
        #month
        self.month = m

    def set_day(self, d):
        #date
        self.day = d

    def get_name(self):
        return self.name
    
    def get_year(self):
        return self.year
    
    def get_month(self):
        return self.month
    
    def get_day(self):
        return self.day