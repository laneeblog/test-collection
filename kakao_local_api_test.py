import requests
import json

'''
1. 타이핑 할 때마다 주소 및 키워드로 나오는 결과를 리스트로 받아서 선택 옵션으로 제시
2. 옵션 중 하나를 선택하면 해당 id로 영업점 정보 가져와서 필요한 정보 추출

'''

# 설정
rest_api_key = "e105d32d47fadac4f39740fb186deb5e"
keyword_api = "https://dapi.kakao.com/v2/local/search/keyword.json"
address_api = "https://dapi.kakao.com/v2/local/search/address.json"
detailed_url = "https://place.map.kakao.com/main/v/"

# 사용자가 키워드 또는 주소를 입력하면 
input_text = "윙스터디"
headers = {"Authorization": f"KakaoAK {rest_api_key}"}
data = {
    "query": input_text
}
keyword_result = json.loads(requests.get(keyword_api, headers=headers, data=data).text)['documents']
address_result = json.loads(requests.get(address_api, headers=headers, data=data).text)['documents']
total_result = keyword_result + address_result

# 입력한 내용으로 검색된 결과를 선택할 수 있게 제공
list_for_selection = []
for r in total_result:
    list_for_selection.append([r['id'], r['address_name']])

# 사용자가 그 중에 하나를 선택하면 id 를 받아서 상세 정보 가져온 후
id_selected = '153694103'
detailed_data = json.loads(requests.get(detailed_url + id_selected, headers=headers).text)
basicInfo = detailed_data['basicInfo'] # placenamefull, mainphotourl, phonenum, address조합, homepage, tags, wpointx-y
blogReview =detailed_data['blogReview'] # list
comment = detailed_data['comment'] # list
menuInfo = detailed_data['menuInfo'] # menuList
photo = detailed_data['photo'] # photoList[0]['list']

# 필요한 정보 추출