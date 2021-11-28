import rofi
import papis.api
import papis.pick
import papis.format
import papis.config
import papis.database
from papis.commands.rm import run as rm
from papis.commands.edit import run as edit
from papis.commands.browse import run as browse
# from papis.commands.open import run as papis_open

import logging
import click
import papis_rofi
import papis_rofi.config

logger = logging.getLogger("rofi")
papis_rofi.config.register_default_settings()


def papis_open(document):
    files_to_open = document.get_files()
    for f in files_to_open:
        papis.api.open_file(f, wait=False)


def get_options():
    options = dict()

    for key in ["fullscreen", "normal_window", "multi_select",
                "case_sensitive", "markup_rows"]:
        options[key] = papis.config.getboolean(key, section="rofi-gui")

    for key in ["width", "eh", "lines", "fixed_lines"]:
        options[key] = papis.config.getint(key, section="rofi-gui")

    for key in ["sep", "theme"]:
        options[key] = papis.config.get(key, section="rofi-gui")

    return options


def pick(options):

    papis_rofi.config.register_default_settings()

    if len(options) == 1:
        return options
    elif len(options) == 0:
        return []
    else:
        return Gui().main(options)


class Picker(papis.pick.Picker):

    def __call__(self,
                 items,
                 header_filter,
                 match_filter,
                 default_index: int = 0):
        return pick(items)


class Gui(object):

    esc_key = -1
    open_key = 0
    quit_key = 1
    edit_key = 2
    delete_key = 3
    help_key = 4
    open_stay_key = 5
    normal_window_key = 6
    browse_key = 7
    query_key = 8
    refresh_key = 9

    def __init__(self, documents=[]):
        # Set default picker
        self.db = papis.database.get()
        self.documents = []
        self.help_message = ""
        self.keys = self.get_keys()
        self.window = None

    def get_help(self):
        space = " "*10
        message = "Rofi based gui for papis\n"
        message += "========================\n"
        for k in self.keys:
            message += "%s%s%s\n" % (self.keys[k][0], space, self.keys[k][1])
        return message

    def get_key(self, key):
        return papis.config.get("key-" + key.lower(), section="rofi-gui")

    def get_keys(self):
        return {
            "key%s" % self.query_key: (
                self.get_key('query'),
                'Query'
            ),
            "key%s" % self.quit_key: (
                self.get_key('quit'),
                'Quit'
            ),
            "key%s" % self.edit_key: (
                self.get_key('edit'),
                'Edit'
            ),
            "key%s" % self.delete_key: (
                self.get_key('delete'),
                'Delete'
            ),
            "key%s" % self.help_key: (
                self.get_key('help'),
                'Help'
            ),
            "key%s" % self.open_stay_key: (
                self.get_key('open-stay'),
                'Open'
            ),
            "key%s" % self.normal_window_key: (
                self.get_key('normal-window'),
                'Normal Win'
            ),
            "key%s" % self.open_key: (
                self.get_key('open'),
                'Open'
            ),
            "key%s" % self.refresh_key: (
                self.get_key('refresh'),
                'Refresh'
            ),
            "key%s" % self.browse_key: (
                self.get_key('browse'),
                'Browse'
            )
        }

    def main(self, documents):
        self.query_string = ''
        self.documents = documents
        key = None
        indices = None
        options = get_options()
        header_format = papis.config.get("header-format", section="rofi-gui")

        def header_filter(x):
            return papis.format.format(header_format, x)

        self.help_message = self.get_help()
        options.update(self.keys)
        # Initialize window
        self.window = rofi.Rofi()
        while not (key == self.quit_key or key == self.esc_key):
            indices, key = self.window.select(
                "Filter: ",
                [header_filter(d) for d in self.documents],
                select=indices,
                **options
            )
            if not isinstance(indices, list):
                indices = [indices]
            if key == self.edit_key:
                for i in indices:
                    edit(self.documents[i])
            elif key in [self.open_key, self.open_stay_key]:
                docs = [self.documents[i] for i in indices]
                if key == self.open_key:
                    return docs
                elif key == self.open_stay_key:
                    for doc in docs:
                        papis_open(doc)
            elif key == self.delete_key:
                for i in indices:
                    self.delete(self.documents[i])
            elif key == self.help_key:
                self.window.error(self.help_message)
            elif key == self.browse_key:
                for i in indices:
                    browse(self.documents[i])
            elif key == self.normal_window_key:
                options["normal_window"] ^= True
            elif key == self.refresh_key:
                self.refresh()
            elif key == self.query_key:
                self.query_string = self.window.text_entry("Query input: ")
                self.set_docs_from_query()

    def delete(self, doc):
        answer = self.window.text_entry(
            "Are you sure? (y/N)",
            message="<b>Be careful!</b>"
        )
        if answer and answer in "Yy":
            rm(doc)

    def set_docs_from_query(self):
        if self.query_string:
            self.documents = self.db.query(self.query_string)

    def refresh(self):
        self.set_docs_from_query()


@click.command()
@click.argument('query', nargs=1, default='')
@click.help_option('--help', '-h')
@click.version_option(version=papis_rofi.__version__)
def main(query):
    """A rofi based GUI for papis"""
    documents = papis.database.get().query(query)
    return Gui().main(documents)


if __name__ == "__main__":
    main()
