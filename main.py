import unittest
import tdd

class TddTest(unittest.TestCase):

    aa = 0
    bb = 0
    result = 0

    # 매 테스트 메소드 실행 전 동작
    def setUp(self):
        self.aa = 13
        self.bb = 18

    def testAdd(self):
        self.result = tdd.add(self.aa, self.bb)
        # 결과 값이 일치 여부 확인
        self.assertEqual(self.result, 31)

    # 매 테스트 메소드 실행 후 동작
    def tearDown(self):
        print(' 결과 값 : ' + str(self.result))


if __name__ == '__main__':
    unittest.main()