#!/usr/bin/env python3
# Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

from cmk.graphing.v1 import metrics, Title

metric_disk_io_utilization = metrics.Metric(
    name="cisco_sma_files_and_sockets",
    title=Title("Open files and sockets"),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=metrics.Color.ORANGE,
)
