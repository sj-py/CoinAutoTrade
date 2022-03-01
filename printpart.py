#코인명만 바꿔서 사용가능
# elif upbit.get_balance("BTC"):
#         #Started Part Of Printing Information About BTC
#             #시간
#             now = datetime.datetime.now()
#             start_time = get_start_time("KRW-BTC")
#             end_time = start_time + datetime.timedelta(days=1)
#             #현재가격
#             now_price = get_current_price("KRW-BTC")
#             #매수 목표 가격
#             if start_time < now < start_time + datetime.timedelta(hours=6):
#                 wish_price = get_target_price("KRW-BTC", 0.6)
#                 #print("dldl")
#             else: #start_time - datetime.timedelta(hours=6) < now < end_time - datetime.timedelta(seconds=10):
#                 wish_price = get_target_price2("KRW-BTC", 0.2)
#                 #print("qwqw")
#             print("현재 거래코인은 BTC입니다.")
#             print("현재시각 : " + str(now))
#             print("BTC보유량 : " + str(upbit.get_balance("KRW-BTC")))   # KRW-BTC 조회
#             print("KRW보유량 : " + str(int(upbit.get_balance("KRW"))))  # 보유 현금 조회
#             print("BTC에 할당된 KRW : " + str(int(get_balance("KRW"))))
#             print("현재가격 : " + str(now_price))
#             print("매수목표가격 : " + str(wish_price) )
#             get_sell_price("KRW-BTC")
#             print("==========================================")
#         #Finished Part Of Printing Information About BTC