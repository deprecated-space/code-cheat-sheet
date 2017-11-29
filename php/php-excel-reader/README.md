## php-excel-reader

Code from <https://code.google.com/archive/p/php-excel-reader/> 或者 <https://sourceforge.net/projects/phpexcelreader/>

~~貌似~~只能解析 `.xls` 文件，不能解析 `.xlsx` 文件。

- <https://github.com/hanzichi/practice/blob/master/2016/php-excel-reader/example.php>（php-excel-reader 库解析 .xls 文件）
- <https://github.com/hanzichi/practice/blob/master/2016/php-excel-reader/example2.php>（php-excel-reader 库解析 .xls 文件）

## excel to csv 

如果 **上传文件可控**，直接把 Excel 文件另存为 `.csv` 文件（直接可用文本编辑器打开 ），然后用 `file_get_contents` 方法处理下就好了 ，或者 PHP 还有自带的解析 `.csv` 文件的函数 `fgetcsv`

- <https://github.com/hanzichi/practice/blob/master/2016/php-excel-reader/example3.php>（file_get_contents 解析 .csv 文件）
- <https://github.com/hanzichi/practice/blob/master/2016/php-excel-reader/example4.php>（fgetcsv 解析 .csv 文件）

## PHPExcel

如果需要更多功能的话，推荐更为强大的 Excel 解析库 <https://github.com/PHPOffice/PHPExcel> 官网 <http://phpexcel.codeplex.com/>
