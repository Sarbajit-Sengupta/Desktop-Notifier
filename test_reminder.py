import argparse
import unittest
from unittest.mock import Mock
from main import positive_interval, run


class ReminderTests(unittest.TestCase):
    def test_interval_validation(self):
        for value in ('0', '-1', 'nan', 'inf'):
            with self.assertRaises(argparse.ArgumentTypeError):
                positive_interval(value)
        self.assertEqual(positive_interval('3600'), 3600)

    def test_reminder_waits_and_stops_cleanly(self):
        notify = Mock()
        sleep = Mock(side_effect=KeyboardInterrupt)
        run(3600, notify, sleep)
        notify.assert_called_once()
        sleep.assert_called_once_with(3600)


if __name__ == '__main__':
    unittest.main()
