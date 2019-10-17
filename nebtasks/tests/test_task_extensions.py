class TestTaskExtensions:
    def test_echo_task(self, datadir, monkeypatch, invoker):
        from nebtasks.task_extensions import neb_task, NebTask
        from nebu.cli.main import cli

        @neb_task(cli, name='test_echo_task')
        def test_echo_task():
            """echo back collection/module ids"""

            def collection_action(id, file, resources):
                print(id)

            def module_action(id, file, resources):
                print(id)

            return NebTask(
                collection_action=collection_action,
                module_action=module_action)

        path = datadir / 'collection'
        monkeypatch.chdir('/tmp')

        args = ['test_echo_task', str(path)]
        result = invoker(cli, args)

        assert result.exit_code == 0

        expected_results = set([
            'col11405',
            'm40645',
            'm37151',
            'm37217',
            'm37386',
            'm40643',
            'm42302',
            'm37154',
            'm37152',
            'm42304',
            'm42303',
            'm40646'
        ])

        actual_results = set(result.output.split('\n'))
        actual_results.remove('')

        assert len(actual_results.difference(expected_results)) == 0

    def test_invalid_task(self, datadir, monkeypatch, invoker):
        from nebtasks.task_extensions import neb_task
        from nebu.cli.main import cli

        @neb_task(cli, name='test_invalid_echo_task')
        def test_invalid_echo_task():
            """echo back collection id"""

            def collection_action(id, file, resources):
                print(id)

            def module_action(id, file, resources):
                print(id)

            return 5

        path = datadir / 'collection'
        monkeypatch.chdir('/tmp')

        args = ['test_invalid_echo_task', str(path)]
        result = invoker(cli, args)

        assert result.exit_code == 1
        error_msg = 'Task test_invalid_echo_task returns int not NebTask'
        assert str(result.exception) == error_msg
