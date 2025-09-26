# Assignment #1: 虚拟机，Shell & 大语言模型

Updated 1745 GMT+8 Sep 8, 2025

2025 fall, Complied by 韩滨羽



**作业的各项评分细则及对应的得分**

| 标准                                 | 等级                                                         | 得分 |
| ------------------------------------ | ------------------------------------------------------------ | ---- |
| 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
| 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分 | 1 分 |
| AC代码截图                           | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分 | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
| 总得分： 5                           | 总分满分：5分                                                |      |
>
>
>
>**说明：**
>
>1. **解题与记录：**
>
>      对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. **课程平台：**课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在<mark>第2周</mark>选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
>
>3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>3. **延迟提交：****如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。



## 1. 题目

### E27653: Fraction类

http://cs101.openjudge.cn/pctbook/E27653/

请练习用OOP方式实现。

思路：

- 花费约30min

代码：

```python
import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

        self._simplify()

    def _simplify(self):
        #化简分数
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd

        if self.denominator < 0 :
            self.denominator *= -1
            self.numerator *= -1

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)
    
    def __str__(self):
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator}/{self.denominator}"
    
a, b, c, d = map(int, input().split())
f1 = Fraction(a, b)
f2 = Fraction(c, d)
print(f1 + f2)
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-09-09 上午10.44.40](/Users/hanbinyu/Library/Application Support/typora-user-images/截屏2025-09-09 上午10.44.40.png)



### M1760.袋子里最少数目的球

binary search, https://leetcode.cn/problems/minimum-limit-of-balls-in-a-bag/


思路：

- 花费约40min

代码：

```python
def bs(nums, maxOperations):
    l = 1
    r = max(nums)
    ans = 0
    while l <= r :
        mid = (l + r) // 2
        ops = sum((x - 1) // mid for x in nums)
        if ops > maxOperations:
            l = mid + 1 #在[mid + 1, r]中
        else:
            r = mid - 1 #在[l, mid - 1]中找
    return l

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        ans = bs(nums, maxOperations)
        return ans
        
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-09-09 下午12.55.27](/Users/hanbinyu/Library/Application Support/typora-user-images/截屏2025-09-09 下午12.55.27.png)



### M04135: 月度开销

binary search, http://cs101.openjudge.cn/pctbook/M04135/



思路：

- 花费约15min

代码：

```python
def binary_search(m_period, nums):
    r = sum(nums)
    l = max(nums)
    while l <= r:
        mid = (l + r) // 2
        tmp = 0
        cnt = 1
        for i in nums:
            tmp += i
            if tmp > mid :
                cnt += 1
                tmp = i
            if cnt > m_period:
                break
        if cnt > m_period:
            l = mid + 1
        else:
            r = mid - 1
    return l

n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]
print(binary_search(m, nums))
```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-09-09 下午1.33.05](/Users/hanbinyu/Library/Application Support/typora-user-images/截屏2025-09-09 下午1.33.05.png)

### M27300: 模型整理

sortings, AI, http://cs101.openjudge.cn/pctbook/M27300/



思路：

- 耗时50min

代码：

```python
n = int(input())
ans = {}

for i in range(n):
    m = input()
    name, size = m.split("-")
    if name in ans:
        ans[name].append(size)
    else:
        ans[name] = [size]

for k in sorted(ans.keys()):
    v = ans[k]
    m_list = []
    b_list = []
    for i in v:
        if i.endswith("B"):
            b_list.append(i)
        else:
            m_list.append(i)
    
    m_list.sort(key=lambda x: float(x[:-1]))
    b_list.sort(key=lambda x: float(x[:-1]))
    
    v_sorted = m_list + b_list
    print(f"{k}: {', '.join(v_sorted)}")

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>

![截屏2025-09-09 下午2.13.32](/Users/hanbinyu/Library/Application Support/typora-user-images/截屏2025-09-09 下午2.13.32.png)



### Q5. 熟悉云虚拟机Linux环境与大语言模型（LLM）本地部署

本项目包括两个任务：

1）通过云虚拟机（如 https://clab.pku.edu.cn/ 提供的资源）熟悉Linux系统操作环境。

2）完成大语言模型（LLM）的本地部署与功能测试。

LLM 部署可选择使用图形化工具（如 LM Studio, https://lmstudio.ai）以简化配置流程，提升部署效率。部署完成后，需对模型进行实际能力测试。

测试内容包括：从主流在线编程评测平台（如 OpenJudge、Codeforces、LeetCode 或洛谷等）选取若干编程题目，提交由本地部署的 LLM 生成的代码解决方案，并确保其能够通过全部测试用例，获得“Accepted”状态。选题时应避免与已知可被 AI 正确解答的题目重复。当前已确认可通过的 AI 解题列表可参考以下 GitHub 仓库： 

https://github.com/GMyhf/2025spring-cs201/blob/main/AI_accepted_locally.md



请提供你的项目进展，内容应该包括：关键操作步骤的截图以及遇到的技术问题及相应的解决方法。这将有助于全面掌握项目推进情况，并为后续优化与扩展提供依据。





### Q6. 阅读《Build a Large Language Model (From Scratch)》第一章

作者：Sebastian Raschka

请整理你的学习笔记。这应该包括但不限于对第一章核心概念的理解、关键术语的解析、学习过程中的思考与启发，以及尚存的疑问与反思。通过系统梳理，不仅有助于巩固自身理解，也希望为其他学习者提供有价值的参考。





## 2. 学习总结和个人收获

- OOP:

  - 实例方法运用self.fraction()	

  - 调用非实例方法fraction(self)

  - 第一个self是实例，其他的参数可以是实例，也可以不是

- binary
  - 最小化最大值的思想


- 回溯
  - 







