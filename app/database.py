from app import db

def fetch_todo() -> dict:
	conn = db.connect()
	query_results = conn.execute("SELECT * FROM tasks;").fetchall()
	conn.close()
	todo_list = []
	for result in query_results:
		item = {
			"id": result[0],
			"task": result[1],
			"status":result[2]
		}
		todo_list.append(item)

	return todo_list


def update_task_entry(task_id: int, text: str) -> None:
    conn = db.connect()
    query = 'UPDATE tasks SET task = "{}" WHERE id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()

def update_status_entry(task_id: int, text: str) -> None:
    conn = db.connect()
    query = 'UPDATE tasks SET status = "{}" WHERE id = {};'.format(text, task_id)
    conn.execute(query)
    conn.close()


def insert_new_task(text: str) ->  int:
    conn = db.connect()
    query = 'INSERT INTO tasks (task, status) VALUES ("{}", "{}");'.format(text, "Todo")
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

    return task_id


def remove_task_by_id(task_id: int) -> None:
    conn = db.connect()
    query = 'DELETE FROM tasks WHERE id={};'.format(task_id)
    conn.execute(query)
    conn.close()