import requests
import pandas as pd
import requests
import random 
import string
import numpy as np

class client:
    def __init__(self,api_key,secret_key,base_url="https://www.marketanalyst.ai"):

        self.api_key = api_key
        self.secret_key = secret_key
        self.base_url = base_url

        self.N = 8

    def Getallsecurities(self):
        security_url = self.base_url + "/api_get_security"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(security_url, data=payload)
        security_data = response.json()
        if "data" not in security_data:
            return "api key or secret key is invalid"
        security_data = security_data['data']
        return pd.DataFrame.from_dict(security_data)

    def getallcategory(self):
        category_url = self.base_url + "/api_get_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(category_url, data=payload)
        category_data = response.json()
        if "data" not in category_data:
            return "api key or secret key is invalid"
        category_data = category_data['data']
        return pd.DataFrame.from_dict(category_data)

    def getallsubcategory(self,category_type):
        category_id = self.get_category_id(category_type)
        if type(category_id) != int:
            return category_id
        exchange_url = self.base_url + "/api_get_exchange"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,'category_id':category_id}
        response = requests.post(exchange_url, data=payload)
        exchange_data = response.json()
        if "data" not in exchange_data:
            return "api key or secret key is invalid"
        exchange_data = exchange_data['data']
        return pd.DataFrame.from_dict(exchange_data)

    def getallportfolio(self):
        portfolio_url = self.base_url + "/api_get_portfolio"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(portfolio_url, data=payload)
        portfolio_data = response.json()
        if "data" not in portfolio_data:
            return "api key or secret key is invalid"
        portfolio_data = portfolio_data['data']
        return pd.DataFrame.from_dict(portfolio_data)

    def getallindicator(self):
        indicator_url = self.base_url + "/api_get_indicator_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(indicator_url, data=payload)
        indicator_data = response.json()
        if "data" not in indicator_data:
            return "api key or secret key is invalid"
        indicator_data = indicator_data['data']
        return pd.DataFrame.from_dict(indicator_data)

    def getallsubindicator(self,indicator_type):
        indicator_id = self.get_indicator_id(indicator_type)
        if type(indicator_id) != int:
            return indicator_id
        sub_indicator_url = self.base_url + "/api_get_indicator_sub_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,"indicator_category_id":indicator_id}
        response = requests.post(sub_indicator_url, data=payload)
        sub_indicator_data = response.json()
        if "data" not in sub_indicator_data:
            return "api key or secret key is invalid"
        sub_indicator_data = sub_indicator_data['data']
        return pd.DataFrame.from_dict(sub_indicator_data)

    def get_indicator_id(self,indicator_type):
        indicator_indicator_url = self.base_url + "/api_get_indicator_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(indicator_indicator_url, data=payload)
        indicator_indicator_data = response.json()
        if "data" not in indicator_indicator_data:
            return "api key or secret key is invalid"
        indicator_indicator_data = indicator_indicator_data['data']
        for indicator in indicator_indicator_data:
            if indicator["title"] == indicator_type:
                return int(indicator["id"])
        return "this indicator does not exsist"

    def get_indicator_sub_id(self,indicator_id,sub_indicator_type):
        sub_indicator_type_url = self.base_url + "/api_get_indicator_sub_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,'indicator_category_id': indicator_id}
        response = requests.post(sub_indicator_type_url, data=payload)
        sub_indicator_indicator_data = response.json()
        if "data" not in sub_indicator_indicator_data:
            return "api key or secret key is invalid"
        sub_indicator_indicator_data = sub_indicator_indicator_data['data']
        for sub_indicator in sub_indicator_indicator_data:
            if sub_indicator["title"] == sub_indicator_type:
                return int(sub_indicator["id"])
        return "this sub indicator does not exsist"
    
    def get_security_id(self,security_string):
        security_url = self.base_url + "/api_get_security"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(security_url, data=payload)
        security_data = response.json()
        if "data" not in security_data:
            return "api key or secret key is invalid"
        security_data = security_data['data']
        for security in security_data:
            if security["title"] == security_string:
                return int(security["id"])
        return "this security does not exsist"

    def get_category_id(self,category_type):
        category_url = self.base_url + "/api_get_category"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        response = requests.post(category_url, data=payload)
        category_data = response.json()
        if "data" not in category_data:
            return "api key or secret key is invalid"
        category_data = category_data["data"]
        for category in category_data:
            if category["title"] == category_type:
                return int(category["id"])
        return "this security does not exsist"

    def download_data(self,security_exchange,start_date,end_date,indicator_type,sub_indicator_type):
        download_name = ''.join(random.choices(string.ascii_uppercase +string.digits, k = self.N))
        indicator_id = self.get_indicator_id(indicator_type)
        if type(indicator_id) != int:
            return indicator_id
        sub_indicator_id = self.get_indicator_sub_id(indicator_id,sub_indicator_type)
        if type(sub_indicator_id) != int:
            return sub_indicator_id
        security_id = self.get_security_id(security_exchange)
        if type(security_id) != int:
            return security_id
        criteria_url = self.base_url + "/api_my_download"
        payload = {
            "api_key":self.api_key,
            "secret_key":self.secret_key,
            "time_period":"{'from_date':'" + str(start_date) + "','to_date':'" + str(end_date) + "'}",
            "download_name":download_name,
            "security":security_id,
            "indicator_category":indicator_id,
            "indicator_sub_category":sub_indicator_id,
            "formate":"json"
        }
        response = requests.post(criteria_url, data=payload)
        criteria_list_url = self.base_url + "/api_criteria_list"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        criteria_list_response = requests.post(criteria_list_url, data=payload)
        criteria_list_data = criteria_list_response.json()["data"]
        for temp_criteria in criteria_list_data:
            if temp_criteria["name"] == download_name:
                criteria_id = temp_criteria["id"]
        criteria_download_url =  self.base_url + "/api_my_criteria"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,'criteria_id':criteria_id}
        criteria_download_response = requests.post(criteria_download_url, data=payload)
        return pd.DataFrame.from_dict(criteria_download_response.json())

    def get_close_price(self,security_exchange,start_date,end_date,indicator_type,sub_indicator_type,interval):
        df = self.download_data(security_exchange,start_date,end_date,indicator_type,sub_indicator_type)
        df1 = df[df["indicator"] == "D_EODCLOSE_EXT_1"].copy()
        df1['ma'] = df1['value'].rolling(interval).mean()
        return df1

    def download_data_with_category(self,category_type,exchange_type,start_date,end_date,indicator_type,sub_indicator_type):
        download_name = ''.join(random.choices(string.ascii_uppercase +string.digits, k = self.N))
        indicator_id = self.get_indicator_id(indicator_type)
        if type(indicator_id) != int:
            return indicator_id
        sub_indicator_id = self.get_indicator_sub_id(indicator_id,sub_indicator_type)
        if type(sub_indicator_id) != int:
            return sub_indicator_id
        category_id = self.get_category_id(category_type)
        if type(category_id) != int:
            return category_id
        criteria_url = self.base_url + "/api_my_download"
        payload = {
            "api_key":self.api_key,
            "secret_key":self.secret_key,
            "time_period":"{'from_date':'" + str(start_date) + "','to_date':'" + str(end_date) + "'}",
            "download_name":download_name,
            "indicator_category":indicator_id,
            "indicator_sub_category":sub_indicator_id,
            "formate":"json",
            "category":category_id,
            "exchange":exchange_type
        }
        response = requests.post(criteria_url, data=payload)
        criteria_list_url = self.base_url + "/api_criteria_list"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        criteria_list_response = requests.post(criteria_list_url, data=payload)
        criteria_list_data = criteria_list_response.json()["data"]
        for temp_criteria in criteria_list_data:
            if temp_criteria["name"] == download_name:
                criteria_id = temp_criteria["id"]
        criteria_download_url =  self.base_url + "/api_my_criteria"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,'criteria_id':criteria_id}
        criteria_download_response = requests.post(criteria_download_url, data=payload)
        return pd.DataFrame.from_dict(criteria_download_response.json())

    def getdata(self,security_exchange,start_date,end_date,indicator_type,sub_indicator_type):
        download_name = ''.join(random.choices(string.ascii_uppercase +string.digits, k = self.N))
        indicator_id = self.get_indicator_id(indicator_type)
        if type(indicator_id) != int:
            return indicator_id
        sub_indicator_id = self.get_indicator_sub_id(indicator_id,sub_indicator_type)
        if type(sub_indicator_id) != int:
            return sub_indicator_id
        security_id_list = []
        for security in security_exchange:
            security_id = self.get_security_id(security)
            if type(security_id) != int:
                return security_id
            security_id_list.append(str(security_id))
        criteria_url = self.base_url + "/api_my_download"
        payload = {
            "api_key":self.api_key,
            "secret_key":self.secret_key,
            "time_period":"{'from_date':'" + str(start_date) + "','to_date':'" + str(end_date) + "'}",
            "download_name":download_name,
            "security":",".join(security_id_list),
            "indicator_category":indicator_id,
            "indicator_sub_category":sub_indicator_id,
            "formate":"json"
        }
        response = requests.post(criteria_url, data=payload)
        criteria_list_url = self.base_url + "/api_criteria_list"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key}
        criteria_list_response = requests.post(criteria_list_url, data=payload)
        criteria_list_data = criteria_list_response.json()["data"]
        for temp_criteria in criteria_list_data:
            if temp_criteria["name"] == download_name:
                criteria_id = temp_criteria["id"]
        criteria_download_url =  self.base_url + "/api_my_criteria"
        payload = {'api_key':self.api_key,'secret_key':self.secret_key,'criteria_id':criteria_id}
        criteria_download_response = requests.post(criteria_download_url, data=payload)
        return pd.DataFrame.from_dict(criteria_download_response.json())

    def getOHLCVData(self,security_exchange,start_date,end_date,indicator_type,sub_indicator_type):
        df = self.getdata(security_exchange,start_date,end_date,indicator_type,sub_indicator_type)
        return_df = pd.DataFrame(columns = ['datetime','exchange','security','open','low','high','close','volume'])
        for group_name, group_df in df.groupby("s"):
            ticker_df = group_df.copy()
            for ticker_group_name, ticker_group_df in ticker_df.groupby("d"):
                datetime_df = ticker_group_df.copy()
                open_price = datetime_df[datetime_df["i"] == "D_EODOPEN_EXT_1"]
                if open_price.empty == False:
                    open_value = open_price["v"].unique()[0]
                else:
                    open_value = np.nan
                low_price = datetime_df[datetime_df["i"] == "D_EODLOW_EXT_1"]
                if low_price.empty == False:
                    low_value = low_price["v"].unique()[0]
                else:
                    low_value = np.nan
                high_price = datetime_df[datetime_df["i"] == "D_EODHIGH_EXT_1"]
                if high_price.empty == False:
                    high_value = high_price["v"].unique()[0]
                else:
                    high_value = np.nan
                volume = datetime_df[datetime_df["i"] == "D_EODVOL_EXT_1"]
                if volume.empty == False:
                    volume_value = volume["v"].unique()[0]
                else:
                    volume_value = np.nan
                close_price = datetime_df[datetime_df["i"] == "D_EODCLOSE_EXT_1"]
                if close_price.empty == False:
                    close_value = close_price["v"].unique()[0]
                else:
                    close_value = np.nan
                return_entry = [datetime_df['d'].unique()[0],datetime_df['e'].unique()[0],datetime_df['s'].unique()[0],open_value,low_value,high_value,close_value,volume_value]
                return_df.loc[len(return_df)] = return_entry
        return return_df