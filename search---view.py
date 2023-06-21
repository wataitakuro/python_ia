import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here


    if q_name :
        customgoods = customgoods.filter(name_icontains=q_name)
    if q_management_code:
        customgoods = customgoods.filter(management_code_icontains==q_management_code)
    if q_group:
        customgoods = customgoods.filter(group=q_group)
    if q_price_begin:
        customgoods = customgoods.filter(price_gte=q_price_begin)
    if q_price_end:
        customgoods = customgoods.filter(price_lte=q_price_end)

    return customgoods

#一覧表示の際に並び替えを行う例
class CustomGoodsListView(generic.ListView):

    #並び替えをするorder_by('フィールド名')昇順
    #order_by('-フィールド名')-を付ける降順
    queryset = CustomGoodsListView.all().order_by('-id')

