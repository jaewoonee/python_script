import sys
import os
from lxml import etree

#변경할 값
str_value = '5'
#변경할 설정의 xml 태그
str_mainTag = 'scm'
str_subTag = 'checkoutThreadTimeout'

#변경할 config.xml의 경로 리스트
config_path_list = []


#변경할 최상위 폴더 인자로 받기
try:
    targetDir = sys.argv[1]
except IndexError:
    print("it needs 1 argument, target directory")
    print("exiting..")
    sys.exit()


# 하위 폴더에서 config.xml 탐색, 변경할 리스트에 경로 추가
for (path, dir, files) in os.walk(targetDir):
    for filename in files:
        if filename == 'config.xml':
            config_path_list.append(path+'\\'+filename)



# xml의 경로와 수정할 값을 인자로 받는 Config xml 수정 함수
def change_config(config_path, modify_value):
    tree = etree.parse(config_path)

    for mainTag in tree.findall('.//' + str_mainTag):  # mainTag 찾기
        subTag = mainTag.find('./' + str_subTag)  # subTag 찾기

        # 수정할 subTag가 있으면
        if subTag is not None:
            subTag.text = modify_value   # 수정할 값 대입
            tree.write(config_path)   # 저장
            print('modify config : ' + config_path)
    
        # 수정할 subTag가 없으면
        else:
            subTag = etree.SubElement(mainTag, str_subTag)  # subTag 생성
            subTag.text = modify_value  # 수정할 값 대입
            tree.write(config_path)  # 저장
            print('add config : ' + config_path)



# 경로를 받아 xml 수정 함수 실행
for path in config_path_list:
    change_config(path, str_value)

print('-' * 60)
print('>>> all done')
print('    target tag   : ' + str_mainTag + '/' + str_subTag)
print('    change value : ' + str_value)