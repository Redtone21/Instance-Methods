# class Student: 
#     def __init__(self, scores = []):
#         self.scores = scores

#     def avg(self):
#         return sum(self.scores) / len(self.scores)

# # object / instance
# kings  = Student(scores = [2,3,5,3,5,35])

# print(kings.avg())

#######################################

# # Rounded up
# class Student: 
#     def __init__(self, scores = []):
#         self.scores = scores

#     def avg(self):
#         return round(sum(self.scores) / len(self.scores))

# # object / instance
# kings  = Student(scores = [2,3,5,3,5,35])

# print(kings.avg())

#######################################
# Rounded up with another another student value
class Student: 
    def __init__(self, scores = []):
        self.scores = scores

    def avg(self):
        return round(sum(self.scores) / len(self.scores))

# object / instance
kings  = Student(scores = [2,3,5,3,5,35])
peter  = Student(scores = [27,30,5,3,5,35])

print(kings.avg())
print(peter.avg())