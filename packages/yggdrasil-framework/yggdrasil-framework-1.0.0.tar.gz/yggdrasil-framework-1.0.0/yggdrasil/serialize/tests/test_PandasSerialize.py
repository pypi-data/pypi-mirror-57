import numpy as np
import pandas as pd
from yggdrasil.serialize.tests import test_AsciiTableSerialize as parent


class TestPandasSerialize(parent.TestAsciiTableSerialize):
    r"""Test class for TestPandasSerialize class."""

    _cls = 'PandasSerialize'

    def test_apply_field_names_errors(self):
        r"""Test errors raised by apply_field_names."""
        self.assert_raises(RuntimeError, self.instance.apply_field_names,
                           pd.DataFrame({'x': np.zeros(3), 'y': np.zeros(3)}),
                           field_names=self.instance.get_field_names())
        names = self.testing_options['objects'][0].columns.tolist()
        names[0] = 'invalid'
        self.assert_raises(RuntimeError, self.instance.apply_field_names,
                           pd.DataFrame({k: np.zeros(3) for k in names}),
                           field_names=self.instance.get_field_names())

    def test_func_serialize_errors(self):
        r"""Test errors raised by func_serialize."""
        self.assert_raises(TypeError, self.instance.func_serialize, None)
