# -*- coding:utf-8 -*-

import pytest
from Utils.GetKeywords import GetKeywords
from Utils.OperationData import OperationData

op_data = OperationData("member_info.xls")
data_list = op_data.get_data_list()


@pytest.mark.parametrize("title,supplier,telephone,code,message",data_list)
def test_02_add_member(member,title,supplier,telephone,code,message):
    print(title)
    result = member.add_member(supplier,telephone)
    print(result)
    pytest.assume(GetKeywords.get_keyword(result,"status_code") == 200)
    pytest.assume(GetKeywords.get_keyword(result,"code") == int(code))
    pytest.assume(GetKeywords.get_keyword(result,"message") == message)



if __name__ == '__main__':
    pytest.main()
