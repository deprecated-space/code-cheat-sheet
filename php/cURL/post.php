<?php
  $cookie = ".CNBlogsCookie=xxxxx";

  // http://www.cnblogs.com/zichi/p/5926346.html 评论
  $postData = 'blogApp=zichi&postId=5926346&body=cURLtest';

  // 也可以写成数组形式，比较直观
  /*
  $postData = array(
    'blogApp' => 'zichi',
    'postId' = > '5926346',
    'body' => 'test'
  );
  */


  // 初始化一个 cURL 对象
  $curl = curl_init();

  // cookie
  curl_setopt($curl, CURLOPT_COOKIE, $cookie);

  // 如果有多个请求头，可以用 CURLOPT_HTTPHEADER 设置
  // $headers = array('Cookie: ' . $cookie);
  // curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);

  // 设置爬取网页的URL
  curl_setopt($curl, CURLOPT_URL, "http://www.cnblogs.com/mvc/PostComment/Add.aspx");

  // 执行 curl_exec() 之后不立即打印
  // 如果后续需要对抓取内容进行解析的话，一般都需要这一句
  curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);

  // POST 设置
  curl_setopt($curl, CURLOPT_POST, 1);
  curl_setopt($curl, CURLOPT_POSTFIELDS, $postData);

  // 执行
  $html = curl_exec($curl);

  var_dump(curl_error($curl));

  // 关闭 cURL 对话
  curl_close($curl);
?>