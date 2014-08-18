import werobot

robot = werobot.WeRoBot(token='1234abcd')

@robot.handler
def echo(message):
    return 'Hello World!'

robot.run(server='waitress')