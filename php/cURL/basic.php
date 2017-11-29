<?php
  // 初始化一个 cURL 对象
  $curl = curl_init();

  // 设置爬取网页的URL
  curl_setopt($curl, CURLOPT_URL, "http://www.sina.com");

  // 执行 curl_exec() 之后不立即打印
  // 如果后续需要对抓取内容进行解析的话，一般都需要这一句
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

  // UA
  curl_setopt($curl, CURLOPT_USERAGENT, $_SERVER['HTTP_USER_AGENT']);

  // 抓取 HTTPS 的网页
  // curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, FALSE);


  // 执行
  $html = curl_exec($curl);

  // 打印错误
  // 比如抓取 HTTPS 的网页，如果没加上那句，就会报错
  // SSL certificate problem, verify that the CA cert is OK. Details:
  // error:14090086:SSL routines:SSL3_GET_SERVER_CERTIFICATE:certificate verify failed
  // 写在 curl_exec 后，curl_close 前
  var_dump(curl_error($curl));


  // 关闭 cURL 对话
  curl_close($curl);


  // 打印抓取的内容
  // 后续可以对该字符串进行解析
  var_dump($html);
?>