#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `mlbench_core.utils.pytorch.helpers` package."""

import pytest

from mlbench_core.utils import Tracker
from mlbench_core.evaluation.pytorch.metrics import TopKAccuracy
from mlbench_core.evaluation.goals import task1_time_to_accuracy_light_goal


def test_tracker():
    tracker = Tracker([TopKAccuracy(5)], 1, 0)

    assert tracker is not None


def test_tracker_goal(mocker):
    patched = mocker.patch('mlbench_core.utils.tracker.LogMetrics')

    metric = TopKAccuracy(1)
    tracker = Tracker([metric], 1, 0, task1_time_to_accuracy_light_goal)

    assert tracker is not None

    tracker.start()

    assert tracker.start_time is not None

    tracker.train()

    tracker.record_stat('global_Prec@1', 69, log_to_api=True)
    tracker.batch_end()

    assert not tracker.goal_reached

    tracker.record_stat('global_Prec@1', 70, log_to_api=True)
    tracker.batch_end()


    assert not tracker.goal_reached

    tracker.validation()

    tracker.record_stat('global_Prec@1', 69, log_to_api=True)
    tracker.batch_end()

    assert not tracker.goal_reached

    tracker.record_stat('global_Prec@1', 70, log_to_api=True)

    assert tracker.goal_reached
