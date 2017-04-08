class GenerateMessage:

    def __init__(self, message):
        self.message = message

    def generatee_welcome_node(self):

        message = {
            "text":"Pick a color:",
            "quick_replies":[
                {
                    "content_type":"text",
                    "title":"Red",
                    "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_RED",
                    "image_url":"http://petersfantastichats.com/img/red.png"
                },
                {
                    "content_type":"text",
                    "title":"Green",
                    "payload":"DEVELOPER_DEFINED_PAYLOAD_FOR_PICKING_GREEN",
                    "image_url":"http://petersfantastichats.com/img/green.png"
                }
            ]
        }

        return message