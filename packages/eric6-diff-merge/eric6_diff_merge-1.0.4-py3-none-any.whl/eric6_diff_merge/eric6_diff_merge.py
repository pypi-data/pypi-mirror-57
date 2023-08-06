# -*- coding: utf-8 -*-

# Copyright (c) 2004 - 2019 Detlev Offenbach <detlev@die-offenbachs.de>
#

"""
Module implementing a dialog to compare two files.
"""

import os
import time
import traceback
from difflib import SequenceMatcher


class Eric6Diff:
    """
    Class implementing a dialog to compare two files.
    """

    def __init__(self, old_file, new_file, output=""):
        """
        Constructor

        @param parent reference to the parent widget (QWidget)
        """
        self.filename1 = old_file
        self.filename2 = new_file
        self.output_name = output
        self.diff_mode = "unifited"
        # self.diff_mode = "context"

        self.tr = print
        self.contents = []

    ### save
    def on_save(self, fname):
        """
        Private slot to handle the Save button press.

        It saves the diff shown in the dialog to a file in the local
        filesystem.
        """

        try:
            f = open(fname, "w", encoding="utf-8")
            txt = self.get_str_patch()
            try:
                f.write(txt)
            except UnicodeError:
                pass
            f.close()
        except IOError as why:

            self.tr('The patch file {0} could not be saved.Reason: {1}').format(fname, str(why))

    ### diff
    def on_diff(self):
        """
        Private slot to handle the Compare button press.
        """

        try:
            filemtime1 = time.ctime(os.stat(self.filename1).st_mtime)
        except IOError as e:
            filemtime1 = ""
            print(e)
        try:
            f1 = open(self.filename1, "r", encoding="utf-8")
            lines1 = f1.readlines()
            f1.close()
        except IOError as e:

            self.tr("""The file {0} could not be read.""".format(self.filename1))

            return

        try:
            filemtime2 = time.ctime(os.stat(self.filename2).st_mtime)
        except IOError as e:
            print(e)
            filemtime2 = ""
        try:
            f2 = open(self.filename2, "r", encoding="utf-8")
            lines2 = f2.readlines()
            f2.close()
        except IOError as e:

            self.tr("""The file {0} could not be read.""".format(self.filename2))

        ####

        if self.diff_mode == "unifited":
            self.__generateUnifiedDiff(
                lines1, lines2, self.filename1, self.filename2,
                filemtime1, filemtime2)
        else:
            self.__generateContextDiff(
                lines1, lines2, self.filename1, self.filename2,
                filemtime1, filemtime2)
        ## save
        if self.output_name:
            self.on_save(self.output_name)
        return self.contents

    def get_list_contents(self) -> list:
        return self.contents

    def get_str_patch(self):

        return "".join(self.contents)

    # def get_str_contents(self):
    #     return "".join(self.contents)

    def __appendText(self, txt):
        """
        Private method to append text to the end of the contents pane.

        @param txt text to insert (string)
        """
        self.handle_appendText(txt)

    def handle_appendText(self, txt):
        self.contents.append(txt)

    def __generateUnifiedDiff(self, a, b, fromfile, tofile,
                              fromfiledate, tofiledate):
        """
        Private slot to generate a unified diff output.

        @param a first sequence of lines (list of strings)
        @param b second sequence of lines (list of strings)
        @param fromfile filename of the first file (string)
        @param tofile filename of the second file (string)
        @param fromfiledate modification time of the first file (string)
        @param tofiledate modification time of the second file (string)
        """
        paras = 0

        for line in self.unified_diff(a, b, fromfile, tofile,
                                      fromfiledate, tofiledate):
            self.__appendText(line)
            paras += 1
 
        if paras == 0:
            self.tr('There is no difference.')

    def __generateContextDiff(self, a, b, fromfile, tofile,
                              fromfiledate, tofiledate):
        """
        Private slot to generate a context diff output.

        @param a first sequence of lines (list of strings)
        @param b second sequence of lines (list of strings)
        @param fromfile filename of the first file (string)
        @param tofile filename of the second file (string)
        @param fromfiledate modification time of the first file (string)
        @param tofiledate modification time of the second file (string)
        """
        paras = 0
        for line in self.context_diff(a, b, fromfile, tofile,
                                      fromfiledate, tofiledate):
            self.__appendText(line)
            paras += 1

        if paras == 0:
            self.tr('There is no difference.')

    ############################################################## # ↓
    ##
    ############################################################## # ↑
    # This function is copied from python 2.3 and slightly modified.
    # The header lines contain a tab after the filename.

    def context_diff(self, a, b, fromfile='', tofile='',
                     fromfiledate='', tofiledate='', n=3, lineterm='\n'):
        r"""
        Compare two sequences of lines; generate the delta as a context diff.

        Context diffs are a compact way of showing line changes and a few
        lines of context.  The number of context lines is set by 'n' which
        defaults to three.

        By default, the diff control lines (those with *** or ---) are
        created with a trailing newline.  This is helpful so that inputs
        created from file.readlines() result in diffs that are suitable for
        file.writelines() since both the inputs and outputs have trailing
        newlines.

        For inputs that do not have trailing newlines, set the lineterm
        argument to "" so that the output will be uniformly newline free.

        The context diff format normally has a header for filenames and
        modification times.  Any or all of these may be specified using
        strings for 'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.
        The modification times are normally expressed in the format returned
        by time.ctime().  If not specified, the strings default to blanks.

        Example:

        <pre>
        &gt;&gt;&gt; print ''.join(
        ...       context_diff('one\ntwo\nthree\nfour\n'.splitlines(1),
        ...       'zero\none\ntree\nfour\n'.splitlines(1), 'Original', 'Current',
        ...       'Sat Jan 26 23:30:50 1991', 'Fri Jun 06 10:22:46 2003')),
        *** Original Sat Jan 26 23:30:50 1991
        --- Current Fri Jun 06 10:22:46 2003
        ***************
        *** 1,4 ****
          one
        ! two
        ! three
          four
        --- 1,4 ----
        + zero
          one
        ! tree
          four
        </pre>

        @param a first sequence of lines (list of strings)
        @param b second sequence of lines (list of strings)
        @param fromfile filename of the first file (string)
        @param tofile filename of the second file (string)
        @param fromfiledate modification time of the first file (string)
        @param tofiledate modification time of the second file (string)
        @param n number of lines of context (integer)
        @param lineterm line termination string (string)
        @return a generator yielding lines of differences
        """
        started = False
        prefixmap = {
            'insert' : '+ ',
            'delete' : '- ',
            'replace': '! ',
            'equal'  : '  '
        }
        for group in SequenceMatcher(None, a, b).get_grouped_opcodes(n):
            if not started:
                yield '*** {0}\t{1}{2}'.format(fromfile, fromfiledate, lineterm)
                yield '--- {0}\t{1}{2}'.format(tofile, tofiledate, lineterm)
                started = True

            yield '***************{0}'.format(lineterm)
            if group[-1][2] - group[0][1] >= 2:
                yield '*** {0:d},{1:d} ****{2}'.format(
                    group[0][1] + 1, group[-1][2], lineterm)
            else:
                yield '*** {0:d} ****{1}'.format(group[-1][2], lineterm)
            visiblechanges = [e for e in group if e[0] in ('replace', 'delete')]
            if visiblechanges:
                for tag, i1, i2, _, _ in group:
                    if tag != 'insert':
                        for line in a[i1:i2]:
                            yield prefixmap[tag] + line

            if group[-1][4] - group[0][3] >= 2:
                yield '--- {0:d},{1:d} ----{2}'.format(
                    group[0][3] + 1, group[-1][4], lineterm)
            else:
                yield '--- {0:d} ----{1}'.format(group[-1][4], lineterm)
            visiblechanges = [e for e in group if e[0] in ('replace', 'insert')]
            if visiblechanges:
                for tag, _, _, j1, j2 in group:
                    if tag != 'delete':
                        for line in b[j1:j2]:
                            yield prefixmap[tag] + line

    # This function is copied from python 2.3 and slightly modified.
    # The header lines contain a tab after the filename.

    def unified_diff(self, a, b, fromfile='', tofile='', fromfiledate='',
                     tofiledate='', n=3, lineterm='\n'):
        """
        Compare two sequences of lines; generate the delta as a unified diff.

        Unified diffs are a compact way of showing line changes and a few
        lines of context.  The number of context lines is set by 'n' which
        defaults to three.

        By default, the diff control lines (those with ---, +++, or @@) are
        created with a trailing newline.  This is helpful so that inputs
        created from file.readlines() result in diffs that are suitable for
        file.writelines() since both the inputs and outputs have trailing
        newlines.

        For inputs that do not have trailing newlines, set the lineterm
        argument to "" so that the output will be uniformly newline free.

        The unidiff format normally has a header for filenames and modification
        times.  Any or all of these may be specified using strings for
        'fromfile', 'tofile', 'fromfiledate', and 'tofiledate'.  The modification
        times are normally expressed in the format returned by time.ctime().

        Example:

        <pre>
        &gt;&gt;&gt; for line in unified_diff('one two three four'.split(),
        ...             'zero one tree four'.split(), 'Original', 'Current',
        ...             'Sat Jan 26 23:30:50 1991', 'Fri Jun 06 10:20:52 2003',
        ...             lineterm=''):
        ...     print line
        --- Original Sat Jan 26 23:30:50 1991
        +++ Current Fri Jun 06 10:20:52 2003
        @@ -1,4 +1,4 @@
        +zero
         one
        -two
        -three
        +tree
         four
        </pre>

        @param a first sequence of lines (list of strings)
        @param b second sequence of lines (list of strings)
        @param fromfile filename of the first file (string)
        @param tofile filename of the second file (string)
        @param fromfiledate modification time of the first file (string)
        @param tofiledate modification time of the second file (string)
        @param n number of lines of context (integer)
        @param lineterm line termination string (string)
        @return a generator yielding lines of differences
        """
        started = False
        for group in SequenceMatcher(None, a, b).get_grouped_opcodes(n):
            if not started:
                yield '--- {0}\t{1}{2}'.format(fromfile, fromfiledate, lineterm)
                yield '+++ {0}\t{1}{2}'.format(tofile, tofiledate, lineterm)
                started = True
            i1 = group[0][1]  # a's first line number.
            i2 = group[-1][2]  # a's end   line number.
            j1 = group[0][3]  # b's first line number.
            j2 = group[-1][4]  # b's end   line number.
            yield "@@ -{0:d},{1:d} +{2:d},{3:d} @@{4}".format(
                i1 + 1, i2 - i1, j1 + 1, j2 - j1, lineterm)

            for tag, i1, i2, j1, j2 in group:
                if tag == 'equal':
                    for line in a[i1:i2]:
                        yield ' ' + line
                    continue
                if tag == 'replace' or tag == 'delete':
                    for line in a[i1:i2]:
                        yield '-' + line
                if tag == 'replace' or tag == 'insert':
                    for line in b[j1:j2]:
                        yield '+' + line
