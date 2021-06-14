import unittest

from tf2rl.algos.curl_sac import CURL
from tests.algos.common import CommonOffPolImgContinuousAlgos


class TestSAC(CommonOffPolImgContinuousAlgos):
    @classmethod
    def setUpClass(cls):
        super().setUpClass(img_dim=100)
        cls.agent = CURL(
            action_dim=cls.continuous_env.action_space.low.size,
            batch_size=cls.batch_size,
            gpu=-1)


if __name__ == '__main__':
    unittest.main()
