import unittest


def suite():
    suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=1).run(suite)
    return suite


suite()
unittest.main()