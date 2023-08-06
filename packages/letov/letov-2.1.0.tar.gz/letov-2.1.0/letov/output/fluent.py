import os

from io import BytesIO

import msgpack

from fluent.sender import FluentSender


class Fluent:
    def __init__(self, host=None, port=None):
        self.sender = FluentSender(
            'letov',
            host=host or os.environ['FLUENT_HOST'],
            port=port or int(os.environ['FLUENT_PORT']),
            buffer_overflow_handler=self.overflow_handler
        )

    @staticmethod
    def overflow_handler(pending):
        unpacker = msgpack.Unpacker(BytesIO(pending), raw=False)
        for tag, ts, record in unpacker:
            # last resort - try to send logs through docker engine (stdout)
            print(record['message'])

    def send(self, message):
        return self.sender.emit('applogs', {'message': message})

    def close(self):
        self.sender.close()
