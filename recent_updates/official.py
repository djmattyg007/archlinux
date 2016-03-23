#!/usr/bin/python3

from recent_updates_lib import *

URL = "https://www.archlinux.org/"
PKG_BASE_URL = "https://www.archlinux.org"

pkg_updates = get_pkg_updates(URL)

rows = pkg_updates.select("table tr")
new_packages = []
for row in rows:
    name, version = row.select(".pkg-name")[0].string.split(" ")
    arch_select = row.select(".pkg-arch a")
    arch = None
    if len(arch_select) == 1:
        arch = arch_select[0].string
        link = PKG_BASE_URL + arch_select[0]["href"]
    else:
        for temp_arch in arch_select:
            if temp_arch.string == "x86_64":
                arch = "x86_64"
                link = PKG_BASE_URL + temp_arch["href"]
                break
        if not arch:
            arch = arch_select[0].string
            link = PKG_BASE_URL + arch_select[0]["href"]
    new_packages.append([name, arch, version, link])

print_table(["name", "arch", "version", "link"], new_packages)
