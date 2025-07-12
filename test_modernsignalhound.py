# test_modernsignalhound.py
"""
Tests for ModernSignalHound module.
"""

import unittest
from modernsignalhound import ModernSignalHound

class TestModernSignalHound(unittest.TestCase):
    """Test cases for ModernSignalHound class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModernSignalHound()
        self.assertIsInstance(instance, ModernSignalHound)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModernSignalHound()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
