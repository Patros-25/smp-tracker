def daily_tracker(sleep, water, steps):
    print(sleep, water, steps)
daily_tracker("7 hours", "8 glasses", "1000 steps")

weekly_log =["7 hours", "8 glasses", "8000 steps"]
for log in weekly_log:
    print("Monday: ", log)


# Inside tracker.py after a conflict, Git inserts markers:

<<<<<<< HEAD
def assess_day(steps):
    return steps >= 10000
=======
def assess_day(steps, goal=10000):
    return steps >= goal
>>>>>>> feature/flexible-goal

# HEAD = your current branch (main)
# Everything between === and >>> = the incoming branch changes
# Decision: pick one, combine both, or write something new
# Then delete all marker lines and save