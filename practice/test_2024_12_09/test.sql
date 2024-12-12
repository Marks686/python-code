--mysql存储过程
create procedured d () begin
	declare
	    i int default 1;
    while
        i <= 10000 do
      insert into user
      values
        (i,concat("张三",i),13000000000+i,"123456");
      set i = i+1;
    end while
end

create procedured d() begin
    declare
        i int default 1;
    while
        i <= 10000 do
        insert into user
        values
        (i,concat("张三",i),13000000000+i,"123456");
        set i = i+1;
    end while
end