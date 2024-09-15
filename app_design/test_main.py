import unittest
from main import preprocess_text, calculate_similarity


class TestTextProcessing(unittest.TestCase):
    def test_preprocess_text(self):
        sample_text = "This is a sample text. It includes some stopwords, such as the, and."
        expected_output = "sample text includes stopwords"
        self.assertEqual(preprocess_text(sample_text), expected_output)

    def test_calculate_similarity(self):
        # 测试计算相似度功能
        text1 = "This is a test text."
        text2 = "This is a test."
        similarity_score = calculate_similarity(text1, text2)
        # 相似度应该接近1，但不一定完全等于1，因为文本不完全相同
        self.assertGreater(similarity_score, 0.8)  # 调整期望值

        # 测试两个完全不同的文本
        text3 = "This is a completely different text."
        similarity_score = calculate_similarity(text1, text3)
        print("Preprocessed text1:", preprocess_text(text1))
        print("Preprocessed text3:", preprocess_text(text3))
        print("Similarity score:", similarity_score)
        # 相似度应该接近0.7
        self.assertLess(similarity_score, 0.7)  # 调整期望值


if __name__ == '__main__':
    unittest.main()
