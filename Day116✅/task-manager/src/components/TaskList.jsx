import { useContext } from "react";
import { TaskContext } from "../context/TaskContext";

const TaskList = () => {
  const { tasks, dispatch } = useContext(TaskContext);

  if (tasks.length === 0) return <p>No tasks yet!</p>;

  return (
    <ul>
      {tasks.map((task) => (
        <li key={task.id}>
          {task.text}
          <button onClick={() => dispatch({ type: "DELETE_TASK", payload: task.id })}>
            ❌
          </button>
        </li>
      ))}
    </ul>
  );
};

export default TaskList;
