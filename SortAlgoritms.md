## Proje 1

[22,27,16,2,18,6] -> Insertion Sort

Yukarı verilen dizinin sort türüne göre aşamalarını yazınız.

Big-O gösterimini yazınız.

Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer? Yazınız

Average case: Aradığımız sayının ortada olması
Worst case: Aradığımız sayının sonda olması
Best case: Aradığımız sayının dizinin en başında olması.
.



[7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

## Çözüm 1


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

## Proje 2
[16,21,11,8,12,22] -> Merge Sort

Yukarıdaki dizinin sort türüne göre aşamalarını yazınız.
Big-O gösterimini yazınız.

Average Case: Aradığımız sayının ortada olması - O(n^2)

## Çözüm 1

Merge Sort Aşamaları:

[16, 21, 11, 8, 12, 22]

(Diziyi ikiye böldük)
[16, 21, 11, 8, 12, 22]

(Her bir alt listeyi ayrı ayrı sıraladık)
[16, 21, 8, 11, 12, 22]

(Her iki sıralı alt listeyi birleştirdik)
[8, 11, 12, 16, 21, 22]

(Her iki sıralı alt listeyi birleştirdik)
Big-O Gösterimi: O(n log n)

Merge Sort, ayrıştırma (divide) ve birleştirme (merge) adımlarıyla çalışır. Bu nedenle, her ayrıştırma ve birleştirme adımı logaritmik zaman alır. Toplam karmaşıklık O(n log n) olur.


Worst Case: Aradığımız sayının sonda olması - O(n^2)
Best Case: Aradığımız sayının dizinin en başında olması - O(n^2)

## Proje 3

[7, 5, 1, 8, 3, 6, 0, 9, 4, 2] dizisinin Binary-Search-Tree aşamalarını yazınız.

Örnek: root x'dir. root'un sağından y bulunur. Solunda z bulunur vb.

## Çözüm 3

Binary Search Tree (BST) aşamaları şu şekildedir:

7 -> Root
5 -> Root'un solunda
1 -> 5'in solunda
0 -> 1'in solunda
3 -> 1'in sağından 5'in soluna
2 -> 3'ün solunda
4 -> 3'ün sağından 5'in soluna
8 -> Root'un sağına
6 -> 8'in solunda
9 -> 8'in sağından Root'un sağına
4 -> 9'un sağından 8'in sağına
