import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def setUp(self):
        # 在每个测试之前运行的代码
        self.emotion_dict = {
            "I am glad this happened": "joy",
            "I am really mad about this": "anger",
            "I feel disgusted just hearing about this": "disgust",
            "I am so sad about this": "sadness",
            "I am really afraid that this will happen": "fear"
        }

    def test_emotion_detection(self):
        for stmt, expected_emotion in self.emotion_dict.items():
            with self.subTest(stmt=stmt):
                emotion_resp = emotion_detector(stmt)
                self.assertEqual(emotion_resp['dominant_emotion'], expected_emotion)

if __name__ == '__main__':
    unittest.main()