https://leetcode.cn/problems/find-customer-referee/

SELECT name
FROM customer
WHERE referee_id is null
or
referee_id != 2;