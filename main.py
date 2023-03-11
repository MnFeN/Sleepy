import shutil
import datetime

print('本工具可在角色技能栏中添加四个游戏中未正式启用的情感动作，')
print('包括在任意位置睡觉和坐下。')
print('请将程序置于 My Games 中的角色文件夹下，与 HOTBAR.DAT 并列。')
print('使用前确保以管理员模式运行程序，且游戏未登录相应角色。')
print('by MnFeN, 2023.3.6')
input('------------------------按回车继续------------------------\n')

try:
    now = datetime.datetime.now().strftime('%y%m%d_%H%M%S')
    shutil.copyfile('HOTBAR.DAT', f'HOTBAR.DAT.{now}.BACKUP')
    print(f'热键栏数据已生成备份：HOTBAR.DAT.{now}.BACKUP')

    with open('HOTBAR.DAT', 'r+b') as file:
        file.seek(2320)
        file.write(b'\x691110117\x511110107\xc21110137\xc51110127')
        print(f'成功编辑 HOTBAR.DAT，情感动作已添加至剑术师的 1 号技能栏')
        
except FileNotFoundError:
    print('目录下未找到 HOTBAR.DAT 文件。')
except PermissionError:
    print('无法访问文件，请确保以管理员模式运行程序。')
input()
