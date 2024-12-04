# -*- coding:utf-8 -*-

import pytest
import os
import shutil

def run_all_tests():
    # 指定测试用例所在的目录
    test_directory = 'Case'

    # 指定生成的Allure结果文件夹
    allure_results_dir = 'Report'

    # 清除旧的结果文件夹
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir, exist_ok=True)

    # 使用 pytest.main() 运行测试，并生成Allure结果
    pytest_args = [
        test_directory,
        '--alluredir', allure_results_dir,
        '-s'  # 显示打印输出
    ]
    pytest.main(pytest_args)

    # 生成测试报告
    os.system(f"allure generate {allure_results_dir} --clean")
    os.system("allure open ./allure-report --port 9999")



if __name__ == "__main__":
    run_all_tests()
