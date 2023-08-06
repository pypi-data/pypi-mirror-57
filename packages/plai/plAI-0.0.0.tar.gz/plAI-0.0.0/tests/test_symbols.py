from plai.parser import parse
from plai.symbol import Symbol


class TestVarSymbol:
    def test_symbol_added_to_table(self):
        parse('df')
        assert 'df' in Symbol.CACHE

