from channels.routing import ProtocolTypeRouter

from chat.routing import websockets


application = ProtocolTypeRouter({
    "websocket": websockets
})
