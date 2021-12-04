import unittest
import dotenv
from src.config.Configuration import Configuration


class ConfigTests(unittest.TestCase):
    def test_shouldGetValuesFromDotenvFile(self):
        # Arrange
        dotenvcfg = dotenv.dotenv_values("./test/.env.test")

        # Act
        configuration = Configuration("./test/.env.test")

        # Assert
        self.assertEqual(configuration.db.host, dotenvcfg.get("APP_DB_HOST"))
        self.assertEqual(configuration.db.port, int(dotenvcfg.get("APP_DB_PORT")))
        self.assertEqual(configuration.db.user, dotenvcfg.get("APP_DB_USER"))
        self.assertEqual(configuration.db.password, dotenvcfg.get("APP_DB_PASSWORD"))
        self.assertEqual(configuration.db.file, dotenvcfg.get("APP_DB_FILE"))


if __name__ == '__main__':
    unittest.main()
