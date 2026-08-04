import unittest

from user_parser import parse_user


class ParseUserTests(unittest.TestCase):
    def test_normal_name(self):
        self.assertEqual(parse_user({"name": " Ada "}), "Ada")

    def test_null_payload_returns_none(self):
        self.assertIsNone(parse_user(None))


if __name__ == "__main__":
    unittest.main()

