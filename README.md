# showmethecode
* 项目地址：https://github.com/Show-Me-the-Code/show-me-the-code
* 此仓库只作为自己平时刷题记录
* 会记录一些算法思想和题解方法

## 极客时间－数据结构与算法之美

### 数组

数组看起来简单基础，但是很多人没有理解这个数据结构的精髓。带着为什么数组要从0开始编号，而不是从1开始的问题，进入主题。

#### **数组如何实现随机访问**

1.  数组是一种**线性表**数据结构，用**连续的存储空间存储相同类型数据**

   - 线性表：数组、链表、队列、栈 
   - 非线性表：树 图
   - 连续的内存空间、相同的数据，所以数组可以随机访问，但对数组进行删除插入，为了保证数组的连续性，就要做大量的数据搬移工

2. 数组如何实现下标随机访问

   * 引入数组在内存中的分配图，得出寻址公式

   * 一维数组：`a[k]_address = base_address + k * type_size`

   * 二维数组：对于 m * n 的数组，a [ i ][ j ] (i < m,j < n)的地址为：

     `address = base_address + ( i * n + j) * type_size`

   *  纠正数组和链表的错误认识。数组的查找操作时间复杂度并不是O(1)。即便是排好的数组，用二分查找，时间复杂度也是O（logn）。
     正确表述：数组支持随机访问，根据下标随机访问的时间复杂度为O（1）

3. 低效的插入和删除

   * 插入：插入最后最好O(1)，插入开头 最坏O(n) ，平均O(n)
   * 但是数组若无序，插入新的元素时，可以将第K个位置元素移动到数组末尾，把新的元素，插入到第k个位置，此处复杂度为O(1)。
   * 删除：从最后删除最好O(1) ，从头删除最坏O(n) ，平均O(n)
   * 多次删除集中在一起，提高删除效率
     记录下已经被删除的数据，每次的删除操作并不是搬移数据，只是记录数据已经被删除，当数组没有更多的存储空间时，再触发一次真正的删除操作。即JVM标记清除垃圾回收算法。

4. 警惕数组的访问越界问题
   用C语言循环越界访问的例子说明访问越界的bug。此例在《C陷阱与缺陷》出现过，很惭愧，看过但是现在也只有一丢丢印象。翻了下书，替作者加上一句话：如果用来编译这段程序的编译器按照内存地址递减的方式给变量分配内存，那么内存中的i将会被置为0，则为死循环永远出不去。

5. 容器能否完全替代数组
   相比于数字，java中的ArrayList封装了数组的很多操作，并支持动态扩容。但一旦超过存储容量，扩容时比较耗内存，因为涉及到内存申请和数据搬移。
   数组适合的场景：
   1）    Java ArrayList 的使用涉及装箱拆箱，有一定的性能损耗，如果特别关注性能，可以考虑数组
   2）    若数据大小事先已知，并且涉及的数据操作非常简单，可以使用数组
   3）    表示多维数组时，数组往往更加直观。
   4）    业务开发容器即可；底层开发，如网络框架，性能优化，选择数组。

6. 解答开篇问题
   1）    从偏移角度理解a[0] ，0实际为偏移量，如果从1计数，a[k]的内存地址变为`a[k]_address = base_address + (k-1)*type_size`，会多出K-1。增加cpu负担。
   2）    也有一定的历史原因

