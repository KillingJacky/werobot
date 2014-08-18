import werobot

robot = werobot.WeRoBot(token='1234abcd')

@robot.text
def echo(message):
    print message.target
    print message.source
    print message.content
    return 'Hello World!'

@robot.handler
def default_handler(message):
    return 'Default Response'

robot.run(server='waitress',port='8123')
