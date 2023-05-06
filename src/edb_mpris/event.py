from enum import Enum
from typing import List


class EventParamType(Enum):
    STRING = "string"
    BOOLEAN = "boolean"
    INTEGER = "integer"


class EventType(Enum):
    PLAY = "PLAY"
    PAUSE = "PAUSE"
    NEXT = "NEXT"
    PREV = "PREV"
    MUTE = "MUTE"
    UNMUTE = "UNMUTE"
    TOGGLE_PLAY = "TOGGLE_PLAY"
    TOGGLE_MUTE = "TOGGLE_MUTE"


class EventParam:
    def __init__(self, name: EventType, ptype: EventParamType):
        self.name = name
        self.ptype = ptype


class Event:
    def __init__(self, name: str, description: str, parameters: List[EventParam]):
        self.name = name
        self.description = description
        self.parameters = parameters


events: List[Event] = [
    Event(EventType.PLAY, "Send play track to one or more media players", [EventParam("player", EventParamType.STRING)]),
    Event(EventType.PAUSE, "Send pause track event to one or more media players", [EventParam("player", EventParamType.STRING)]),
    Event(EventType.TOGGLE_PLAY, "Toggles the play state of one or more media players", [EventParam("player", EventParamType.STRING)]),
    Event(EventType.NEXT, "Send next track event to one or more media players", [EventParam("player", EventParamType.STRING)]),
    Event(EventType.PREV, "Send previous track event to one or more media players", [EventParam("player", EventParamType.STRING)]),
    Event(EventType.MUTE, "Send mute audio event to one or more media players", [EventParam("player", EventParamType.STRING)]),
    Event(EventType.UNMUTE, "Send unmute audio event to one or more media players", [EventParam("player", EventParamType.STRING)]),
    Event(EventType.TOGGLE_MUTE, "Toggles the mute state of one or more media players", [EventParam("player", EventParamType.STRING)])
]
