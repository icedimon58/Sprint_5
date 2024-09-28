# Sprint_5
Тестирование сайта https://stellarburgers.nomoreparties.site

Файл test_registration производит тестирование регистрации на сайте:
	test_registration_postive - положителное тестирование регистрации
	test_registration_wrong_password - негативное тестирование при неправильном пароле
		
Файл test_autorisation_method производит тестирование авторизацию на сайте различными методами:	
	test_login_from_login_button - авторизация через кнопку авторизации
	test_login_from_cabinet - авторизация через личный кабинет
	test_login_from_restore_password_button - авторизация через восстановление пароля
	
Файл test_different_path производит тестирование переходов по странице
	test_path_to_cabinet - переход в личный кабинет
	test_path_to_constructor_from_cabinet - переход в конструктор из личного кабинета
	test_path_to_logo_from_cabinet - переход из кабинета по клику на логотипе
	test_exit_from_account - выход из аккаунта
	test_stuffing_button - тест выбора в конструкоре меню "Начинки"
	test_souce_button - тест выбора в конструкоре меню "Соусы"
	test_bread_button - тест выбора в конструкоре меню "Булки"

В файле Locators содержатся локаторы и ссылки на различные страницы
В файле helps содержатся дополнительные функции
	generate_password - функция генерации пароля
	generate_wrong_password - функция генерации неправильного пароля
	generate_email - функция генерации электроннгной почты	
	get_autorisation - функция авторизации
	get_autorisation_on_site_from_login_button - функция авторизации через кнопку авторизации