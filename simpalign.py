import sublime
import sublime_plugin
import re
import math
import os
import sys

####################################################################
# This is apparently (maybe?) necessary
#   due to load order of packages in Sublime Text 2
# See https://github.com/wbond/sublime_alignment/blob/master/Alignment.py#L8
sys.path.append(os.path.join(sublime.packages_path(), 'Default'))
indentation = __import__('indentation')
reload(indentation)
del sys.path[-1]
####################################################################

# Deals with non-space tabs, presumably...
normed_rowcol = indentation.line_and_normed_pt

class SimpalignCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view

        # Maps row -> (start_col, start)
        by_row = {}
        # Maximum starting column of all the by_row's
        max_start_col = 0

        for single in view.sel():
            # Only look at start, for now
            # TODO(gregp): would we ever want to use end?
            start = min(single.a, single.b)
            # Get the row (and column in that row)
            (row, col) = normed_rowcol(view, start)

            # Handle two selections on one row, by ignoring the second
            # TODO(gregp): align all the second/(3rd/...) selections too?
            if by_row.has_key(row):
                continue

            # Add another row to indent
            by_row[row] = (col, start)

            # Keep track of the maximum (where we will indent to)
            if col > max_start_col:
                max_start_col = col

        # Need to take the last row first, since otherwise the position number
        #   of the single selection starts will change during the edit.
        tasks = by_row.items()
        tasks.sort()
        tasks.reverse()
        # For each row we care about, insert some spaces.
        for (row, (col, start)) in tasks:
            print "%s, %s, %s" % (row, col, start)
            view.insert(edit, start, ' ' * (max_start_col - col))
