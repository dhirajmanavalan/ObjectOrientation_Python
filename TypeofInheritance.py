class Messenger:
    def sendMessage(self):
        print("Message is sent")

    def receiveMessage(self):
        print("Message is received")


class InternalMessenger(Messenger):
    pass


class WhatsappMessenger(Messenger):
    def sendMessage(self):
        print("whatsapp is sent")

    def receiveMessage(self):
        print("whatsapp is received")

    def set_dp(self):
        print("dp is set")

    def set_status(self):
        print("status is set")


im = InternalMessenger()
im.sendMessage()
im.receiveMessage()

wp = WhatsappMessenger()
wp.sendMessage()
wp.receiveMessage()
wp.set_dp()
wp.set_status()
