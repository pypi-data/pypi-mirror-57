from gi import require_version
require_version('GtkSource', '3.0')     # noqa
require_version('Pango', '1.0')         # noqa
require_version('GtkSpell', '3.0')      # noqa

from gi.repository.Pango import FontDescription
from gi.repository.GtkSource import LanguageManager, Buffer, View, \
    DrawSpacesFlags, SearchContext, SearchSettings
from gi.repository.GLib import get_home_dir, timeout_add_seconds, Variant, \
    idle_add, timeout_add
from gi.repository.GtkSpell import Checker

from gi.repository import GObject
from gi.repository import Gtk

from os import rename, stat, fstat
from os.path import splitext, basename, isfile, exists
from io import open
from traceback import format_exc
from sys import version_info, stderr

from formiko.dialogs import FileSaveDialog, TraceBackDialog, FileChangedDialog
from formiko.widgets import ActionHelper

default_manager = LanguageManager.get_default()
LANGS = {
    '.rst': default_manager.get_language('rst'),
    '.md': default_manager.get_language('markdown'),
    '.html': default_manager.get_language('html'),
    '.htm': default_manager.get_language('html'),
    '.json': default_manager.get_language('json')
}
PERIOD_SAVE_TIME = 300      # 5min


class SourceView(Gtk.ScrolledWindow, ActionHelper):
    __file_name = ''
    __last_changes = 0
    __last_ctime = 0
    __skip_period = 0

    __gsignals__ = {
        'file-type': (GObject.SIGNAL_RUN_FIRST, None, (str,)),
        'scroll-changed': (GObject.SIGNAL_RUN_LAST, None, (float,))
    }

    action_name = GObject.property(type=str)
    action_target = GObject.property(type=GObject.TYPE_VARIANT)

    def __init__(self, win, preferences, action_name=None):
        super(SourceView, self).__init__()
        if action_name:
            self.action_name = action_name

        self.set_hexpand(True)
        self.set_vexpand(True)
        self.text_buffer = Buffer.new_with_language(
            LANGS['.%s' % preferences.parser])
        self.text_buffer.connect("changed", self.inc_changes)
        # TODO: will work when FileSaver and FileLoader will be used
        # self.text_buffer.set_implicit_trailing_newline(False)
        self.source_view = View.new_with_buffer(self.text_buffer)

        adj = self.get_vadjustment()
        adj.connect("value-changed", self.on_scroll_changed)

        self.spellchecker = Checker()
        self.spellchecker.connect("language-changed", self.on_language_changed)

        self.source_view.override_font(
            FontDescription.from_string('Monospace'))
        # self.source_view.set_monospace(True) since 3.16
        self.add(self.source_view)

        editor_pref = preferences.editor
        self.set_period_save(editor_pref.period_save)
        self.set_check_spelling(editor_pref.check_spelling,
                                editor_pref.spell_lang)
        self.set_spaces_instead_of_tabs(editor_pref.spaces_instead_of_tabs)
        self.source_view.set_tab_width(editor_pref.tab_width)
        self.source_view.set_auto_indent(editor_pref.auto_indent)
        self.source_view.set_show_line_numbers(editor_pref.line_numbers)
        self.source_view.set_show_right_margin(editor_pref.right_margin)
        self.source_view.set_highlight_current_line(editor_pref.current_line)
        self.set_text_wrapping(editor_pref.text_wrapping)
        self.set_white_chars(editor_pref.white_chars)

        self.search_settings = SearchSettings(wrap_around=True)
        self.search_context = SearchContext.new(
            self.text_buffer, self.search_settings)
        self.search_iter = None

        self.__win = win
        timeout_add(200, self.check_in_thread)

    @property
    def changes(self):
        return self.__last_changes

    @property
    def is_modified(self):
        return self.text_buffer.get_modified()

    @property
    def text(self):
        return self.text_buffer.get_text(self.text_buffer.get_start_iter(),
                                         self.text_buffer.get_end_iter(),
                                         True)

    @property
    def position(self):
        adj = self.source_view.get_vadjustment()
        hight = self.get_allocated_height()
        value = adj.get_value()
        if value:
            return adj.get_value()/(adj.get_upper()-hight)
        return 0

    @property
    def file_name(self):
        return basename(self.__file_name)

    @property
    def file_path(self):
        return self.__file_name

    @property
    def file_ext(self):
        name, ext = splitext(self.__file_name)
        return ext

    def inc_changes(self, text_buffer):
        self.__last_changes += 1

    def on_language_changed(self, spellchecker, language):
        action, go = self.get_action_owner()
        if go:
            action_target = Variant("s", language)
            go.activate_action(action, action_target)

    def on_scroll_changed(self, *params):
        self.emit("scroll-changed", self.position)

    def set_period_save(self, save):
        self.period_save = bool(save)*PERIOD_SAVE_TIME
        if save:
            self.period_save_thread()

    def set_check_spelling(self, check_spelling, spell_lang):
        if check_spelling:
            if spell_lang in Checker.get_language_list():
                self.spellchecker.set_language(spell_lang)
            else:
                # refresh from temporary off check spelling
                self.on_language_changed(self.spellchecker,
                                         self.spellchecker.get_language())
            self.spellchecker.attach(self.source_view)
        else:
            self.spellchecker.detach()
            self.on_language_changed(self.spellchecker, "")

    def set_spaces_instead_of_tabs(self, use_spaces):
        self.source_view.set_insert_spaces_instead_of_tabs(use_spaces)
        self.source_view.set_smart_backspace(use_spaces)

    def set_text_wrapping(self, text_wrapping):
        if text_wrapping:
            self.source_view.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
        else:
            self.source_view.set_wrap_mode(Gtk.WrapMode.NONE)

    def set_white_chars(self, white_chars):
        if white_chars:
            self.source_view.set_draw_spaces(DrawSpacesFlags.ALL)
        else:
            self.source_view.set_draw_spaces(0)

    def check_in_thread(self):
        """This function is called from GLib.timeout_add"""
        if not self.__file_name:
            return
        try:
            last_ctime = stat(self.__file_name).st_ctime
            if last_ctime > self.__last_ctime:
                self.__skip_period = True
                dialog = FileChangedDialog(self.__win, self.__file_name)
                if dialog.run() == Gtk.ResponseType.YES:
                    cursor = self.text_buffer.get_insert()
                    offset = self.text_buffer.get_iter_at_mark(
                        cursor).get_offset()

                    self.read_from_file(self.__file_name, offset)

                dialog.destroy()
                self.__skip_period = False
        except OSError:
            pass        # file switching when modify by another software
        timeout_add(200, self.check_in_thread)

    def period_save_thread(self):
        if self.period_save:
            if self.__file_name and self.is_modified \
                    and not self.__skip_period:
                idle_add(self.save_to_file)
            timeout_add_seconds(self.period_save, self.period_save_thread)

    def read_from_file(self, file_name, offset=0):
        self.__file_name = file_name
        self.emit("file_type", self.file_ext)

        if isfile(file_name):
            with open(file_name, 'r', encoding="utf-8") as src:
                self.text_buffer.set_text(src.read())
                self.__last_changes += 1
                self.__last_ctime = fstat(src.fileno()).st_ctime

        self.text_buffer.set_modified(False)
        if offset > -1:
            cursor = self.text_buffer.get_iter_at_offset(offset)
            self.text_buffer.place_cursor(cursor)
            idle_add(self.scroll_to_cursor, cursor)

    def scroll_to_cursor(self, cursor):
        self.source_view.scroll_to_iter(cursor, 0, 1, 1, 1)

    def save_to_file(self):
        try:
            if exists(self.__file_name):
                rename(self.__file_name, "%s~" % self.__file_name)
            with open(self.__file_name, 'w', encoding="utf-8") as src:
                if version_info.major == 2:
                    src.write(self.text.decode('utf-8'))
                else:   # python version 3.x
                    src.write(self.text)
                self.__last_ctime = fstat(src.fileno()).st_ctime
            self.text_buffer.set_modified(False)
        except Exception:
            error = format_exc()
            if self.__win:
                md = TraceBackDialog(self.__win, error)
                md.run()
                md.destroy()
            stderr.write(error)
            stderr.flush()

    def save(self):
        if not self.__file_name:
            self.__file_name = self.get_new_file_name()
            self.emit("file_type", self.file_ext)
        if self.__file_name:
            self.save_to_file()

    def save_as(self):
        new_file_name = self.get_new_file_name()
        if new_file_name:
            self.__file_name = new_file_name
            self.emit("file_type", self.file_ext)
            self.save_to_file()

    def get_new_file_name(self):
        ret_val = ''
        dialog = FileSaveDialog(self.__win)
        # TODO: set default filtry by select parser
        dialog.add_filter_rst()
        dialog.add_filter_md()
        dialog.add_filter_html()
        dialog.set_do_overwrite_confirmation(True)

        if not self.__file_name:
            dialog.set_current_folder(get_home_dir())

        if dialog.run() == Gtk.ResponseType.ACCEPT:
            ret_val = dialog.get_filename()
        dialog.destroy()
        return ret_val

    def do_file_type(self, ext):
        language = LANGS.get(ext, LANGS['.rst'])
        if self.text_buffer.get_language() != language:
            self.text_buffer.set_language(language)

    def do_next_match(self, text):
        if self.search_settings.get_search_text() != text:
            self.search_settings.set_search_text(text)
            self.search_iter = self.text_buffer.get_iter_at_mark(
                self.text_buffer.get_insert())
        elif self.search_iter:
            self.search_iter.forward_char()
        else:
            return False

        found, self.search_iter, end = self.search_context.forward(
            self.search_iter)

        if not found:
            self.search_iter = None
            return False
        self.source_view.scroll_to_iter(self.search_iter, 0, 1, 1, 1)
        self.text_buffer.place_cursor(self.search_iter)
        return True

    def do_previous_match(self, text):
        if self.search_settings.get_search_text() != text:
            self.search_settings.set_search_text(text)
            self.search_iter = self.text_buffer.get_iter_at_mark(
                self.text_buffer.get_insert())
        elif not self.search_iter:
            return False

        found, start, self.search_iter = self.search_context.backward(
            self.search_iter)
        if not found:
            self.search_iter = None
            return False
        self.search_iter.backward_chars(len(text))
        self.source_view.scroll_to_iter(self.search_iter, 0, 1, 1, 1)
        self.text_buffer.place_cursor(self.search_iter)
        return True

    def stop_search(self):
        self.search_settings.set_search_text(None)
