# Leetcode刷题记录

## 01.两数之和

两数之和是leetcode的第一题，该题目比较简单，转换一下思路，遍历数组，用target 减去一个数，得到结果，遍历数组，找到这个结果，返回索引位置即可。

## 02.两数相加

两数相加是一个中等的题，这个题的难点有两点
- 链表是逆序方式存储。
- 两个非空的链表的长度可能不一致。

知道这两个难点之后，就可以着手解决问题，链表问题通常的解决方式是设置一个虚拟头节点dummy，令其指向head，再令p=dummy，对p进行操作，保存dummy的不变。

此题目中，设置target为虚拟头节点。

设置flag判断是否进位。

## 03.无重复字符的最长字串

无重复字符的最长字串
- 首先要判断字符串是否为空串。
- 题目的思路是滑动窗口

滑动窗口其实就是一个队列，比如例题中的 `abcabcbb` ,进入这个队列（窗口）为`abc`满足题目要求，当再进入`a`，队列变成了`abca`，这时候就不满足要求。我们就滑动这个队列。

如何滑动？我们只要吧队列的左边元素移除，直到再次满足题目要求。
这里的队列表示使用Python中的set()集合，set集合的特点是集合元素不能重复且集合元素不可变。

定义两个值，一个记录当前滑动窗口长度，一个记录最大滑动窗口长度，比较之后即可得出结果。

## 05.最长回文子串

什么是回文串？即正过来读和反过来读相同的字符串，例如`abba`,`abccba`等，当然，单个字符一定是回文串。

这个题目使用动态规划的方法进行解决。

什么是动态规划？
- 动态规划，(dynamic programming)简称DP算法。是一种求解决策过程最优化的数学方法。它把多阶段过程转化为一系列单阶段问题（其实就是将一个大问题分成数个小问题），利用各阶段之间的关系进行逐个求解。

动态规划常分两步：
1. 定义“状态”
2. 找到“状态转移方程”
---
1. 定义“状态”，这里“状态”数组是二位数组
   
即定义一个二维数组dp,`dp[l][r]`的值表示子串`s[l,r]`(包含区间左右端点)是否构成回文串，如果子串`s[l,r]`是回文串，那么
`dp[l][r] = True`。

2. 找到“状态转移方程”
   
这是动态规划中关键的一步，我们需要找到各个子问题之间的联系，以本题为例。

我们首先清楚一个事实。

> 1、当子串只包含1个字符，那么它一定是回文串。
>
> 2、当子串包含2个以上的字符时：如果`s[l,r]`是回文串，例如:`abccba`,那么这个回文串两边各往里面收缩一个字符的子串`s[l+1,r-1]`也一定是回文串，即：如果`dp[l][r] == True`成立，那么,`while abs(l-r) > 2 `,`dp[l+1][r-1] = True`.

了解上述事实之后，我们就可以知道，给出一个子串`s[l,r]`，如果`s[l]!=s[r]`,那么`dp[l][r]=False`,如果`s[l] == s[r]`,那么我们就需要判断下一个`s[l+1]`与`s[r-1]`。

在这里我们继续考虑边界情况：即“原字符串去掉左右边界”的子串情况。

> 1. 当原字符的元素个数为3个时，如果左右边界相等，那么去掉它们后，只剩一个字符，一个字符一定是回文串，所以原字符串一定是回文串。
>
> 2. 当原字符串的个数为2个时，如果左右边界相等，那么去掉后，没有字符，故原字符串一定是回文串。

归纳一下，就是只要`s[l+1,r-1]`至少包含两个元素，就继续判断。至少包含两个元素，等价于`l+1<r-1`，即`l - r < -2 or r - l > 2`。

综上，如果一个字符串的左右边界相等，一下二者之一成立即可：

1. 去掉左右边界后的字符串不具有两个以上字符，即“`s[l+1,r-1]`至少包含两个元素”的反，即`l - r >= -2 or r - l <= 2`。
2. 去掉左右边界后的字符串时回文串。

整理成“状态转移方程”：
`dp[l][r] = (s[l] == s[r] and (l-r >= -2 or dp[l+1][r-1]))`

或者

`dp[l][r] = (s[l] == s[r] and (r - l <= 2 or dp[l+1][r-1]))`

编程技巧，r从1到`len(str)`, l从0到r,固定r不动，移动l判断

## 06.Z字形变换

Z字形变换较为简单，首先生成行数个空列表，即`s = [''] * numRows`,之后按列进行插入即可。

columns :列

rows：行