    Домашняя работа "Права доступа".
Создана группа «Модератор продуктов».
У модели продукта добавлено право на отмену публикации продукта.
Для группы «Модератор продуктов» настроено право на отмену публикации продукта.
Для группы «Модератор продуктов» настроено право на удаление любого продукта.
Проверяется наличие прав у пользователя при попытке отменить публикацию или удалить продукт.
Приложена фикстура с группами или реализована команда для заполнения групп с настроенными правами в БД.
 Владельцы продуктов
Добавлено поле владельца к модели продукта.
Поле владельца связано с моделью пользователя через 
ForeignKey
.
При создании нового продукта поле 
owner
 автоматически заполняется текущим авторизованным пользователем.
Реализована проверка прав доступа в представлениях для редактирования и удаления продуктов, чтобы только владелец мог выполнять эти действия.
При запросе удаления проверяется дополнительно наличие группы модератора у пользователя.
