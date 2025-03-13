total_land = 80

tomato_sales_1 = total_land / 5.0 * 0.3 * 7
tomato_sales_2 = total_land / 5.0 * 0.7 * 7

total_tomato_sales = tomato_sales_1 + tomato_sales_2
potato_sales = total_land / 5.0 * 10 * 1000 * 20
cabbage_sales = total_land / 5.0 * 14 * 1000 * 24
sunflower_sales = total_land / 5.0 * .7 * 1000 * 200
sugarcane_sales = total_land / 5.0 * 45 * 4000

total_sales = total_tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

total_sales_2 = total_sales - sugarcane_sales

print(f'Total sales realization is {total_sales}')
print(f'Total sales realization after 11 months is {total_sales_2}')
