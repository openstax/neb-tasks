from nebu.cli.task_extensions import neb_task, NebTask

@neb_task(name='test_ext')
def test_ext():
    return NebTask()
