from unittest import TestCase
from utils.pagination import make_pagination_range


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1
        )['pagination']
        self.assertEqual(pagination, [1, 2, 3, 4])

    def test_first_range_is_static_if_current_page_is_less_than_middle(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=1
        )['pagination']
        self.assertEqual(pagination, [1, 2, 3, 4])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=2
        )['pagination']
        self.assertEqual(pagination, [1, 2, 3, 4])



    def test_make_sure_middle_ranges_are_correct(self):
        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=3
        )['pagination']
        self.assertEqual(pagination, [2, 3, 4, 5])

        pagination = make_pagination_range(
            page_range=list(range(1, 21)),
            qty_pages=4,
            current_page=15
        )['pagination']
        self.assertEqual(pagination, [14, 15, 16, 17])

    def test_make_pagination_range_is_static_when_last_page_is_next(self):
        pagination = make_pagination_range(
        page_range=list(range(1, 21)),
        qty_pages=4,
        current_page=19
    )['pagination']
        self.assertEqual(pagination, [17, 18, 19, 20])

