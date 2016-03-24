# Quiz1 Ans 

---

##一. 填空题
1. 119; 167
2. 4G; 16EB (2^64B; 16384PB)
3. 101011.00000111; 53.017676
4. 虚拟文件系统（包含系统核心信息）； 配置文件（存储系统、服务的配置目录和文件）
5. 字符设备文件；块设备文件；（套接口文件）
6. 长； 短
7. user commands; system calls; libc calls; devices and special files; file formats and protocals
8. 之前的目录； 用户家目录
9. chmod a+x FILENAME; chmod 754 FILENAME
10. /var/log/wtmp; /var/log/utmp
11. uname -r (-v); uname -i
12. ls --color=auto; cp -r
13. set UID; 使拥有x权限的用户在该文件执行阶段具有该文件的owner权限
14. Byte; KB, MB, GB等
15. resource configuration

##二. 选择题
1~5：DCBCB
6~10：AADB(CD)
11~15：A(ABD)AB(ABCD)
16~20：BDCDA
21~25：(AD)(BD)AD(ABD)
26：dr-x-wx-wx
27~30：BBBA

##三. 解答题
1. 
l: long list format;
h: human readable (size);
d: list directories themselves but not their contents;
g: do not list owner;
G: in long listing, don't print group names;
o: do not list group info;
t: sort by modification time, newest first;
r: reverse order while sorting;
.*: 列出以.开头的所有目录及文件

2. 
which：查找可执行文件；
whereis和locate均为在数据库中查找，而find直接进行硬盘查找；
whereis：对文件名进行查找；
locate：对关键词进行查找

3. 
mtime: modify time; (文件内容被修改）
atime: access time;
ctime: change/create time;（文件状态（inode信息）改变）
用法：
find -mtime +n n天之前（不含n天）被修改过
find -mtime -n n天之内（不含n天）被修改过
find -mtime n n天之前的“一天之内”被修改过

4. 
多条件查询：使用-a, -o连接多个条件；
查询结果的处理：-exec COMMAND; -ok COMMAND; ...|xargs COMMAND 等

5. 
查看系统中相关的说明文件；-f为完全匹配所给出的字符串；-k为以所给出的字符串为关键词进行查找

6. 
w： 返回登陆的用户及其行为（较详细）
who： 返回登陆的用户

7. 
/dev/zero 无限0资源（输出）
/dev/null 无限数据接收（黑洞）
/dev/random 与 /dev/urandom 随机数生成

8. 
write USER TTY

9. 重要的系统执行文件（开机、修复、还原系统、设置系统环境所需的命令）

10. 
文件类型与权限；
多少文件名连接到此节点（inode）；（注：非“文件数”；对于目录也不可以称为“硬连接数”）
owner;
group; （文件或目录所属的group）
大小；
最近修改日期；
文件名

11. 
使用户对该目录的权限为rwx（可通过将用户加入新建组、更改目录所属组、并修改目录权限实现；或通过setfacl修改用户对目录的权限实现）；
修改用户个人的umask，使得同组用户对该用户创建的新文件默认具有写的权限

12. 
文件拷贝创建新文件，具有新的inode；而硬链接不具有新的inode；
实验：
查看文件inode;
修改文件，查看对源文件的影响。




