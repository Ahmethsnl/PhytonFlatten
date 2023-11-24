## Proje 

[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

Big-O gösterimini yazınız.

Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

Average case: Aradığımız sayının ortada olması
Worst case: Aradığımız sayının sonda olması
Best case: Aradığımız sayının dizinin en başında olması.
.



[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

## Çözüm


Insertion Sort Aşamaları:

[2, 22, 27, 16, 18, 6]
[2, 6, 22, 27, 16, 18]
[2, 6, 16, 22, 27, 18]
[2, 6, 16, 18, 22, 27]
[2, 6, 16, 18, 22, 27]
Big-O Gösterimi: O(n^2)

Time Complexity:

Average Case: O(n^2)
Worst Case: O(n^2)
Best Case: O(n) (Ancak genellikle bu durum pek gerçekleşmez)
Selection Sort Aşamaları:

[2, 3, 5, 8, 7, 9, 4, 15, 6]
[2, 3, 5, 8, 7, 9, 4, 15, 6]
[2, 3, 4, 5, 8, 7, 9, 15, 6]
[2, 3, 4, 5, 8, 7, 9, 15, 6]
Not: İlk dört adımı tamamlamak diziyi sıralamaya yeterlidir. Diğer adımlar sıralı kısmın devamını oluşturacaktır.

Average Case: Aradığımız sayının ortada olması - O(n^2)
Worst Case: Aradığımız sayının sonda olması - O(n^2)
Best Case: Aradığımız sayının dizinin en başında olması - O(n^2)
