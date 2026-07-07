# Day 5 Summary: NumPy + pandas 数据处理 Pipeline

## 今日目标

今天完成了一个小型数据处理 pipeline：读取学生成绩 CSV，检查缺失值，用平均值填补缺失值，计算每个学生的平均分，根据平均分生成等级，并保存清洗后的 CSV 文件。

## 今日新掌握的知识点

1. `Path(__file__).resolve().parents[1]` 可以找到项目根目录
2. `pd.read_csv()` 可以读取 CSV 文件
3. `DataFrame` 可以理解为 pandas 里的表格
4. `df.isna().sum()` 可以检查每一列的缺失值数量
5. `df[column].mean()` 可以计算某一列的平均值
6. `fillna()` 可以填补缺失值
7. `mean(axis=1)` 可以按行计算平均值
8. `np.where()` 可以批量进行条件判断
9. `to_csv()` 可以把处理后的表格保存成 CSV 文件

## 今日完成内容

今天创建并完成了：

```text
src/day05_data_pipeline.py