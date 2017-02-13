import re

from sublime import Region
import sublime_plugin


REPLACEMENTS = {
    '\u00a0': ' ', # no-break space
    '\u200b': '', # zero-width space
}


class UnicodeTrapsListener(sublime_plugin.EventListener):
    @staticmethod
    def on_pre_save(view):
        view.run_command('unicode_traps')


class UnicodeTraps(sublime_plugin.TextCommand):
    def run(self, edit):
        all_file = self.view.substr(Region(0, self.view.size()))

        matches = list(re.finditer('[%s]' % ''.join(REPLACEMENTS), all_file))

        for match in reversed(matches):
            self.view.replace(edit, Region(*match.span()), REPLACEMENTS[match.group()])
