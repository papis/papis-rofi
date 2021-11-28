"""
Rofi gui
********
.. papis-config:: key-quit
    :section: rofi-gui

.. papis-config:: key-query
    :section: rofi-gui

.. papis-config:: key-refresh
    :section: rofi-gui

.. papis-config:: key-edit
    :section: rofi-gui

.. papis-config:: key-delete
    :section: rofi-gui

.. papis-config:: key-help
    :section: rofi-gui

.. papis-config:: key-open-stay
    :section: rofi-gui

.. papis-config:: key-normal-window
    :section: rofi-gui

.. papis-config:: key-browse
    :section: rofi-gui

.. papis-config:: key-open
    :section: rofi-gui

.. papis-config:: eh
    :section: rofi-gui

.. papis-config:: sep
    :section: rofi-gui

.. papis-config:: theme
    :section: rofi-gui

.. papis-config:: width
    :section: rofi-gui

.. papis-config:: lines
    :section: rofi-gui

.. papis-config:: fullscreen
    :section: rofi-gui

.. papis-config:: normal_window
    :section: rofi-gui

.. papis-config:: fixed_lines
    :section: rofi-gui

.. papis-config:: markup_rows
    :section: rofi-gui

.. papis-config:: multi_select
    :section: rofi-gui

.. papis-config:: case_sensitive
    :section: rofi-gui

.. papis-config:: header-format
    :section: rofi-gui

"""

import papis.config

configuration_settings = {
    "rofi-gui": {
        "key-quit": "Alt+q",
        "key-query": "Alt+y",
        "key-refresh": "Alt+r",
        "key-edit": "Alt+e",
        "key-delete": "Alt+d",
        "key-help": "Alt+h",
        "key-open-stay": "Alt+o",
        "key-normal-window": "Alt+w",
        "key-browse": "Alt+u",
        "key-open": "Enter",
        "eh": 3,
        "sep": "|",
        "width": 80,
        "lines": 10,
        "fullscreen": False,
        "normal_window": False,
        "fixed_lines": 20,
        "theme": None,
        "markup_rows": True,
        "multi_select": True,
        "case_sensitive": False,
        "header-format":
            "<b>{doc[title]}</b>\n"
            "{doc[empty]}  <i>{doc[author]}</i>\n"
            "{doc[empty]}  <span foreground=\"red\">"
            "({doc[year]:->4})</span>"
            "<span foreground=\"green\">{doc[tags]}</span>",
    },
}


def register_default_settings():
    papis.config.register_default_settings(configuration_settings)
