#encoding:utf-8
# 计算房贷函数
current_principal_all = []
current_interest_all = []
def calculate_house_loan(amount1, amount2, interest_rate1, loan_years1, interest_rate2, loan_years2):
    # 计算贷款总额和贷款月数 for 贷款1
    loan_amount1 = amount1
    loan_months1 = loan_years1 * 12
    # 计算每月还款本金和利息 for 贷款1
    monthly_principal1 = loan_amount1 / loan_months1
    monthly_interest_rate1 = interest_rate1 / 12
    # 计算还款总额和利息总额 for 贷款1
    payment_total1 = 0
    interest_total1 = 0
    for i in range(loan_months1):
        # 当期应还本金
        current_principal = monthly_principal1
        # 当期应还利息
        current_interest = loan_amount1 * monthly_interest_rate1
        # 更新贷款总额
        loan_amount1 -= current_principal
        # 更新还款总额和利息总额
        payment_total1 += (current_principal + current_interest)
        interest_total1 += current_interest
        # 输出当期还款情况
        current_principal_all.append(current_principal)
        current_interest_all.append(current_interest)
        #print(f'贷款1第{i + 1}个月应还金额为：{(current_principal + current_interest):.2f}元，其中本金为{current_principal:.2f}元，利息为{current_interest:.2f}元')

    
    # 计算贷款总额和贷款月数 for 贷款2
    loan_amount2 = amount2
    loan_months2 = loan_years2 * 12
    # 计算每月还款本金和利息 for 贷款2
    monthly_principal2 = loan_amount2 / loan_months2
    monthly_interest_rate2 = interest_rate2 / 12
    # 计算还款总额和利息总额 for 贷款2
    payment_total2 = 0
    interest_total2 = 0
    for i in range(loan_months2):
        # 当期应还本金
        current_principal = monthly_principal2
        # 当期应还利息
        current_interest = loan_amount2 * monthly_interest_rate2
        # 更新贷款总额
        loan_amount2 -= current_principal
        # 更新还款总额和利息总额
        payment_total2 += (current_principal + current_interest)
        interest_total2 += current_interest
        # 输出当期还款情况
        current_principal_all[i] = current_principal_all[i] + current_principal
        current_interest_all[i] = current_interest_all[i] + current_interest
        #print(f'贷款2第{i + 1}个月应还金额为：{(current_principal + current_interest):.2f}元，其中本金为{current_principal:.2f}元，利息为{current_interest:.2f}元')

    
    # 返回结果
    return (payment_total1 + payment_total2), (interest_total1 + interest_total2)

over_interest = 0
# 测试房贷计算器
def fun(data):
    global over_interest
    # 测试数据
    amount1 = data[0] #商贷
    amount2 = data[1]  #公积金
    interest_rate1 = data[2]  # 商贷年利率
    interest_rate2 = data[3] # 公积金年利率
    loan_years = data[4]       # 贷款年限
    # 计算房贷
    payment_total, interest_total = calculate_house_loan(amount1, amount2, interest_rate1, loan_years, interest_rate2, loan_years)
    # 输出结果

    #print(f'还款总额：{payment_total/10000:.2f}万元')
    #print(f'利息总额：{interest_total/10000:.2f}万元')
    for i in range(loan_years*12):
        if i < 60:
            over_interest = over_interest + current_interest_all[i]
        #if i==0 or i==59:
            #print(f'贷款第{i + 1}个月应还金额为：{(current_principal_all[i] + current_interest_all[i]):.2f}元，其中本金为{current_principal_all[i]:.2f}元，利息为{current_interest_all[i]:.2f}元')
    #print(f'5年利息为{over_interest:.2f}元')
    #print('商贷   |公积金   |年限    |总还款     |总利息     |5年利息')
    print(f'{amount1/10000:.2f} |{amount2/10000:.2f}    |{loan_years}      |{payment_total/10000:.2f}     |{interest_total/10000:.2f}      |{over_interest:.2f}')
    
    
if __name__ == '__main__':
    data =  [1160000,400000,0.041,0.031,20]
    data1 = [1160000,400000,0.041,0.031,30]
    data2 = [1470000,400000,0.041,0.031,30]
    data3 = [760000,800000,0.049,0.03575,30]
    data4 = [1070000,800000,0.049,0.03575,30]
    all_data = [data,data1,data2,data3,data4]
    print('商贷   |公积金   |年限    |总还款     |总利息     |5年利息')
    for i in all_data:
        over_interest = 0
        current_principal_all = []
        current_interest_all = []
        fun(i)
