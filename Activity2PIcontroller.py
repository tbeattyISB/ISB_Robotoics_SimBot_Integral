from Robot import MainRun

# In this problem you will need too create a PROPORTIONAL CONTROLLER for your robot.
# Steps:  - Create a proportional controller
#         - Create an integral controller
#         - Your power formula should then be  eror * kp + integral * ki
#         - Make sure that your integral resets after it crosses the desired position
#         - Try creating a range in which integral is added (abs(error) < 100)

def go(bot):

    while True:
        ...

MainRun(go)


# How  does changing your ki (integral constant) affect:
#   1. speed,
#   2. overshoot and
#   3. stability
# Answer below (as comment):