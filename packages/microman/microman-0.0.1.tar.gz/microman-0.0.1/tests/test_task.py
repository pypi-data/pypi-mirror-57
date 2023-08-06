from microman import task, Task


def test_decorator():

  @task
  def task_with_no_args():
    pass

  task_with_no_args()
  assert isinstance(
    task_with_no_args, Task
  ), 'task decorator should return an instance of Task'
  assert task_with_no_args.name == 'task_with_no_args'

  @task()
  def task_with_empty_args():
    """
    this is a description
    """
    pass

  task_with_empty_args()
  assert isinstance(
    task_with_empty_args, Task
  ), 'task decorator should return an instance of Task'
  assert 'this is a description' in task_with_empty_args.description

  @task(name='foo')
  def task_with_different_name():
    pass

  task_with_different_name()
  assert isinstance(
    task_with_different_name, Task
  ), 'task decorator should return an instance of Task'

  assert task_with_different_name.name == 'foo'

  assert len(task_with_different_name.runs) == 1
