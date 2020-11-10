#############################################################################
# -*- coding: UTF-8 -*-
#
# Copyright (c) 2020 BalaSys IT Ltd, Budapest, Hungary
#
# Authors: Szilárd Pfeiffer <szilard.pfeiffer@balabit.com>
#
# Permission is granted to copy, distribute and/or modify this document
# under the terms of the GNU Free Documentation License, Version 1.3
# or any later version published by the Free Software Foundation;
# with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
# A copy of the license is included in the section entitled "GNU
# Free Documentation License".
#
#############################################################################


Zone(
    name="clients",
    addrs=["172.16.10.0/23", ],
)


Zone(
    name="servers",
    addrs=["172.16.20.0/23", ],
)


Zone(
    name="servers.audit",
    addrs=["172.16.21.1/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.stack_clamav",
    addrs=["172.16.21.5/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.smtp_starttls",
    addrs=["172.16.21.9/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.smtp_one_sided_ssl",
    addrs=["172.16.21.13/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.http_stack_cat",
    addrs=["172.16.21.17/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.http_stack_tr",
    addrs=["172.16.21.21/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.http_header_replace",
    addrs=["172.16.21.25/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.http_url_filter",
    addrs=["172.16.21.29/32", ],
    admin_parent="servers"
)


Zone(
    name="servers.plug",
    addrs=["172.16.21.33/32", ],
    admin_parent="servers"
)

