import pytest
from requests import Response
import allure
from utils.gapi import  Google_maps_api
from utils.checking import Checking
import json
"""Создание, изменение и удаление новой локации"""
@allure.epic("Test_create_places")
class Test_create_places():
    @allure.description("Test create, update, delete new place")
    def test_create_place(self):
        print("Метод Post")
        result_post = Google_maps_api.Create_new_place() 
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        token = json.loads(result_post.text)
        print(list(token))
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_status_code(result_post, 200)
        Checking.check_json_value(result_post, 'status', 'OK')
        
        print("Метод GET")
        result_get = Google_maps_api.Get_new_place(place_id)
        check_get = result_get.json()
        Checking.check_status_code(result_get, 200)
        token = json.loads(result_get.text)
        print(list(token))
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', '29, side layout, cohen 09')
        # 29, side layout, cohen 09
        
        print("Метод PUT")
        result_put = Google_maps_api.Put_new_place(place_id)
        check_put = result_put.json()
        Checking.check_status_code(result_put, 200)
        token = json.loads(result_put.text)
        print(list(token))
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        
        print("Метод GET PUT")
        result_get = Google_maps_api.Get_new_place(place_id)
        check_get = result_get.json()
        Checking.check_status_code(result_get, 200)
        Checking.check_json_value(result_get, 'address', '190 Zhukovskogonina street, RU')
    
        print("Метод Delete")
        result_delete = Google_maps_api.Delete_new_place(place_id)
        check_delete = result_delete.json()
        Checking.check_status_code(result_delete, 200)
        token = json.loads(result_delete.text)
        print(list(token))
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status' , 'OK')
        
        print("Метод GET Delete")
        result_get = Google_maps_api.Get_new_place(place_id)
        check_get = result_get.json()
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        # Checking.check_json_value(result_get, 'msg', "Delete operation failed, looks like the place_id doesn't exists") 
        Checking.check_json_search_word_in_value(result_get, 'msg', "failed") 
        