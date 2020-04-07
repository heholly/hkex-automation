from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from TestScript.DashBoard.TestClientPortal import TestClientPortal


example_tests = TestLoader().loadTestsFromTestCase(TestClientPortal)

suite = TestSuite([example_tests])
kwargs = {
    "output": "TestReport",
    "report_name": "TrialTestReport",
    "failfast": False
}
runner = HTMLTestRunner(**kwargs)
runner.run(suite)
