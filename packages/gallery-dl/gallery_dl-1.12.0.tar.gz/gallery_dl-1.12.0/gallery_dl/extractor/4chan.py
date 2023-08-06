# -*- coding: utf-8 -*-

# Copyright 2015-2019 Mike Fährmann
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

"""Extractors for https://www.4chan.org/"""

from .common import Extractor, Message
from .. import text


class _4chanThreadExtractor(Extractor):
    """Extractor for 4chan threads"""
    category = "4chan"
    subcategory = "thread"
    directory_fmt = ("{category}", "{board}", "{thread} {title}")
    filename_fmt = "{tim} {filename}.{extension}"
    archive_fmt = "{board}_{thread}_{tim}"
    pattern = (r"(?:https?://)?boards\.4chan(?:nel)?\.org"
               r"/([^/]+)/thread/(\d+)")
    test = (
        ("https://boards.4chan.org/tg/thread/15396072/", {
            "url": "39082ad166161966d7ba8e37f2173a824eb540f0",
            "keyword": "7ae2f4049adf0d2f835eb91b6b26b7f4ec882e0a",
            "content": "20b7b51afa51c9c31a0020a0737b889532c8d7ec",
        }),
        ("https://boards.4channel.org/tg/thread/15396072/", {
            "url": "39082ad166161966d7ba8e37f2173a824eb540f0",
            "keyword": "7ae2f4049adf0d2f835eb91b6b26b7f4ec882e0a",
        }),
    )

    def __init__(self, match):
        Extractor.__init__(self, match)
        self.board, self.thread = match.groups()

    def items(self):
        url = "https://a.4cdn.org/{}/thread/{}.json".format(
            self.board, self.thread)
        posts = self.request(url).json()["posts"]
        title = posts[0].get("sub") or text.remove_html(posts[0]["com"])

        data = {
            "board" : self.board,
            "thread": self.thread,
            "title" : text.unescape(title)[:50],
        }

        yield Message.Version, 1
        yield Message.Directory, data
        for post in posts:
            if "filename" in post:
                post.update(data)
                post["extension"] = post["ext"][1:]
                post["filename"] = text.unescape(post["filename"])
                url = "https://i.4cdn.org/{}/{}{}".format(
                    post["board"], post["tim"], post["ext"])
                yield Message.Url, url, post
