#!/usr/bin/python3

from recent_updates_lib import *

URL = "https://aur.archlinux.org/"
PKG_BASE_URL = "https://aur.archlinux.org"

pkg_updates = get_pkg_updates(URL)

rows = pkg_updates.select("table tr")
new_packages = []
for row in rows:
    pkg_name = row.select(".pkg-name a")[0]
    name, version = pkg_name.string.split(" ")
    link = PKG_BASE_URL + pkg_name["href"]
    date = row.select(".pkg-date span")[0].string
    new_packages.append([name, version, date, link])

print_table(["name", "version", "date", "link"], new_packages)
