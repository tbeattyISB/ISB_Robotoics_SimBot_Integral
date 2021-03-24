from Robot import MainRun
# In this assignement you will crerate an integral controller (not used in the real world):
#


def go(bot):
    bot.setPayload(0)
    desired = 300
    kp = 10
    while True: #Edit this so that it stops at 300
        error = desired - bot.ultrasonic_sensor()
        bot.run(- error*kp)   # TRY EDITING THIS POWER (from -100 to 100)

MainRun(go)

# 1. Discuss the behavior of an integral only controller

# 2. Explain why a integral clear is needed when the bot passes the desired distance

# 3. Compared to a poportional controller, why wouldn't we use an integral only controller in the real world?