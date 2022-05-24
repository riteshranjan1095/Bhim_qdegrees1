def dotask(df1):
    col = ['mobile', 'zone', 'city', 'state', 'Rating', 'Remarks', 'Cleaned_Remarks', 'Categories', 'Sub Categories',
           'NPS CAT', 'Total Nps Score']
    import pandas as pd
    import numpy as np
    import re
    import string
    #     global df_final
    #     df_final = pd.DataFrame(columns=col)

    def clean_text(text):
        delete_dict = {sp_character: '' for sp_character in string.punctuation}
        delete_dict[' '] = ' '
        table = str.maketrans(delete_dict)
        text1 = text.translate(table)

        textArr = text1.split()
        text2 = ' '.join([w for w in textArr if (not w.isdigit() and (not w.isdigit() and len(w) > 3))])
        return text2.lower()

    df1['Remarks'] = df1['Remarks'].astype(str)
    df1['Cleaned_Remarks'] = ''
    df1['Cleaned_Remarks'] = df1['Remarks'].apply(clean_text)
    df1['Categories'] = ''
    df1['Sub Categories'] = ''

    Happy_Customers = ['very good ', 'simple transfer ', 'good', 'easy ', 'good ', 'efficient way ', 'fast app ',
                       'more accessible ', 'better processing ',
                       'very effective ', 'fast ', 'user friendly ', 'best upi ', 'quite efficient ', 'so simple ',
                       'very safe ', 'indian ',
                       'very quickly ', 'best ', 'nice ', 'very satisfied ', 'happy ', 'love ', 'just wonderful ',
                       'super ', 'awesome ', 'best performance ',
                       'excellent ', 'nice app ', 'for pay bill easily ', 'nice service ', 'best customer experience ',
                       'satisfied ', 'better app ',
                       'very nice ', 'excellent ', 'fabulous ', 'awsome ', 'awesome ', 'cool ', 'very good',
                       ' simple transfer', ' easy', ' good', ' efficient way', ' fast app', ' more accessible',
                       ' better processing',
                       ' very effective', ' fast', ' user friendly', ' best upi', ' quite efficient', ' so simple',
                       ' very safe', ' indian',
                       ' very quickly', ' best', ' nice', ' very satisfied', ' happy', ' love', ' just wonderful',
                       ' super', ' awesome', ' best performance',
                       ' excellent', ' nice app', ' for pay bill easily', ' nice service', ' best customer experience',
                       ' satisfied', ' better app',
                       ' very nice', ' excellent', ' fabulous', ' awsome', ' awesome', ' cool']
    Transaction = ['transaction ', 'transition ', 'transection ', 'nfc ', 'nfc', ' transaction', ' transition',
                   ' transection', 'regular payments', 'transfer in my account']
    Recharge = ['recharge ', 'recharging ', ' recharge', ' recharging']
    Comparing = ['works faster than ', 'compare ', 'way better than ', 'better than ', 'googlepay ', 'google pay ',
                 'paytm ', 'phonepay ', 'phone pay ', 'mi ', 'other upi ',
                 'mobikwik ', 'gpay ', 'phonepes ', 'paypal ', ' works faster than', ' compare', ' way better than',
                 ' better than', ' googlepay',
                 ' google pay', ' paytm', ' phonepay', ' phone pay', ' mi', ' other upi', ' mobikwik', ' gpay',
                 ' phonepes', ' paypal']
    Interface = ['interface ', 'inter face ', ' interface', ' inter face', 'very slow ', 'speed ', 'server ',
                 'network issue ', 'low speed', 'servsr ', ' very slow',
                 ' speed', ' server', ' network issue', ' low speed', ' servsr', 'hopeless ', 'pathetic ', 'hate ',
                 'bad app ', 'not good ', 'app not working ', ' hopeless',
                 ' pathetic', ' hate', ' bad app', ' not good', ' app not working']

    # interface, note happy with app and server merged into App interface/UI
    # related to bug, app loggin issue, facing problem in app merged into app loggin issue

    # Server                       = ['very slow ','speed ','server ','network issue ','low speed','servsr ',' very slow',' speed',' server',' network issue',' low speed',' servsr']
    Complaints = ['complaint ', 'fraud ', 'upi pin ', 'complaints ', 'unblock ', 'thing went wrong ', 'disabled ',
                  'complaint ',
                  'fraud ', 'upi pin ', 'complaints ', 'unblock ', 'thing went wrong ', 'disabled ']
    Isses_Not_Solved = ['issue ', 'issues ', 'not resolved ', ' issue', ' issues', ' not resolved']
    Offers_And_Reward = ['reward ', 'discount ', 'offer ', 'rewards ', 'cashback ', 'scratch card ', 'cashbach ',
                         'vouchers ', 'cashbacks ', 'cash back ', 'coupons ',
                         'redeem card ', ' reward', ' discount', ' offer', ' rewards', ' cashback', ' scratch card',
                         ' cashbach', ' vouchers', ' cashbacks', ' cash back', ' coupons',
                         ' redeem card']
    Customer_Service = ['customer care ', 'customer service ', 'customer support ', 'toll free ', 'customers care ',
                        ' customer care', ' customer service', ' customer support',
                        ' toll free', ' customers care']
    Suggestion_For_Improvement = ['add ', 'improve ', 'improvement ', 'improvements ', 'start new ', 'more options ',
                                  'more option ',
                                  'Make better ', 'feedback given by ', 'more update ', 'improvment ',
                                  'more facilities ', 'booking features ', ' add', ' improve', ' improvement',
                                  ' improvements', ' start new', ' more options', ' more option', ' Make better',
                                  ' feedback given by', ' more update', ' improvment',
                                  ' more facilities', ' booking features']
    QR_Code = [' qr', 'qr ']
    Security = ['security ', 'security issues ', ' security', ' security issues', 'secure']
    # Facing_Problem_In_App        = [' can not see',' cannt see',' cant see', 'can not see ','cannt see ','cant see ']
    # Related_to_Bugs              = ['bugs ','bug ','fix it ',' bugs',' bug',' fix it']
    # Not_Happy_With_App           = ['hopeless ','pathetic ','hate ','bad app ','not good ','app not working ',' hopeless',' pathetic',' hate',' bad app',' not good',' app not working']
    Not_Able_To_Login = ['bugs ', 'bug ', 'fix it ', ' bugs', ' bug', ' fix it', ' can not see', ' cannt see',
                         ' cant see', 'can not see ', 'cannt see ', 'cant see ', 'login ', 'log in ', 'sign in ',
                         'signin ', 'sim ', 'late ', 'verfication ', ' login', ' log in', ' sign in', ' signin', ' sim',
                         ' late', ' verfication', 'password']
    IPO = ['ipo ', ' ipo']

    for i in range(0, len(df1.Cleaned_Remarks)):
        if any(word in df1.Cleaned_Remarks[i] for word in Happy_Customers):
            df1['Categories'][i] = 'Happy customers'

        elif any(word in df1.Cleaned_Remarks[i] for word in Transaction):
            df1['Categories'][i] = 'Transaction related issue'

        elif any(word in df1.Cleaned_Remarks[i] for word in Recharge):
            df1['Categories'][i] = 'Prepaid recharge/Billing'

        elif any(word in df1.Cleaned_Remarks[i] for word in Comparing):
            df1['Categories'][i] = 'Comparision with other brands'

        elif any(word in df1.Cleaned_Remarks[i] for word in Interface):
            df1['Categories'][i] = 'App interface/UI'

        #     elif any(word in df.Cleaned_Remarks[i] for word in Server):
        #         df['Categories'][i] = 'Server'

        elif any(word in df1.Cleaned_Remarks[i] for word in Complaints):
            df1['Categories'][i] = 'Complaints'

        elif any(word in df1.Cleaned_Remarks[i] for word in Isses_Not_Solved):
            df1['Categories'][i] = 'Issues Not resolved'

        elif any(word in df1.Cleaned_Remarks[i] for word in Offers_And_Reward):
            df1['Categories'][i] = 'Offers & Rewards'

        elif any(word in df1.Cleaned_Remarks[i] for word in Customer_Service):
            df1['Categories'][i] = 'Customer Service'

        elif any(word in df1.Cleaned_Remarks[i] for word in Suggestion_For_Improvement):
            df1['Categories'][i] = 'Suggestion for improvement'

        elif any(word in df1.Cleaned_Remarks[i] for word in QR_Code):
            df1['Categories'][i] = 'QR Code'

        elif any(word in df1.Cleaned_Remarks[i] for word in Security):
            df1['Categories'][i] = 'App security'

        #     elif any(word in df.Cleaned_Remarks[i] for word in Facing_Problem_In_App):
        #         df['Categories'][i] = 'Facing Problem In App'

        #     elif any(word in df.Cleaned_Remarks[i] for word in Related_to_Bugs):
        #         df['Categories'][i] = 'Related to Bugs'

        #     elif any(word in df.Cleaned_Remarks[i] for word in Not_Happy_With_App):
        #         df['Categories'][i] = 'Not Happy With App'

        elif any(word in df1.Cleaned_Remarks[i] for word in Not_Able_To_Login):
            df1['Categories'][i] = 'App login issue'

        elif any(word in df1.Cleaned_Remarks[i] for word in IPO):
            df1['Categories'][i] = 'IPO'

    Transaction = df1[df1.Categories == 'Transaction related issue']
    Transaction = Transaction.reset_index()
    Transaction = Transaction.drop(['index'], axis=1)

    Not_able_to_do_transcation = ['mobile number has been changed', 'transfer', 'payement not', 'payment not ',
                                  'processed',
                                  'can not debited', 'cant debited', 'can not debited',
                                  'mobile number has been changed ', 'transfer ', 'payement not ', 'payment not ',
                                  'processed ',
                                  'can not debited ', 'cant debited ', 'can not debited ']
    wrong_transaction = ['wrong transaction', 'mistakly wrong transaction', 'wrong transaction ',
                         'mistakly wrong transaction ']
    money_dedected = ['detected', 'deduct', 'deducted', 'detected ', 'deduct ', 'deducted ']
    transaction_limit = ['limit', 'trasaction limit', 'limit ', 'trasaction limit ', 'limitation', ]
    payment_failure = ['failure', 'fails', ' payment failure', ' payment fails', 'failure ', 'fails ',
                       'payment failure ', 'payment fails ']
    not_refund = [' not refund', ' refund', ' refunding', ' refunds', 'not refund ', 'refund ', 'refunding ',
                  'refunds ']
    error = [' error', ' errors', 'error ', 'errors ']
    other_issue = [' issue', ' other issue', ' issues', 'issue ', 'other issue ', 'issues ']
    pending = [' pending', 'pending ']
    rejection_in_payment = [' rejection', 'rejection ']
    transaction_details_required = ['details', 'history', 'account statement']
    otp_requirement_for_every_transaction = ['otp']

    for i in range(0, len(Transaction.Cleaned_Remarks)):
        if any(word in Transaction.Cleaned_Remarks[i] for word in Not_able_to_do_transcation):
            Transaction['Sub Categories'][i] = 'Not able to do transcation'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in wrong_transaction):
            Transaction['Sub Categories'][i] = 'Wrong transaction'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in money_dedected):
            Transaction['Sub Categories'][i] = 'Money deducted'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in transaction_limit):
            Transaction['Sub Categories'][i] = 'Transaction limit'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in payment_failure):
            Transaction['Sub Categories'][i] = 'Payment failure'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in not_refund):
            Transaction['Sub Categories'][i] = 'Not refund'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in error):
            Transaction['Sub Categories'][i] = 'Error'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in other_issue):
            Transaction['Sub Categories'][i] = 'Other issue'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in pending):
            Transaction['Sub Categories'][i] = 'Pending'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in rejection_in_payment):
            Transaction['Sub Categories'][i] = 'Rejection in payment'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in transaction_details_required):
            Transaction['Sub Categories'][i] = 'Transaction details required'

        elif any(word in Transaction.Cleaned_Remarks[i] for word in otp_requirement_for_every_transaction):
            Transaction['Sub Categories'][i] = 'Otp requirement for every transaction'

    Happy_Customer = df1[df1.Categories == 'Happy customers']
    Happy_Customer = Happy_Customer.reset_index()
    Happy_Customer = Happy_Customer.drop(['index'], axis=1)

    cashback = ['cashback', 'offer', 'reward']
    interface = ['interface']
    security = ['secuity', 'secure']
    trust_bcz_gov_support = ['indian', 'govt', 'government']
    userfriendlyapp = ['easy', 'user friendly', 'app', 'application']

    for i in range(0, len(Happy_Customer.Cleaned_Remarks)):
        if any(word in Happy_Customer.Cleaned_Remarks[i] for word in cashback):
            Happy_Customer['Sub Categories'][i] = 'Cashback/offer Related'

        elif any(word in Happy_Customer.Cleaned_Remarks[i] for word in interface):
            Happy_Customer['Sub Categories'][i] = 'Interface'

        elif any(word in Happy_Customer.Cleaned_Remarks[i] for word in security):
            Happy_Customer['Sub Categories'][i] = 'Security'

        elif any(word in Happy_Customer.Cleaned_Remarks[i] for word in trust_bcz_gov_support):
            Happy_Customer['Sub Categories'][i] = 'Trust Because of Govt Support'

        elif any(word in Happy_Customer.Cleaned_Remarks[i] for word in userfriendlyapp):
            Happy_Customer['Sub Categories'][i] = 'User Friendly App'

    Happy_Customer['Sub Categories'] = Happy_Customer['Sub Categories'].replace(np.nan, 'Generic Comment')

    Comparing_ = df1[df1.Categories == 'Comparision with other brands']
    Comparing_ = Comparing_.reset_index()
    # Happy_Customer['Sentiment'] = "Positive"
    Comparing_ = Comparing_.drop(['index'], axis=1)

    comparing_with_google_pay = [' google pay', 'google pay ', ' gpay', ' googlepay', 'gpay ']
    comparing_with_phone_pay = [' phone pay', 'phone pay ']
    comparing_with_paytm = [' paytm', 'paytm ']

    for i in range(0, len(Comparing_.Cleaned_Remarks)):
        if any(word in Comparing_.Cleaned_Remarks[i] for word in comparing_with_google_pay):
            Comparing_['Sub Categories'][i] = 'Comparing with google pay'

        elif any(word in Comparing_.Cleaned_Remarks[i] for word in comparing_with_phone_pay):
            Comparing_['Sub Categories'][i] = 'Comparing with phone pay'

        elif any(word in Happy_Customer.Cleaned_Remarks[i] for word in comparing_with_paytm):
            Comparing_['Sub Categories'][i] = 'Comparing with paytm'

    Offers_And_Reward_ = df1[df1.Categories == 'Offers & Rewards']
    Offers_And_Reward_ = Offers_And_Reward_.reset_index()
    # Happy_Customer['Sentiment'] = "Positive"
    Offers_And_Reward_ = Offers_And_Reward_.drop(['index'], axis=1)

    Customers_wants_more_offer = ['should be', 'add', 'provide', 'lacks', 'need more', 'give']
    more_transaction_more_offer = ['every', 'transaction']

    for i in range(0, len(Offers_And_Reward_.Cleaned_Remarks)):
        if any(word in Offers_And_Reward_.Cleaned_Remarks[i] for word in Customers_wants_more_offer):
            Offers_And_Reward_['Sub Categories'][i] = 'Customers wants more offer'

        elif any(word in Offers_And_Reward_.Cleaned_Remarks[i] for word in more_transaction_more_offer):
            Offers_And_Reward_['Sub Categories'][i] = 'More transaction more offer'

    Prepaid_recharge_Billing = df1[df1.Categories == 'Prepaid recharge/Billing']
    Prepaid_recharge_Billing = Prepaid_recharge_Billing.reset_index()
    Prepaid_recharge_Billing = Prepaid_recharge_Billing.drop(['index'], axis=1)

    App_interface_UI = df1[df1.Categories == 'App interface/UI']
    App_interface_UI = App_interface_UI.reset_index()
    App_interface_UI = App_interface_UI.drop(['index'], axis=1)

    Complaints = df1[df1.Categories == 'Complaints']
    Complaints = Complaints.reset_index()
    Complaints = Complaints.drop(['index'], axis=1)

    Issues_Not_resolved = df1[df1.Categories == 'Issues Not resolved']
    Issues_Not_resolved = Issues_Not_resolved.reset_index()
    Issues_Not_resolved = Issues_Not_resolved.drop(['index'], axis=1)

    Customer_Service = df1[df1.Categories == 'Customer Service']
    Customer_Service = Customer_Service.reset_index()
    Customer_Service = Customer_Service.drop(['index'], axis=1)

    Suggestion_for_improvement = df1[df1.Categories == 'Suggestion for improvement']
    Suggestion_for_improvement = Suggestion_for_improvement.reset_index()
    Suggestion_for_improvement = Suggestion_for_improvement.drop(['index'], axis=1)

    QR_Code = df1[df1.Categories == 'QR Code']
    QR_Code = QR_Code.reset_index()
    QR_Code = QR_Code.drop(['index'], axis=1)

    App_security = df1[df1.Categories == 'App security']

    App_security = App_security.reset_index()
    App_security = App_security.drop(['index'], axis=1)

    App_login_issue = df1[df1.Categories == 'App login issue']
    App_login_issue = App_login_issue.reset_index()
    App_login_issue = App_login_issue.drop(['index'], axis=1)

    Unproductive = df1[df1.Categories == '']
    Unproductive = Unproductive.reset_index()
    Unproductive = Unproductive.drop(['index'], axis=1)
    #         display(Unproductive)

    IPO = df1[df1.Categories == 'IPO']
    IPO = IPO.reset_index()
    IPO = IPO.drop(['index'], axis=1)

    df_ = pd.concat(
        [Transaction, Comparing_, Happy_Customer, Offers_And_Reward_, Prepaid_recharge_Billing, App_interface_UI,
         Complaints, Issues_Not_resolved, QR_Code, Suggestion_for_improvement, App_security, App_login_issue, IPO,
         Unproductive]).drop_duplicates().reset_index(drop=True)
    #         df_['Categories'] = df_['Categories'].replace('', np.nan, regex=True)
    #         df_['Categories'] = df_['Categories'].replace(np.nan, 'Unproductive Comment')
    df_ = df_.sample(frac=1).reset_index(drop=True)
    df_['Categories'] = df_['Categories'].replace('', np.nan, regex=True)
    df_['Categories'] = df_['Categories'].replace(np.nan, 'Unproductive comment')
    df_['Sub Categories'] = df_['Sub Categories'].replace('', np.nan, regex=True)
    df_['Sub Categories'] = df_['Sub Categories'].replace(np.nan, 'Not available')
    df_['NPS CAT'] = ""
    df_['Rating'] = df_['Rating'].astype(int)
    detractor = df_[df_['Rating'] < 7]
    detractor['NPS CAT'] = "Detractor"
    promoter = df_[df_['Rating'] > 8]
    promoter['NPS CAT'] = "Promoter"
    passive = df_[(df_['Rating'] < 9) & (df_['Rating'] > 6)]
    passive['NPS CAT'] = "Passive"
    df_1 = pd.concat([detractor, promoter, passive])
    Promoter_count = len(df_1[df_1['NPS CAT'] == 'Promoter'])
    Passive_count = len(df_1[df_1['NPS CAT'] == 'Passive'])
    Detractor_count = len(df_1[df_1['NPS CAT'] == 'Detractor'])
    df_1['Total Nps Score'] = ''
    df_1['Total Nps Score'] = (Promoter_count - Detractor_count) / (
            Promoter_count + Passive_count + Detractor_count) * 100
    col = ['mobile', 'zone', 'city', 'state', 'Rating', 'Remarks', 'Cleaned_Remarks', 'Categories', 'Sub Categories',
           'NPS CAT', 'Total Nps Score']
    global df_2
    df_2 = pd.DataFrame(columns=col)

    for i in df_1['Categories'].unique():
        j = i
        j = df_1[df_1['Categories'] == i]
        detractor = j[j['Rating'] < 7]
        detractor['NPS CAT'] = "Detractor"
        promoter = j[j['Rating'] > 8]
        promoter['NPS CAT'] = "Promoter"
        passive = j[(j['Rating'] < 9) & (j['Rating'] > 6)]
        passive['NPS CAT'] = "Passive"

        frames = [detractor, promoter, passive]
        a = pd.concat(frames)
        Promoter_count = len(a[a['NPS CAT'] == 'Promoter'])
        Passive_count = len(a[a['NPS CAT'] == 'Passive'])
        Detractor_count = len(a[a['NPS CAT'] == 'Detractor'])

        a['Total Nps Score Cat Wise'] = ''
        a['Total Nps Score Cat Wise'] = (Promoter_count - Detractor_count) / (Promoter_count + Passive_count
                                                                              + Detractor_count) * 100
        frames = [df_2, a]
        df_2 = pd.concat(frames)
    #         global data
    #         data = df_final.append(df_2)

    # df_2.to_excel(r'D:\Ritesh_2022\Bhim\Bhim_model_based_approach\testing.xlsx')
    return df_2