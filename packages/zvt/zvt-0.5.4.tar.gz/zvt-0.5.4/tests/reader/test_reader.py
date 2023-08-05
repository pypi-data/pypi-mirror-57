# -*- coding: utf-8 -*-
from ..context import init_test_context

init_test_context()

import time

from zvt.api.rules import iterate_timestamps
from zvt.domain import Stock1dKdata

from zvdata.utils.time_utils import to_time_str

from zvdata.reader import DataReader
from zvdata import IntervalLevel


def test_china_stock_reader():
    data_reader = DataReader(codes=['002572', '000338'], data_schema=Stock1dKdata, provider='joinquant',
                             start_timestamp='2019-01-01',
                             end_timestamp='2019-06-10', entity_provider='eastmoney')

    categories = data_reader.data_df.index.levels[0].to_list()

    df = data_reader.data_df

    assert 'stock_sz_002572' in categories
    assert 'stock_sz_000338' in categories

    assert ('stock_sz_002572', '2019-01-02') in df.index
    assert ('stock_sz_000338', '2019-01-02') in df.index
    assert ('stock_sz_002572', '2019-06-10') in df.index
    assert ('stock_sz_000338', '2019-06-10') in df.index

    for timestamp in iterate_timestamps(entity_type='stock', exchange='sz',
                                        level=IntervalLevel.LEVEL_1DAY,
                                        start_timestamp='2019-06-11',
                                        end_timestamp='2019-06-14'):
        data_reader.move_on(to_timestamp=timestamp)

        df = data_reader.data_df

        assert ('stock_sz_002572', timestamp) in df.index
        assert ('stock_sz_000338', to_time_str(timestamp)) in df.index


def test_reader_move_on():
    data_reader = DataReader(codes=['002572', '000338'], data_schema=Stock1dKdata, provider='joinquant',
                             start_timestamp='2019-06-13',
                             end_timestamp='2019-06-14', entity_provider='eastmoney')

    data_reader.move_on(to_timestamp='2019-06-15')
    assert ('stock_sz_002572', '2019-06-15') not in data_reader.data_df.index
    assert ('stock_sz_000338', '2019-06-15') not in data_reader.data_df.index

    start_time = time.time()
    data_reader.move_on(to_timestamp='2019-06-20', timeout=5)
    assert time.time() - start_time < 5
