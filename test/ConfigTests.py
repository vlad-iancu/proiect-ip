import unittest
import dotenv
from src.config.Configuration import get_configuration


class ConfigTests(unittest.TestCase):
    def test_shouldGetValuesFromDotenvFile(self):
        # Arrange
        dotenvcfg = dotenv.dotenv_values(".env.test")

        # Act
        configuration = get_configuration(".env.test")

        # Assert
        self.assertEqual(configuration.db_host, dotenvcfg.get("APP_DB_HOST"))
        self.assertEqual(configuration.db_port, int(dotenvcfg.get("APP_DB_PORT")))
        self.assertEqual(configuration.db_user, dotenvcfg.get("APP_DB_USER"))
        self.assertEqual(configuration.db_password, dotenvcfg.get("APP_DB_PASSWORD"))
        self.assertEqual(configuration.db_file, dotenvcfg.get("APP_DB_FILE"))


if __name__ == '__main__':
    unittest.main()
