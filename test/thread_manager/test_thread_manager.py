from unittest import TestCase

from thread_manager.thread_manager import ThreadManager


class ThreadManagerTest(TestCase):

    def test_run(self):
        ThreadManager.run(function=lambda x: x + 1, kwargs={'x':1},
                          success_handler=lambda x: self.assertEqual(x, 2)
                          )

    def test_when_exception_raises(self):
        def raise_error():
            raise ValueError('you wrong')
        ThreadManager.run(
            function=raise_error,
            fail_handler=lambda e: self.assertIsInstance(e, ValueError)
        )

    def test_run_after(self):
        ThreadManager.run_after(1, function=lambda x: x + 1, kwargs={'x':1},
                          success_handler=lambda x: self.assertEqual(x, 2)
                          )
