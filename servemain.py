#거래파트 코인명 대문자와 소문자(변수)바꿔서 사용가능
#         #장 시작 직후
#         if start_time < now < start_time + datetime.timedelta(hours=6):
#             target_price = get_target_price("KRW-ETH", 0.6)
#             current_price = get_current_price("KRW-ETH")
#             if target_price < current_price:
#                 krw = get_balance("KRW")
#                 if krw > 5000:
#                     upbit.buy_market_order("KRW-ETH", krw*0.9995)
#                     print("Buy : " + str(target_price))
#             if ((current_price-target_price)/target_price) >= 0.01 or ((current_price-target_price)/target_price) <= -0.05:
#                 eth = get_balance("ETH")
#                 if eth > 0.00008:
#                     print("Sell : " + str(current_price))
#                     upbit.sell_market_order("KRW-ETH", eth*0.9995)
#         #장 시작 6시간 후
#         elif start_time + datetime.timedelta(hours=6) < now < end_time - datetime.timedelta(seconds=10):
#             #
#             target_price2 = get_target_price2("KRW-ETH", 0.2)
#             current_price = get_current_price("KRW-ETH")
#             if target_price2 < current_price:
#                 krw = get_balance("KRW")
#                 if krw > 5000:
#                     if current_price <= target_price2 + (target_price2*0.0002):
#                         upbit.buy_market_order("KRW-ETH", krw*0.9995)
#                         print("Buy : " + str(target_price2))
#             if ((current_price-target_price2)/target_price2) >= 0.01 or ((current_price-target_price2)/target_price2) <= -0.008:
                
#                 eth = get_balance("ETH")
#                 if eth > 0.00008:
#                     print("Sell : " + str(current_price))
#                     upbit.sell_market_order("KRW-ETH", eth*0.9995) 

#         else:
#             eth = get_balance("ETH")
#             if eth > 0.00008:
#                 upbit.sell_market_order("KRW-ETH", eth*0.9995)
#         time.sleep(1)