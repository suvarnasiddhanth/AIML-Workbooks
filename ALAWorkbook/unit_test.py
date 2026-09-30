import math
import pytest

from Vector import Vec


class TestMean:
    def test_mean_of_positive_values(self):
        v = Vec([2, 4, 6, 8])
        assert v.mean() == 5

    def test_mean_of_negative_values(self):
        v = Vec([-2, -4, -6])
        assert v.mean() == -4

    def test_mean_can_be_fractional(self):
        v = Vec([1, 2])
        assert v.mean() == 1.5

    def test_mean_of_singleton_is_the_element(self):
        v = Vec([42])
        assert v.mean() == 42

    def test_mean_of_symmetric_values_is_zero(self):
        v = Vec([-10, -5, 0, 5, 10])
        assert v.mean() == 0

    def test_mean_is_translation_equivariant(self):
        """
        Adding a constant c to every element should increase
        the mean by exactly c.
        """
        v = Vec([1, 4, 7, 10])
        shifted = Vec([x + 13 for x in v.elements])

        assert shifted.mean() == pytest.approx(v.mean() + 13)

    def test_mean_is_linear_under_scaling(self):
        v = Vec([2, 5, 9])
        scaled = Vec([7 * x for x in v.elements])

        assert scaled.mean() == pytest.approx(7 * v.mean())

    def test_mean_is_invariant_under_permutation(self):
        v = Vec([1, 9, 3, 7, 4])
        shuffled = Vec([4, 7, 1, 3, 9])

        assert shuffled.mean() == v.mean()

    def test_empty_vector_has_no_mean(self):
        with pytest.raises(ValueError):
            Vec().mean()


class TestDemean:
    def test_demean_basic_example(self):
        v = Vec([2, 4, 6])
        assert v.demean() == Vec([-2, 0, 2])

    def test_demean_singleton_is_zero(self):
        v = Vec([123])
        assert v.demean() == Vec([0])

    def test_demean_symmetric_vector(self):
        v = Vec([-3, 0, 3])
        assert v.demean() == Vec([-3, 0, 3])

    def test_demeaned_vector_has_zero_mean(self):
        v = Vec([3, 7, 11, 19])
        assert v.demean().mean() == pytest.approx(0)

    def test_demean_does_not_modify_original(self):
        v = Vec([1, 2, 3])

        result = v.demean()

        assert v == Vec([1, 2, 3])
        assert result is not v

    def test_demean_is_translation_invariant(self):
        """
        Shifting every element by the same constant should
        not change the demeaned vector.
        """
        v = Vec([2, 5, 11])
        shifted = Vec([102, 105, 111])

        assert shifted.demean() == v.demean()

    def test_demean_of_already_demeaned_vector_is_unchanged(self):
        v = Vec([4, 8, 15, 16, 23, 42])

        once = v.demean()
        twice = once.demean()

        assert twice == once

    def test_sum_of_demeaned_entries_is_zero(self):
        v = Vec([10, 20, 30, 40, 50])

        assert sum(v.demean().elements) == pytest.approx(0)

    def test_demean_preserves_pairwise_differences(self):
        """
        Removing the mean changes the origin, not the distances
        between observations.
        """
        v = Vec([3, 8, 15])
        d = v.demean()

        original_difference = v.elements[2] - v.elements[0]
        demeaned_difference = d.elements[2] - d.elements[0]

        assert demeaned_difference == pytest.approx(original_difference)


