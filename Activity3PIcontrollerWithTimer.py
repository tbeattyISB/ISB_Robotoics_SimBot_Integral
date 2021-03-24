from RobotHW import MainRun

# Copy your code from Activity2, you may need to adjust your kp and ki.
# Within your while loop add conditional statements that change the desired time IF(bot.runTime()>...)
# At the end, remove the payload and see how your robot preforms.
#
# Starting at 700,
# Move to 300,
# Move back to 500
# Move forward to 50
#

def go(bot):
    bot.setPayload(20)
    while True:
        # Replace with your code

MainRun(go)

# 1. What cnnection (familiarity) do you have to a integral controller?
# 2. How has it extended your thinking?
# 3. What question do you have about integral controllers?
# Answer below (as comment):