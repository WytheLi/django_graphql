from datetime import timedelta


BEAT_SCHEDULE = {
    'testing-print': [
        {
            # 将调用PrintConsumer的test_print方法
            'type': 'test.print',
            # 将消息传递给消费者
            'message': {'pushData': 'common data...', 'group': group},
            # 定时每5秒
            'schedule': timedelta(seconds=5)
        } for group in ['group01', 'group02', 'group03']
    ]
}

BEAT_SCHEDULE['testing-print'].append(
    {
        'type': 'test.print',
        'message': {'pushData': '这条消息指定给group01', 'group': 'group01'},
        # 精准的在星期一凌晨三点
        # * * * * *
        # M H D m w
        # 分 时 天 月 星期
        'schedule': '0 3 * * 1'
    }
)

BEAT_SCHEDULE['testing-print'].append(
    {
        'type': 'test.print',
        'message': {'pushData': '这条消息指定给group02', 'group': 'group02'},
        'schedule': timedelta(seconds=3)
    }
)