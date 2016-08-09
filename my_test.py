import unittest


def suite():
    suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=1, buffer=True).run(suite)
#    return suite


suite()
#unittest.main(module=__name__, buffer=True, exit=False)