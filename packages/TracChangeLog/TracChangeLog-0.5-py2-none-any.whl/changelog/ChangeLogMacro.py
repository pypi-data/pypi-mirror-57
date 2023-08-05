# -*- coding: utf-8 -*-
#
# Copyright (C) 2006-2008 Alec Thomas
# Copyright (C) 2010-2015 Ryan J Ollos <ryan.j.ollos@gmail.com>
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.
#

import re
from StringIO import StringIO

from trac.util.datefmt import format_datetime
from trac.util.html import Markup, html
from trac.util.translation import _
from trac.versioncontrol.api import NoSuchNode, RepositoryManager
from trac.web.chrome import web_context
from trac.wiki.formatter import format_to_html, format_to_oneliner, \
    system_message
from trac.wiki.macros import WikiMacroBase, parse_args


class ChangeLogMacro(WikiMacroBase):
    """Write repository change log to output.

    The !ChangeLog macro writes a log of the last changes of a repository at a
    given path. Following variants are possible to use:
    {{{
    1. [[ChangeLog(/path)]]
    2. [[ChangeLog(/path@rev)]]
    3. [[ChangeLog(/path@rev, limit)]]
    4. [[ChangeLog(/path@from-to)]]
    5. [[ChangeLog(/path, limit, rev)]]
    }}}

    1. Default repository is used if reponame is left out. To show the last
       five changes of the default repository:
       {{{
       [[ChangeLog(/)]]
       }}}
       To show the last five changes of the trunk folder in a named otherrepo:
       {{{
       [[ChangeLog(/otherrepo/trunk)]]
       }}}
    2. The ending revision can be set.
       To show the last five changes up to revision 99:
       {{{
       [[ChangeLog(/otherrepo/trunk@99)]]
       }}}
    3. The limit can be set by an optional parameter. To show the last
       10 changes, up to revision 99:
       {{{
       [[ChangeLog(/otherrepo/trunk@99, 10)]]
       }}}
    4. A range of revisions can be logged.
       {{{
       [[ChangeLog(/otherrepo/trunk@90-99)]]
       }}}
       To lists all changes:
       {{{
       [[ChangeLog(/otherrepo/trunk@1-HEAD)]]
       }}}
       HEAD can be left out:
       {{{
       [[ChangeLog(/otherrepo/trunk@1-)]]
       }}}
    5. For backwards compatibility, revision can be stated as a third
       parameter:
       {{{
       [[ChangeLog(/otherrepo/trunk, 10, 99)]]
       }}}

    limit and rev may be keyword arguments.
    {{{
    [[ChangeLog(/otherrepo/trunk, limit=10, rev=99)]]
    }}}
    """

    def expand_macro(self, formatter, name, content):
        req = formatter.req

        if 'CHANGESET_VIEW' not in req.perm:
            return Markup('<i>Changelog not available</i>')

        context = web_context(req)
        args, kwargs = parse_args(content)
        if len(args) == 0:
            return system_message(_("ChangeLog macro error"),
                                  _("Repository path is required."))
        args += [None, None]
        raw_path, limit, rev = args[:3]
        limit = kwargs.pop('limit', limit)
        rev = kwargs.pop('rev', rev)
        if '@' in raw_path:
            raw_path, rev = raw_path.split('@', 2)
        if ':' in raw_path:  # Compatibility with version 0.4
            abs_path = '/'.join(raw_path.split(':', 2))
        else:
            abs_path = raw_path
        reponame, repo, path = \
            RepositoryManager(self.env).get_repository_by_path(abs_path)
        log_href = req.href.log(abs_path, rev=rev)
        path = repo.normalize_path(path)
        revstart = 0
        if rev is not None:
            for d in [':', '-']:
                if d in rev:
                    revstart, revstop = rev.split(d, 2)
                    if not revstop or revstop.lower() in ['head', '0']:
                        revstart = int(revstart)
                        rev = repo.get_youngest_rev()
                        limit = rev - revstart + 1
                    else:
                        revstart, revstop = int(revstart), int(revstop)
                        if revstart > revstop:
                            revstart, revstop = revstop, revstart
                        limit = revstop - revstart + 1
                        rev = revstop or None
                    break

        if rev is None:
            rev = repo.get_youngest_rev()
        rev = repo.normalize_rev(rev)
        if limit is None:
            limit = 5
        else:
            limit = int(limit)
        try:
            node = repo.get_node(path, rev)
        except NoSuchNode, e:
            return system_message(_("ChangeLog macro failed"), e)
        out = StringIO()
        out.write('</p>')  # close surrounding paragraph
        out.write('\n<div class="changelog">\n<dl class="wiki">')
        for npath, nrev, nlog in node.get_history(limit):
            if nrev < revstart:
                break
            change = repo.get_changeset(nrev)
            datetime = format_datetime(change.date, '%Y-%m-%d %H:%M:%S',
                                       req.tz)
            drev = repo.display_rev(nrev)
            if not reponame:
                sargs = nrev, drev
            else:
                sargs = '%s/%s' % (nrev, reponame), '%s/%s' % (drev, reponame)
            cset = '[changeset:%s %s]' % sargs
            header = format_to_oneliner(
                self.env, context,
                "%s by %s on %s" % (cset, change.author, datetime))
            out.write('\n<dt id="changelog-changeset-%s">\n%s\n</dt>' %
                      (cset, header))
            message = _remove_p(format_to_html(
                self.env, context, change.message, escape_newlines=True))
            out.write('\n<dd>\n%s\n</dd>' % message)
        out.write(html.small(html.a(_("(more)"), href=log_href)))
        out.write('\n</dl>\n</div>')
        out.write('\n<p>')  # re-open surrounding paragraph
        return out.getvalue()


REMOVE_P = '^\s*<p>(.*?)</p>\s*$'
REMOVE_P_RE = re.compile(REMOVE_P, re.DOTALL)


def _remove_p(html):
    f = REMOVE_P_RE.findall(html)
    if f:
        return f[0]
    else:
        return html
