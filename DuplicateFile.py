import sublime_plugin
import os, time, shutil


class DuplicateFile(sublime_plugin.ApplicationCommand):
    def run(self, paths):
        file_ = paths[0]
        file_name, file_ext = os.path.splitext(file_)
        copy = "%s_%d%s" % (file_name, int(time.time()), file_ext)
        shutil.copy2(file_, copy)

    def is_visible(self, paths):
        return os.path.isfile(paths[0])
