# *****************************************************************************
#
# Copyright (c) 2020, the pyEX authors.
#
# This file is part of the jupyterlab_templates library, distributed under the terms of
# the Apache License 2.0.  The full license can be found in the LICENSE file.
#

# for Coverage
import time

from mock import MagicMock, patch

SYMBOL = "aapl"


class TestAlternative:
    def teardown(self):
        time.sleep(0.1)  # prevent being blocked

    def test_crypto(self):
        from pyEX import crypto

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            crypto("test")

    def test_cryptoDF(self):
        from pyEX import cryptoDF

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            cryptoDF("test")

    def test_sentiment(self):
        from pyEX import sentiment

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            sentiment("test")

    def test_sentimentDF(self):
        from pyEX import sentimentDF

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            sentimentDF("test")

    def test_ceoComp(self):
        from pyEX import ceoCompensation

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            ceoCompensation("test")

    def test_ceoCompDF(self):
        from pyEX import ceoCompensationDF

        with patch("requests.get") as mock, patch("pickle.dump"):
            mock.return_value = MagicMock()
            mock.return_value.status_code = 200
            mock.return_value.json = MagicMock(return_value=[])
            ceoCompensationDF("test")
