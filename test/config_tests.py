import unittest
import json
import os

from src.config.Config import Config
from src.config.AppEnvironmentEnum import AppEnvironment

TEST_CONFIG_FILE = "test/conf.test.json"
f = open(TEST_CONFIG_FILE, "r")
parsed = json.loads(f.read())
env = str(parsed["env"])
f.close()


class ConfigTests(unittest.TestCase):
    def test_shouldGetValuesFromJSON(self):
        # Act
        config = Config(TEST_CONFIG_FILE)

        # Assert
        self.assertEqual(config.env, AppEnvironment.parse(env))
        self.assertEqual(config.host, parsed[env]["host"])
        self.assertEqual(config.port, int(parsed[env]["port"]))
        self.assertEqual(config.db.host, parsed[env]["db"]["host"])
        self.assertEqual(config.db.port, int(
            parsed[env]["db"]["port"]))
        self.assertEqual(config.db.user, parsed[env]["db"]["user"])
        self.assertEqual(config.db.password,
                         parsed[env]["db"]["password"])

    def test_shouldOverrideConfigPropertiesWithEnvVars(self):
        # Arrange
        os.environ["APP_PORT"] = "7777"
        os.environ["APP_DB_USER"] = "new_db_user"

        # Act
        config = Config(TEST_CONFIG_FILE)

        # Assert
        self.assertEqual(config.env, AppEnvironment.parse(env))
        self.assertEqual(config.host, parsed[env]["host"])
        self.assertEqual(config.port, 7777)
        self.assertEqual(config.db.host, parsed[env]["db"]["host"])
        self.assertEqual(config.db.port, int(
            parsed[env]["db"]["port"]))
        self.assertEqual(config.db.user, "new_db_user")
        self.assertEqual(config.db.password,
                         parsed[env]["db"]["password"])


if __name__ == '__main__':
    unittest.main()
