"""example of inheritance"""

# class Messenger:
#     def use_keyboard(self):
#         print('using keyboard')

#     def send_message(self):
#         print('sending message')

#     def receive_message(self):
#         print('receive message')

# class Whatsapp(Messenger):
#     def send_message(self):
#         print('sending message via whatsapp')

#     def receive_message(self):
#          print('recevie message via whatsapp')

# class Facebook(Messenger):
#     def send_message(self):
#         print('sending message via facebook')

#     def receive_message(self):
#          print('recevie message via facebook')

# class Instagram(Messenger):
#     def send_message(self):
#         print('sending message via insta')

#     def receive_message(self):
#          print('recevie message via insta')

# wp = Whatsapp()
# wp.use_keyboard()
# wp.send_message()
# wp.receive_message()

# fb = Facebook()
# fb.use_keyboard()
# fb.send_message()
# fb.receive_message()

# ins = Instagram()
# ins.use_keyboard()
# ins.send_message()
# ins.receive_message()

"""inheritance ---> polymorphism"""

# class Messenger:
#     def use_keyboard(self):
#         print('using keyboard')

#     def send_message(self):
#         print('sending message')

#     def receive_message(self):
#         print('receive message')

# class Whatsapp(Messenger):
#     def send_message(self):
#         print('sending message via whatsapp')

#     def receive_message(self):
#          print('recevie message via whatsapp')

# class Facebook(Messenger):
#     def send_message(self):
#         print('sending message via facebook')

#     def receive_message(self):
#          print('recevie message via facebook')

# class Instagram(Messenger):
#     def send_message(self):
#         print('sending message via insta')

#     def receive_message(self):
#          print('recevie message via insta')

# def use_messenger(ref):
#     ref.use_keyboard()
#     ref.send_message()
#     ref.receive_message()

# wp = Whatsapp()

# fb = Facebook()

# ins = Instagram()

# use_messenger(wp)
# use_messenger(fb)
# use_messenger(ins)

"""Inheritance using specialized methods"""


class Messenger:
    def use_keyboard(self):
        print("using keyboard")

    def send_message(self):
        print("sending message")

    def receive_message(self):
        print("receive message")


class Whatsapp(Messenger):
    def send_message(self):
        print("sending message via whatsapp")

    def receive_message(self):
        print("recevie message via whatsapp")

    def live_location(self):
        print("live location is enabled in wp")


class Facebook(Messenger):
    def send_message(self):
        print("sending message via facebook")

    def receive_message(self):
        print("recevie message via facebook")

    def new_emoji(self):
        print("new emojis added in fb")


class Instagram(Messenger):
    def send_message(self):
        print("sending message via insta")

    def receive_message(self):
        print("recevie message via insta")

    def video_call(self):
        print("vc enabled in insta")


def use_messenger(ref):
    ref.use_keyboard()
    ref.send_message()
    ref.receive_message()

    if type(ref) == Whatsapp:
        ref.live_location()

    if type(ref) == Instagram:
        ref.video_call()

    if type(ref) == Facebook:
        ref.new_emoji()


wp = Whatsapp()

fb = Facebook()

ins = Instagram()

use_messenger(wp)
use_messenger(fb)
use_messenger(ins)
