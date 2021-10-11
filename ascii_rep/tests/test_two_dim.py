import unittest
from ascii_rep.ascii_rep.two_dim import *

class TestAsciiMethods(unittest.TestCase):

    def test_docs_gen(self):
        a = np.array([[1,2,3],[4,5,6],[7,8,9]])
        print(decorate(a))

    def test_decorate_exception(self):
        small_array = np.arange(6).reshape(2, 3)
        big_array = np.arange(24).reshape(2, 3, 4)
        self.assertRaises(ValueError, decorate, big_array)

        try:
            decorate(small_array)
        except ValueError:
            self.fail(f"decorate() raised {ValueError} unexpectedly!")

    def test_decorate_does_not_change_input(self):
        small_array = np.arange(6).reshape(2, 3)
        expected = small_array.copy()
        decorate(small_array)
        self.assertTrue(np.array_equal(expected, small_array, equal_nan=False))

    def test_decorate(self):
        a = np.arange(0, 90, 5)
        small_array = 10 * np.sin(a)
        small_array = np.reshape(small_array, (-1, 3))
        print(decorate(small_array))

    def test_decorate_complex(self):
        a_complex = np.random.random(6) + np.random.random(6) * 1j  # random complex128 array
        a_complex = np.reshape(a_complex, (3, -1))
        print(decorate(a_complex))

    def test_string_cast_copy(self):
        a_complex = np.random.random(6) + np.random.random(6) * 1j  # random complex128 array
        a_complex = np.reshape(a_complex, (3, -1))
        str_arr = copy_as_str(a_complex)
        self.assertTupleEqual(a_complex.shape, str_arr.shape)

    def test_string_cast_copy_all_dims(self):
        axis_one_array = np.random.random(6)  # one dimensional array edge case. actually not considered for decoration
        str_arr = copy_as_str(axis_one_array)
        self.assertTupleEqual(axis_one_array.shape, str_arr.shape)

        v_row = np.reshape(axis_one_array, (1, -1))
        str_arr = copy_as_str(v_row)
        self.assertTupleEqual(v_row.shape, str_arr.shape)

        v_col = np.reshape(axis_one_array, (-1, 1))
        str_arr = copy_as_str(v_col)
        self.assertTupleEqual(v_col.shape, str_arr.shape)

        a2_3 = np.reshape(axis_one_array, (2, 3))
        str_arr = copy_as_str(a2_3)
        self.assertTupleEqual(a2_3.shape, str_arr.shape)

        a2_1_1 = np.reshape(axis_one_array, (2, 3, 1))
        str_arr = copy_as_str(a2_1_1)
        self.assertTupleEqual(a2_1_1.shape, str_arr.shape)

    def test_max_len_in_col(self):
        data = ['lorem', 'ipsum', 'is', 'simply', 'dummy', 'text', 'of', 'the', 'printing', 'and', 'typesetting',
                'industry']
        str_arr = np.array(data)
        str_arr = str_arr.reshape(6, 2)
        max_len_in_col(str_arr)

    def test_gen_format_string(self):
        a = np.array([[1,2,3],[1231,-234523523000000011,2342],[0,0,0]])
        a_str = copy_as_str(a)
        fmt_str = gen_format_string(a)
        print(fmt_str.format(*a.flatten()))

    def test_decorate_aug(self):
        a = np.array([[10,1],[2,3],[4,5]])
        b = np.array([[1],[2],[3]])
        bf = np.array([[1],[2],[3],[4]])
        self.assertRaises(ValueError, decorate_aug, a, bf)
        print(decorate_aug(a, b))
        b = np.array([[1,1],[2,2],[3,3]])
        print(decorate_aug(a, b))


