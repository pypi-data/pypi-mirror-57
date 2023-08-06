from smartregex import SmartRegex
import unittest

class RegexTestCase(unittest.TestCase):
    def setUp(self):
        return ""

class TestLinks(RegexTestCase):
    def test_link(self):
        valid = ["def.abc.com", "www.abc.com", "http://www.abc.com", "abc.com", "www.abc.com/jaksfkjsf"]
        non_valid = ["www.abc.def"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("links"), [v])
        for v in non_valid:
            interpreter = SmartRegex(v)
            self.assertNotEqual(interpreter.has("links"), [v])

class TestEmails(RegexTestCase):
    def test_email(self):
        valid = ["name@abc.com", "name.name@abc.com", "name_name@abc.com"]
        non_valid = ["name.name@abc....con"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("emails"), [v])
        for v in non_valid:
            interpreter = SmartRegex(v)
            self.assertNotEqual(interpreter.has("emails"), [v])

class TestDates(RegexTestCase):
    def test_date(self):
        valid = ["10-20-30", "10.20.30", "1.20.30", "01.20.30", '1.2/20', '30/06/2010', "January 1st, 2000", "Jan. 1st, 2000", "Jan 1 2000", "1 Jan 2000"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("dates"), [v])

class TestTimes(RegexTestCase):
    def test_time(self):
        valid = ["12:00", "2:00", "12:34", "12:34am", "12:00 A.M.", "12:00 pm", "12:00 P.M."]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("times"), [v])

class TestIP(RegexTestCase):
    def test_ip(self):
        valid = ["1.2.3.4"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("ips"), [v])

class TestIPv6(RegexTestCase):
    def test_ipv6(self):
        valid = ["fe80:0000:0000:0000:0000:0000:0000:0000", "::1"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("ipv6s"), [v])

class TestPhone(RegexTestCase):
    def test_phone(self):
        valid = ["12345678900", "1234567890", "+1 234 567 8900", "(123) 456 7890", 
                    "+41 22 730 5989", "(+41) 22 730 5989", "+442345678900"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("phone"), [v])

class TestZipCodes(RegexTestCase):
    def test_zip(self):
        valid = ["02111"]
        non_valid = ["1 my looper", "111111"]

        for v in valid:
            interpreter = SmartRegex(v)
            self.assertTrue(interpreter.has("zip"), [v])
        for v in non_valid:
            interpreter = SmartRegex(v)
            self.assertFalse(interpreter.has("zip"), [v])

class TestAmount(RegexTestCase):
    def test_amount(self):
        valid = ["$1", "$1.00", "$1,000,000"]
        non_valid = ["$1.", "$1.000", "$1,000.000"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("amount"), [v])
        for v in non_valid:
            interpreter = SmartRegex(v)
            self.assertNotEqual(interpreter.has("amount"), [v])

class TestStreet(RegexTestCase):
    def test_street(self):
        valid = ["my new address at 1 main st.", "1 main st", "2 your avenue"]
        non_valid = ["1 main laner"]

        for v in valid:
            interpreter = SmartRegex(v)
            self.assertTrue(interpreter.has("street"), [v])
        for v in non_valid:
            interpreter = SmartRegex(v)
            self.assertFalse(interpreter.has("street"), [v])

class TestHexColors(RegexTestCase):
    def test_hex_color(self):
        valid = ["#fff", "#ffffff"]
        for v in valid:
            interpreter = SmartRegex(v)
            self.assertEqual(interpreter.has("hex_colors"), [v])

if __name__ == '__main__':
    test_cases = [c for each_type, c in list(locals().items()) if each_type.startswith('Test')]
    cases = []
    for type in test_cases:
        cases.append(unittest.TestLoader().loadTestsFromTestCase(type))

    unittest.TextTestRunner(verbosity=10).run(unittest.TestSuite(cases))