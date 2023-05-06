# El Decko MPRIS-Backend
An El Decko backend to control media applications via the MPRIS2 dbus interface.

## First run

Upon running El Decko the first time with this backend installed it will create an empty default config to connect to
your local OBS Studio instance at: `$XDG_CONFIG/eldecko/backend/mpris.json`.  
Please update the generated default credentials with the actual port and password of what is shown inside your OBS
Studio Websocket Settings.

## Use this backend

In order to use this backend you need to supply the `streamdeck.json` generated
by [El Decko Core](https://github.com/Z-Ray-Entertainment/el_decko_core) with the following `key_config`:

```
{
    "STREAM_DECK_SERIAL_NUMBER": {
        "brightness": 30,
        "key_config": {
            "0": {
            "backend": "edb_mpris",
            "event": "PLAY",
            "event_parameters": {},
            "image_idle": null,
            "image_pressed": null
            }
        }
    }
}
```

This will configure the very first key (`0`) to use this plugin (`edb_mpris`) and bind the event `PLAY` to it.
If the `event_parameters` are kept empty the respective MPRIS event will itterate over all available MPRIS2 compatible 
clients and trigger the respective event.  

### Supported MPRIS controls

- None

## Requirements
### Python
Python >= 3.8
pympris
xdg