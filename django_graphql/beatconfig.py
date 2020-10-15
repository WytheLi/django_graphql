from datetime import timedelta


BEAT_SCHEDULE = {
    'testing-print': [
        {
            # 将调用PrintConsumer的test_print方法
            'type': 'test.print',
            # 将消息传递给消费者
            'message': {'testing': 'one'},
            # 定时每5秒
            'schedule': timedelta(seconds=5)
        },
        {
            'type': 'test.print',
            'message': {'testing': 'two'},
            # 精准的在星期一凌晨三点
            # * * * * *
            # M H D m w
            # 分 时 天 月 星期
            'schedule': '0 3 * * 1'
        }
    ]
}