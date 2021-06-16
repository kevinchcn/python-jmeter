# python-jmeter

这是一个Flask小程序，只是简单的生成jmxfile，你可以灵活的使用，不用再依赖人工操作GUI生成

启动该程序 python app.py
向本地接口 http://127.0.0.1:5000/api/gjmx 发送POST请求, 请求内容在app.py中有模板，是一个json
python-jmeter会通过模板中的模板jmx生成一个你需要的jmxfile
