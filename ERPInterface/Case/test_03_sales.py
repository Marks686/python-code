# -*- coding:utf-8 -*-
import pytest
from Utils.GetKeywords import GetKeywords


def test_03_sales_order_out(sales, db):
    sql = 'SELECT js.current_number from jsh_material jm join jsh_material_current_stock js on jm.id = js.material_id where `name` = "小米剃须刀"'
    res = db.get_one(sql)
    num1 = int(res["current_number"])
    print(num1)

    result_order = sales.add_sales_order()
    status_code = GetKeywords.get_keyword(result_order, "status_code")
    msg = GetKeywords.get_keyword(result_order, "msg")
    pytest.assume(status_code == 200)
    pytest.assume(msg == "操作成功")

    result_out = sales.add_sales_out()
    status_code = GetKeywords.get_keyword(result_out, "status_code")
    msg = GetKeywords.get_keyword(result_out, "msg")
    pytest.assume(status_code == 200)
    pytest.assume(msg == "操作成功")

    # 断言存库减少
    res = db.get_one(sql)
    num2 = int(res["current_number"])
    print(num2)
    pytest.assume(num1 - num2 == 1)


if __name__ == '__main__':
    pytest.main()