class TestStd:
    def test_std_basic_example(self):
        v = Vec([2, 4, 6])
        # Mean = 4
        # Variance = (4 + 0 + 4) / 3
        expected = math.sqrt(8 / 3)

        assert v.std() == pytest.approx(expected)

    def test_std_of_constant_vector_is_zero(self):
        v = Vec([7, 7, 7, 7])

        assert v.std() == pytest.approx(0)

    def test_std_of_singleton_is_zero(self):
        v = Vec([12345])

        assert v.std() == pytest.approx(0)

    def test_std_is_non_negative(self):
        v = Vec([-10, 2, 100])

        assert v.std() >= 0

    def test_std_is_translation_invariant(self):
        """
        Adding the same constant to every observation changes
        the mean but not the spread.
        """
        v = Vec([1, 3, 7, 11])
        shifted = Vec([101, 103, 107, 111])

        assert shifted.std() == pytest.approx(v.std())

    def test_std_scales_by_absolute_value(self):
        """
        std(cX) = |c| * std(X)
        """
        v = Vec([1, 3, 8])

        assert Vec([4 * x for x in v.elements]).std() == pytest.approx(
            4 * v.std()
        )

        assert Vec([-4 * x for x in v.elements]).std() == pytest.approx(
            4 * v.std()
        )

    def test_std_is_invariant_under_permutation(self):
        v = Vec([1, 2, 8, 10])
        shuffled = Vec([10, 8, 1, 2])

        assert shuffled.std() == pytest.approx(v.std())

    def test_std_of_symmetric_values(self):
        """
        For [-a, 0, a], std = a * sqrt(2/3).
        """
        v = Vec([-6, 0, 6])
        expected = 6 * math.sqrt(2 / 3)

        assert v.std() == pytest.approx(expected)

    def test_std_can_be_derived_from_demeaned_vector(self):
        """
        Verify that std really corresponds to the RMS of
        the demeaned entries.
        """
        v = Vec([1, 4, 9, 16])
        d = v.demean()

        expected = math.sqrt(
            sum(x ** 2 for x in d.elements) / len(d)
        )

        assert v.std() == pytest.approx(expected)

    def test_std_depends_on_spread_not_location(self):
        """
        Two datasets with identical shape but different locations
        should have identical standard deviations.
        """
        first = Vec([10, 12, 14, 16])
        second = Vec([1000, 1002, 1004, 1006])

        assert first.std() == pytest.approx(second.std())

    def test_std_of_zero_vector(self):
        v = Vec([0, 0, 0, 0, 0])

        assert v.std() == 0


class TestMeanDemeanStdRelationship:
    def test_demean_and_mean_form_a_zero_mean_residual(self):
        v = Vec([5, 8, 12, 20])

        residual = v.demean()

        assert pytest.approx(sum(residual.elements)) == 0

    def test_variance_equals_mean_squared_demeviations(self):
        v = Vec([1, 2, 5, 10])
        d = v.demean()

        expected_variance = sum(x ** 2 for x in d.elements) / len(d)

        assert v.std() ** 2 == pytest.approx(expected_variance)

    def test_std_of_demeaned_vector_matches_original(self):
        """
        Demeaning changes location but does not change spread.
        """
        v = Vec([2, 7, 13, 21])

        assert v.demean().std() == pytest.approx(v.std())

    def test_mean_plus_demeaned_entry_recovers_original(self):
        v = Vec([3, 8, 15, 22])
        mean = v.mean()
        demeaned = v.demean()

        recovered = Vec(
            [x + mean for x in demeaned.elements]
        )

        assert recovered == v

    def test_constant_shift_preserves_demeaning_and_std(self):
        v = Vec([4, 9, 16, 25])
        shifted = Vec([104, 109, 116, 125])

        assert shifted.demean() == v.demean()
        assert shifted.std() == pytest.approx(v.std())

    def test_negating_vector_preserves_std(self):
        v = Vec([-2, 4, 9, 15])
        negated = Vec([-x for x in v.elements])

        assert negated.std() == pytest.approx(v.std())

    @pytest.mark.parametrize(
        "values",
        [
            [1, 2, 3],
            [-10, 0, 10],
            [1.5, 2.5, 7.5],
            [100, 101, 103, 107],
            [-5, -4, -3, -2, -1],
        ],
    )
    def test_demeaned_values_always_sum_to_zero(self, values):
        v = Vec(values)

        assert sum(v.demean().elements) == pytest.approx(0)

    @pytest.mark.parametrize(
        "values",
        [
            [1, 2, 3],
            [-10, 0, 10],
            [1.5, 2.5, 7.5],
            [100, 101, 103, 107],
        ],
    )
    def test_std_is_unchanged_by_constant_shift(self, values):
        v = Vec(values)
        shifted = Vec([x + 1000 for x in values])

        assert shifted.std() == pytest.approx(v.std())
