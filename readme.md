Теоретичний аналіз
Сортування злиттям (Merge Sort)

Часова складність: O(n log n)
Просторова складність: O(n)
Сортування вставками (Insertion Sort)

Часова складність: O(n^2) в найгіршому випадку, O(n) в найкращому випадку
Просторова складність: O(1)
Timsort

Часова складність: O(n log n)
Просторова складність: Залежить від реалізації, зазвичай O(n)
Емпіричні тести
Щоб отримати точні дані про час виконання алгоритмів, використаємо модуль timeit. Напишемо код для кожного алгоритму і порівняємо їх швидкість на різних наборах даних.

Сортування злиттям є дуже ефективним з точки зору часу, але має високу потребу в пам’яті.
Сортування вставками працює швидше на малих масивах і вже відсортованих даних, але швидкість падає на великих масивах.
Timsort поєднує переваги обох підходів, використовуючи сортування вставками на невеликих частинах масиву та сортування злиттям для об’єднання відсортованих частин. Це робить його дуже ефективним і оптимізованим для практичних випадків.
Таким чином, Timsort зазвичай буде найшвидшим і найефективнішим варіантом в більшості реальних сценаріїв, що пояснює його використання в стандартних бібліотеках Python.