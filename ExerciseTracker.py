class Tracker:
    def __init__(self):
        self.exercises = set()
        self.exercise_count = {}
        self.exercise_type = {"mental":set(), "physical":set()}
    
    def add_exercise(self, exercise, physical):
        if (exercise in self.exercises):
            print("Exercise already added!")
        else:
            if physical:
                self.exercise_type["physical"].add(exercise)
            else:
                self.exercise_type["mental"].add(exercise)
            self.exercises.add(exercise)
            self.exercise_count[exercise] = 1
    
    def increment_exercise(self, exercise):
        if (exercise not in self.exercises):
            print("Exercise doesn't exist, did you mean to add it?")
        else:
            self.exercise_count[exercise] += 1
    
    def decrement_exercise(self, exercise):
        if (exercise not in self.exercises):
            print("Exercise doesn't exist, did you mean to add it?")
        elif (self.exercise_count[exercise] == 0):
            pass
        else:
            self.exercise_count[exercise] -= 1
    
    def remove_exercise(self, exercise):
        if (exercise not in self.exercises):
            print("Exercise not found.")
        else:
            self.exercises.remove(exercise)
            del self.exercise_count[exercise]
    
    def list_exercises(self, type_exercises):
        if (type_exercises == "physical"):
            return self.exercise_type["physical"]
        else:
            return self.exercise_type["mental"]

def main():
    tracker = Tracker()
    init_msg = "Welcome to our mindful fitness tracker! Options: \n" \
        + "1: Add exercise \n2: Remove exercise \n3 Increment Exercise\n4 Decrement Exercise" \
            + "\n5 View Exercises\nq to quit"
    
    while True:
        print(init_msg)
        choice = input("Enter your choice: ")
        
        if choice == "1":
            exercise = input("Enter the name of the exercise: ")
            physical = input("Is this a physical exercise? (yes/no): ").lower() == 'yes'
            tracker.add_exercise(exercise, physical)
        
        elif choice == "2":
            exercise = input("Enter the name of the exercise to remove: ")
            tracker.remove_exercise(exercise)
        
        elif choice == "3":
            exercise = input("Enter the name of the exercise to increment: ")
            tracker.increment_exercise(exercise)
        
        elif choice == "4":
            exercise = input("Enter the name of the exercise to decrement: ")
            tracker.decrement_exercise(exercise)
        
        elif choice == "5":
            exercise = input("Enter the type of exercises (mental/physical): ")
            print(tracker.list_exercises(exercise))
        
        elif choice == "q":
            print("Exiting the tracker. Stay healthy and mindful!")
            break
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()