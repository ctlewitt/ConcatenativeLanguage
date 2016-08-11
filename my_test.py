import unittest

if __name__ == "__main__":
    suite = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=1, buffer=True).run(suite)


#unittest.main(module=__name__, buffer=True, exit=False)