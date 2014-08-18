import werobot

robot = werobot.WeRoBot(token='1234abcd')

@robot.handler
def echo(message):
    print message.target
    print message.source
    return 'Hello World!'

robot.run(server='waitress',port='8123')
