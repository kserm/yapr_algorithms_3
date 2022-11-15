# Recursions and sorts
links to tasks list at yandex.contest.ru:

[recursions and sorts](https://contest.yandex.ru/contest/24734/problems/)

[final tasks](https://contest.yandex.ru/contest/24735/problems/)

_________________________________________________

<details>
<summary>
Parentheses generator (<a href="1_parenthesis_generator.py">1_parenthesis_generator.py</a>) 
</summary>
Generate all correct bracket sequences of length 2n in alphabetical order —– the alphabet consists of ( and ) and the opening bracket comes before the closing bracket.

Input example:
|Input|Description|
|:-|:-|
|`3`|input number n|
|`((()))`|output|
|`(()())`|output|
|`(())()`|output|
|`()(())`|output|
|`()()()`|output|

</details>

_________________________________________________

<details>
<summary>
Combinations (<a href="2_combinations.py">2_combinations.py</a>) 
</summary>
On the keyboard of old mobile phones, each digit corresponded to several letters. More or less like this:

* 2:'abc',
* 3:'def',
* 4:'ghi',
* 5:'jkl',
* 6:'mno',
* 7:'pqrs',
* 8:'tuv',
* 9:'wxyz'

You know in what order the phone buttons were pressed, excluding repetitions. Type all combinations of letters that can be typed in such a sequence of clicks.

Input example:
|Input|Description|
|:-|:-|
|`23`|input string of numbers from 2 to 9|
|`ad ae af bd be bf cd ce cf`|output|
|||
|`92`|input string of numbers from 2 to 9|
|`wa wb wc xa xb xc ya yb yc za zb zc`|output|

</details>

_________________________________________________

<details>
<summary>
Subsequence (<a href="3_subsequence.py">3_subsequence.py</a>) 
</summary>
Given 2 strings, and you need to understand whether the first of them is a subsequence of the second.

Input example:
|Input|Description|
|:-|:-|
|`abc`|first string|
|`ahbgdcu`|second string|
|`True`|output|
|||
|`abcp`|first string|
|`ahpc`|second string|
|`False`|output|

</details>

_________________________________________________

<details>
<summary>
Cookies (<a href="4_cookies.py">4_cookies.py</a>) 
</summary>
Cookies can be of different sizes. And every child has a greed factor - the minimum size of a cookie that he will take. We need to find out how many children will be satisfied in the best case, when they perform optimally.

Each child can take no more than one cookie.

Input example:
|Input|Description|
|:-|:-|
|`2`|amount of children|
|`1 2`|greed factor for each child|
|`3`|amount of cookies|
|`2 1 3`|size of cookie|
|`2`|output|

</details>

_________________________________________________

<details>
<summary>
Buying houses (<a href="5_house_buying.py">5_house_buying.py</a>) 
</summary>
There are n advertisements for sale, where the cost of each house is indicated. There are k money. Determine the maximum number of houses that can be purchased with this money.

Input example:
|Input|Description|
|:-|:-|
|`3 300`|number of houses and amount of money|
|`999 999 999`|houses prices|
|`0`|output|
|||
|`3 1000`|number of houses and amount of money|
|`350 999 200`|houses prices|
|`2`|output|

</details>

_________________________________________________

<details>
<summary>
Perimeter of a triangle (<a href="6_triangle_perimeter.py">6_triangle_perimeter.py</a>) 
</summary>
An array of integers is given, in which each element represents the length of a side of a triangle. It is necessary to determine the maximum possible perimeter of a triangle made up of sides with lengths from a given array.

Input example:
|Input|Description|
|:-|:-|
|`4`|number of given segments|
|`6 3 3 2`|segment lengths|
|`8`|output|
|||
|`6`|number of given segments|
|`5 3 7 2 8 3`|segment lengths|
|`20`|output|

</details>

_________________________________________________

<details>
<summary>
Wardrobe (<a href="7_wardrobe.py">7_wardrobe.py</a>) 
</summary>
Given a wardrobe with clothes of three colors. Sort your wardrobe by color. First, things should go pink(0), then - yellow(1), and at the end - raspberry(2).

Input example:
|Input|Description|
|:-|:-|
|`7`|overall number of things in wardrobe|
|`0 2 1 2 0 0 1`|given colors of things|
|`0 0 0 1 1 2 2`|output|
|||
|`6`|overall number of things in wardrobe|
|`2 1 1 2 0 2`|given colors of things|
|`0 1 1 2 2 2`|output|

</details>

_________________________________________________

<details>
<summary>
Big number (<a href="8_big_number.py">8_big_number.py</a>) 
</summary>
Numbers are given. It is necessary to determine what is the largest number that can be formed from them.

Input example:
|Input|Description|
|:-|:-|
|`3`|amount of input numbers|
|`15 56 2`|numbers|
|`56215`|output|
|||
|`5`|amount of input numbers|
|`2 4 5 2 10`|numbers|
|`542210`|output|

</details>

_________________________________________________

<details>
<summary>
Conference Lovers (<a href="9_conf_lovers.py">9_conf_lovers.py</a>) 
</summary>
The IT conference was attended by students from different universities from all over the country. For each student, the ID of the university where he studies is known.
From which k universities the largest number of students came to the conference.

Input example:
|Input|Description|
|:-|:-|
|`7`|amount of students|
|`1 2 3 1 2 3 4`|universities IDs|
|`3`|k number|
|`1 2 3`|output|
|||
|`6`|amount of students|
|`1 1 1 2 2 3`|universities IDs|
|`1`|k number|
|`1`|output|

</details>

_________________________________________________

<details>
<summary>
Bubble (<a href="10_bubble.py">10_bubble.py</a>) 
</summary>
Implement a bubble sort algorithm. After each pass through the array, on which some elements are swapped, output its intermediate state.

Input example:
|Input|Description|
|:-|:-|
|`5`|array length|
|`4 3 9 2 1`|array of numbers|
|`3 4 2 1 9`|output|
|`3 2 1 4 9`|output|
|`2 1 3 4 9`|output|
|`1 2 3 4 9`|output|

</details>

_________________________________________________

<details>
<summary>
Merge sort (<a href="11_merge_sort.py">11_merge_sort.py</a>) 
</summary>
You need to implement separately the merge function and the merge_sort function.

* The merge function takes two sorted arrays, merges them into one sorted array, and returns it. If the required signature is merge(array, left, mid, right), then the first array is given as a half-interval [left, mid) array, and the second - a half-interval [mid, right) array.
* The merge_sort function takes some subarray to be sorted. A subarray is defined by a half-interval - its beginning and end. The function must sort the subarray passed to it, it does not return anything.
* The merge_sort function splits a half-interval into two halves and recursively calls the sort separately for each. Then the two sorted arrays are merged into one using merge.

Input example:
"test" function in 11_merge_sort.py file

</details>

_________________________________________________

<details>
<summary>
Two bicycles (<a href="12_two_bicycles.py">12_two_bicycles.py</a>) 
</summary>
There is a piggy bank in which money can be added every day. In the process of accumulation, money is not taken out of the piggy bank. You have information about how much money was in the piggy bank on each day.

Your task is to determine, given the cost of the bicycle,
the first day in which you can buy one bike,
and the first day that two bikes can be bought.

If the required amount was not found in the piggy bank, you need to return -1 instead of the day number.

Hint: the solution should run in O(log n).

Input example:
|Input|Description|
|:-|:-|
|`6`|days number|
|`1 2 4 4 6 8`|money by days|
|`3`|bicycle price|
|`3 5`|output|
|||
|`6`|days number|
|`1 2 4 4 4 4`|money by days|
|`3`|bicycle price|
|`3 -1`|output|

</details>

_________________________________________________

<details>
<summary>
Flowerbeds (<a href="14_flowerbed.py">14_flowerbed.py</a>) 
</summary>
On the diagram of the land plot, flower beds are indicated simply by horizontal segments lying on one straight line. n gardeners were hired for landscaping. Each of them processed some segment on the diagram. The continuous processed segment will then become a flower bed. It is necessary to determine the boundaries of future flower beds.

Input example:
|Input|Description|
|:-|:-|
|`4`|amount of gardeners|
|`7 8`|flowerbed boundaries|
|`7 8`|flowerbed boundaries|
|`2 3`|flowerbed boundaries|
|`6 10`|flowerbed boundaries|
|`2 3`|output|
|`6 10`|output|

</details>

_________________________________________________

<details>
<summary>
Difference of trash indices (<a href="15_trash_index_diff.py">15_trash_index_diff.py</a>) 
</summary>
There is a set of islands. It is necessary to consider all pairs of islands (we recall that there are n * (n-1) / 2 such pairs) and calculate in pairs the difference in areas between all the islands. Now we need to sort the resulting differences in order to take the k-th one in order.

Input example:
|Input|Description|
|:-|:-|
|`3`|amount of islands|
|`2 3 4`|areas of islands|
|`2`|k number|
|`1`|output|
|||
|`3`|amount of islands|
|`1 3 5`|areas of islands|
|`3`|k number|
|`4`|output|

</details>

_________________________________________________

<details>
<summary>
Partial sort (<a href="16_partial_sort.py">16_partial_sort.py</a>) 
</summary>
The sorting algorithm consists of three steps:

* Split the original sequence into k blocks B1, …, Bk. Blocks can have different sizes. If block size i is si, then B1 ={ a1, …, as1 }, B2 = { as1 + 1, … , as1 + s2 } and so on.
* Sort each of the blocks.
* Merge blocks - write first the sorted block B1, then B2, ... , Bk.

Partial sorting is better than normal sorting if, in the first paragraph, we can break the sequence into a large number of blocks. However, not every such partition is suitable. Determine the maximum number of blocks into which the original sequence can be divided in order for the sort to work correctly.

Input example:
|Input|Description|
|:-|:-|
|`4`|amount of numbers|
|`0 1 3 2`|numbers|
|`3`|output|
|||
|`8`|amount of numbers|
|`3 6 7 4 1 5 0 2`|numbers|
|`1`|output|

</details>

_________________________________________________
_________________________________________________

## Final tasks

<details>
<summary>
Search in a broken array (<a href="final_tasks_2/broken_array_search.py">broken_array_search.py</a>) 
</summary>
Given an array of numbers in a ring buffer. The array was sorted in ascending order, and it was possible to find an element in it in logarithmic time. The data from the ring buffer was copied into a regular array, while the data of the original sorted sequence was shifted. Now the array is not sorted. However, it is necessary to provide the ability to find an element in it in O(logn).

It can be assumed that the array contains only unique elements.

Note that you do not need to read data and output a response.

Input example:
|Input|Description|
|:-|:-|
|`9`|n - array length|
|`5`|k - element to find|
|`19 21 100 101 1 4 5 7 12`|array numbers|
|`6`|output (element index)|
|||
|`2`|n - array length|
|`1`|k - element to find|
|`5 1`|array numbers|
|`1`|output (element index)|

</details>

_________________________________________________

<details>
<summary>
Efficient Quicksort (<a href="final_tasks_2/effective_quick_sort.py">effective_quick_sort.py</a>) 
</summary>
Sort the results table as follows: when comparing two participants, the one with more problems solved will go higher. If the number of solved problems is equal, the participant with the lowest penalty goes first. If the penalties are the same, then the first one will be the one whose login comes earlier in alphabetical (lexicographical) order.

As in the case of normal quicksort, which uses additional memory, you need to select a pivot element (eng. pivot), and then reorder the array. Let's make it so that at first there are elements that do not exceed the pivot, and then - greater than the pivot.

The sort is then called recursively on the two resulting parts. It is at the stage of dividing elements into groups in the usual algorithm that additional memory is used.

Input example:
|Input|Description|
|:-|:-|
|`5`|n - number of participants|
|`alla 4 100`|participant name, problems solved, penalty|
|`gena 6 1000`|participant name, problems solved, penalty|
|`gosha 2 90`|participant name, problems solved, penalty|
|`rita 2 90`|participant name, problems solved, penalty|
|`timofey 4 80`|participant name, problems solved, penalty|
|`gena`|output|
|`timofey`|output|
|`alla`|output|
|`gosha`|output|
|`rita`|output|

</details>