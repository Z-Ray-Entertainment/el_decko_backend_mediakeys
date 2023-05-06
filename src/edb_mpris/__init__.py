import pympris
import dbus
from dbus.mainloop.glib import DBusGMainLoop
from pympris import PyMPRISException

from edb_mpris.event import EventType

VERSION = "2023.5.6.1"
dbus_loop = DBusGMainLoop()
bus = dbus.SessionBus(mainloop=dbus_loop)
player_volumes = []


def edb_init():
    pass


def edb_stop():
    pass


def edb_fire_event(event_type: str, event_parameters: dict = None):
    players_ids = list(pympris.available_players())
    __make_request(EventType[event_type].value, players_ids, event_parameters)


def edb_available_events() -> dict:
    pass


def __make_request(event_type: EventType, player_ids, event_parameters: dict = None):
    player_name = ""
    if event_parameters and "player" in event_parameters:
        player_name = event_parameters["player"]

    match event_type:
        case EventType.MUTE.value:
            __unmute(player_ids, player_name)
        case EventType.UNMUTE.value:
            __mute(player_ids, player_name)
        case EventType.TOGGLE_MUTE.value:
            __toggle_mute(player_ids, player_name)
        case EventType.PREV.value:
            __prev(player_ids, player_name)
        case EventType.NEXT.value:
            __next(player_ids, player_name)
        case EventType.PAUSE.value:
            __pause(player_ids, player_name)
        case EventType.PLAY.value:
            __play(player_ids, player_name)
        case EventType.TOGGLE_PLAY.value:
            __toggle_play(player_ids, player_name)


def __play(player_ids, player_name):
    if player_name != "":
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if player_name.lower() in str(media_player.root.Identity).lower():
                if media_player.player.CanPlay:
                    media_player.player.Play()
    else:
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if media_player.player.CanPlay:
                media_player.player.Play()


def __pause(player_ids, player_name):
    if player_name != "":
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if player_name.lower() in str(media_player.root.Identity).lower():
                if media_player.player.CanPause:
                    media_player.player.Pause()
    else:
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if media_player.player.CanPause:
                media_player.player.Pause()


def __toggle_play(player_ids, player_name):
    if player_name != "":
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if player_name.lower() in str(media_player.root.Identity).lower():
                if media_player.player.CanPlay and media_player.player.CanPause:
                    media_player.player.PlayPause()
    else:
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if media_player.player.CanPlay and media_player.player.CanPause:
                media_player.player.PlayPause()


def __next(player_ids, player_name):
    if player_name != "":
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if player_name.lower() in str(media_player.root.Identity).lower():
                if media_player.player.CanGoNext:
                    media_player.player.Next()
    else:
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            media_player.player.Pause()
            if media_player.player.CanGoNext:
                media_player.player.Next()


def __prev(player_ids, player_name):
    if player_name != "":
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if player_name.lower() in str(media_player.root.Identity).lower():
                if media_player.player.CanGoNext:
                    media_player.player.Previous()
    else:
        for player in player_ids:
            media_player = pympris.MediaPlayer(player, bus)
            if media_player.player.CanGoPrevious:
                media_player.player.Previous()


def __mute(player_ids, player_name):
    try:
        if player_name != "":
            for player in player_ids:
                media_player = pympris.MediaPlayer(player, bus)
                if player_name.lower() in str(media_player.root.Identity).lower():
                    player_volumes[media_player.root.Identity] = media_player.player.Volume
                    media_player.player.Volume = 0
        else:
            for player in player_ids:
                media_player = pympris.MediaPlayer(player, bus)
                player_volumes[media_player.root.Identity] = media_player.player.Volume
                media_player.player.Volume = 0
    except PyMPRISException:
        print("WARN: Player " + player_name + " does not support interface Volume!")


def __unmute(player_ids, player_name):
    try:
        if player_name != "":
            for player in player_ids:
                media_player = pympris.MediaPlayer(player, bus)
                if player_name.lower() in str(media_player.root.Identity).lower():
                    media_player.player.Volume = player_volumes[media_player.root.Identity]
        else:
            for player in player_ids:
                media_player = pympris.MediaPlayer(player, bus)
                media_player.player.Volume = player_volumes[media_player.root.Identity]
    except PyMPRISException:
        print("WARN: Player " + player_name + " does not support interface Volume!")


def __toggle_mute(player_ids, player_name):
    try:
        if player_name != "":
            for player in player_ids:
                media_player = pympris.MediaPlayer(player, bus)
                if player_name.lower() in str(media_player.root.Identity).lower():
                    if media_player.player.Volume == 0:
                        media_player.player.Volume = player_volumes[media_player.root.Identity]
                    else:
                        player_volumes[media_player.root.Identity] = media_player.player.Volume
                        media_player.player.Volume = 0
        else:
            for player in player_ids:
                media_player = pympris.MediaPlayer(player, bus)
                if media_player.player.Volume == 0:
                    media_player.player.Volume = player_volumes[media_player.root.Identity]
                else:
                    player_volumes[media_player.root.Identity] = media_player.player.Volume
                    media_player.player.Volume = 0
    except PyMPRISException:
        print("WARN: Player " + player_name + " does not support interface Volume!")
