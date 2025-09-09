from cmath import rect, polar
from math import degrees, radians


class SymmetricalComponents:
    """
    Class for calculating symmetrical components of three-phase voltages/currents.

    Symmetrical components are a mathematical tool used in the analysis
    of unbalanced three-phase electrical systems.
    """

    def __init__(self):
        """Initializes the class with the alpha operator (120°)"""
        self.alpha = (1, 120)  # Rotational operator of 120°

    @staticmethod
    def _angles_deg_to_rad(value_deg: tuple) -> tuple:
        """
        Converts angles from degrees to radians.

        Args:
            value_deg: Tuple (magnitude, angle_in_degrees)

        Returns:
            Tuple (magnitude, angle_in_radians)
        """
        return value_deg[0], radians(value_deg[1])

    @staticmethod
    def _round_small_values(magnitude: float, threshold: float = 0.0001) -> float:
        """
        Rounds very small values to zero.

        Args:
            magnitude: Magnitude value
            threshold: Threshold to consider as zero

        Returns:
            Rounded magnitude
        """
        return 0.000 if magnitude < threshold else round(magnitude, 3)

    def _format_result(self, complex_result: tuple) -> tuple:
        """
        Formats the final result with 3 decimal places and converts to degrees.

        Args:
            complex_result: Result in polar coordinates (magnitude, angle_rad)

        Returns:
            Tuple (rounded_magnitude, rounded_angle_in_degrees)
        """
        magnitude_rounded = self._round_small_values(complex_result[0])
        angle_degrees = round(degrees(complex_result[1]), 3)

        return round(magnitude_rounded, 3), angle_degrees

    def zero_sequence_component(self, ua: tuple, ub: tuple, uc: tuple) -> tuple:
        """
        Calculates the zero-sequence component.

        U0 = (Ua + Ub + Uc) / 3

        Args:
            ua: Phase A voltage (magnitude, angle_in_degrees)
            ub: Phase B voltage (magnitude, angle_in_degrees)
            uc: Phase C voltage (magnitude, angle_in_degrees)

        Returns:
            Zero-sequence component (magnitude, angle_in_degrees)
        """
        # Convert angles to radians
        ua_rad = self._angles_deg_to_rad(ua)
        ub_rad = self._angles_deg_to_rad(ub)
        uc_rad = self._angles_deg_to_rad(uc)

        # Calculate zero-sequence component
        u0 = polar((rect(*ua_rad) + rect(*ub_rad) + rect(*uc_rad)) / 3)

        return self._format_result(u0)

    def positive_sequence_component(self, ua: tuple, ub: tuple, uc: tuple) -> tuple:
        """
        Calculates the positive-sequence component.

        U1 = (Ua + α*Ub + α²*Uc) / 3

        Args:
            ua: Phase A voltage (magnitude, angle_in_degrees)
            ub: Phase B voltage (magnitude, angle_in_degrees)
            uc: Phase C voltage (magnitude, angle_in_degrees)

        Returns:
            Positive-sequence component (magnitude, angle_in_degrees)
        """
        # Convert angles to radians
        ua_rad = self._angles_deg_to_rad(ua)
        ub_rad = self._angles_deg_to_rad(ub)
        uc_rad = self._angles_deg_to_rad(uc)
        alpha_rad = self._angles_deg_to_rad(self.alpha)

        # Calculate positive-sequence component
        alpha_complex = rect(*alpha_rad)
        u1 = polar((rect(*ua_rad) +
                    rect(*ub_rad) * alpha_complex +
                    rect(*uc_rad) * (alpha_complex ** 2)) / 3)

        return self._format_result(u1)

    def negative_sequence_component(self, ua: tuple, ub: tuple, uc: tuple) -> tuple:
        """
        Calculates the negative-sequence component.

        U2 = (Ua + α²*Ub + α*Uc) / 3

        Args:
            ua: Phase A voltage (magnitude, angle_in_degrees)
            ub: Phase B voltage (magnitude, angle_in_degrees)
            uc: Phase C voltage (magnitude, angle_in_degrees)

        Returns:
            Negative-sequence component (magnitude, angle_in_degrees)
        """
        # Convert angles to radians
        ua_rad = self._angles_deg_to_rad(ua)
        ub_rad = self._angles_deg_to_rad(ub)
        uc_rad = self._angles_deg_to_rad(uc)
        alpha_rad = self._angles_deg_to_rad(self.alpha)

        # Calculate negative-sequence component
        alpha_complex = rect(*alpha_rad)
        u2 = polar((rect(*ua_rad) +
                    rect(*ub_rad) * (alpha_complex ** 2) +
                    rect(*uc_rad) * alpha_complex) / 3)

        return self._format_result(u2)

    def calculate_all_components(self, ua: tuple, ub: tuple, uc: tuple) -> dict:
        """
        Calculates all symmetrical components at once.

        Args:
            ua: Phase A voltage (magnitude, angle_in_degrees)
            ub: Phase B voltage (magnitude, angle_in_degrees)
            uc: Phase C voltage (magnitude, angle_in_degrees)

        Returns:
            Dictionary with all components:
            {
                'zero': (magnitude, angle),
                'positive': (magnitude, angle),
                'negative': (magnitude, angle)
            }
        """
        return {
            'zero': self.zero_sequence_component(ua, ub, uc),
            'positive': self.positive_sequence_component(ua, ub, uc),
            'negative': self.negative_sequence_component(ua, ub, uc)
        }
