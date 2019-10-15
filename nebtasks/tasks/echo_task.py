from nebu.cli.task_extensions import neb_task, NebTask

@neb_task(name='echo-task')
def echo_task():
    """echo back collection/module ids"""

    def collection_action(id, file, resources):
        print(id)

    def module_action(id, file, resources):
        print(id)

    return NebTask(
        collection_action=collection_action,
        module_action=module_action)
