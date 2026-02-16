class Student:
    def __init__(self, name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for i in self.marks:
            sum+=i
        print(f"Average marks of {self.name} is {sum/3}")
s1= Student("Aishwarya", [90, 95, 85])
s1.get_avg()
s1.name="Vishal"
s1.get_avg()