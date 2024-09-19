from utils.api import GoogleMapsApi
from utils.checking import Checking
import allure

@allure.epic('Test new place')
class TestNewPlace:
    """Класс содержащий тест по работе с локацией"""

    @allure.description('Test create, read, update, delete new place')
    def test_new_place(self):
        """Тест по созданию, чтению, изменению и удалению новой локации"""

        print("Метод POST")
        result_post = GoogleMapsApi.create_new_place()  # вызов метода по созданию новой локации
        check_post = result_post.json()
        place_id = check_post.get("place_id")  # получения place_id для метода GET
        Checking.check_status_code(result_post, 200)
        Checking.check_json_fields(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')
        Checking.check_json_search_word_in_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                                'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', "29, side layout, cohen 09")
        Checking.check_json_search_word_in_value(result_get, 'address', 'cohen')

        print("Метод PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)  # изменение данных о созданной локации
        Checking.check_status_code(result_put, 200)
        Checking.check_json_fields(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')
        Checking.check_json_search_word_in_value(result_put, 'msg', 'updated')

        print("Метод GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 200)
        Checking.check_json_fields(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                                'types', 'website', 'language'])
        Checking.check_json_value(result_get, 'address', "100 Lenina street, RU")
        Checking.check_json_search_word_in_value(result_get, 'address', 'Lenina')

        print("Метод DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)  # удаление данных о созданной локации
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_fields(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')
        Checking.check_json_search_word_in_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)  # отправка метода Get
        Checking.check_status_code(result_get, 404)
        Checking.check_json_fields(result_get, ['msg'])
        Checking.check_json_value(result_get, 'msg', "Get operation failed, looks "
                                                     "like place_id  doesn't exists")
        Checking.check_json_search_word_in_value(result_get, 'msg', 'failed')

        print('Тестирование создания, чтения, изменения и удаления новой локации прошло успешно!')
