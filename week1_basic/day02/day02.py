import requests




def fetch_juejin():
    url = "https://api.juejin.cn/interact_api/v1/message/count"

    params = {
        "aid": 2608,
        "uuid": "7551251884074829366",
        "spider": 0
    }
    cookie_str = "_tea_utm_cache_2608=undefined; __tea_cookie_tokens_2608=%257B%2522web_id%2522%253A%25227551251884074829366%2522%252C%2522user_unique_id%2522%253A%25227551251884074829366%2522%252C%2522timestamp%2522%253A1758162848206%257D; passport_csrf_token=719a3d200d7eb43d7d452fefd32a8fad; passport_csrf_token_default=719a3d200d7eb43d7d452fefd32a8fad; n_mh=CkuPnz9oTsh0SrWTo8X-A4Iv6lWhfXwf1fW1-ywqfTo; sid_guard=07c5b0344aefebd9c21fdc46fcf7069d%7C1761010963%7C31536000%7CWed%2C+21-Oct-2026+01%3A42%3A43+GMT; uid_tt=4ad0393a766b39c51a61debd82495513; uid_tt_ss=4ad0393a766b39c51a61debd82495513; sid_tt=07c5b0344aefebd9c21fdc46fcf7069d; sessionid=07c5b0344aefebd9c21fdc46fcf7069d; sessionid_ss=07c5b0344aefebd9c21fdc46fcf7069d; session_tlb_tag=sttt%7C3%7CB8WwNErv69nCH9xG_PcGnf_________Z0_TM0GF_4NURN5uggre5VuXoXv0f1odLXf5m2fO_iSc%3D; is_staff_user=false; sid_ucp_v1=1.0.0-KDRiMmY5Mjk4NGQxMzg1OWE0MTdlMTdlNjc2NzEwNTdmOWViZDZjZWQKFgiJu6DX8s01EJPK28cGGLAUOAJA8QcaAmxmIiAwN2M1YjAzNDRhZWZlYmQ5YzIxZmRjNDZmY2Y3MDY5ZA; ssid_ucp_v1=1.0.0-KDRiMmY5Mjk4NGQxMzg1OWE0MTdlMTdlNjc2NzEwNTdmOWViZDZjZWQKFgiJu6DX8s01EJPK28cGGLAUOAJA8QcaAmxmIiAwN2M1YjAzNDRhZWZlYmQ5YzIxZmRjNDZmY2Y3MDY5ZA; csrf_session_id=c96b50e6171c9497f781c6908f3190b8"

    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    "cookies": cookie_str}
    s = requests.Session()
    resp = s.get(url, params=params, headers=headers)
    data = resp.json()
    print(data)
    print(s.cookies)
      




# def fetch_page(query, page=2):
#     limit = 20
#     cursor = '0'
#     for i in range(page):
#         print(f"正在爬取 {query} 的第 {i} 页数据")
#         next_cursor, has_more = fetch_juejin(query, cursor, limit)
#          # ⭐ 优先判断 cursor 是否有效
#         if not next_cursor:
#             print("cursor 无效，停止")
#             break

#         if not has_more:
#             print("已无更多数据")
#             break

#         cursor = next_cursor


if __name__ == '__main__':
    fetch_juejin()



