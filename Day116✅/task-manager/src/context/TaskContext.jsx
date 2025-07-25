import { createContext, useReducer } from "react";
import { useLocalStorage } from "../hooks/useLocalStorage";

export const TaskContext = createContext();

const taskReducer = (state, action) => {
  switch (action.type) {
    case "ADD_TASK":
      return [...state, { id: Date.now(), text: action.payload }];
    case "DELETE_TASK":
      return state.filter((task) => task.id !== action.payload);
    default:
      return state;
  }
};

export const TaskProvider = ({ children }) => {
  const [storedTasks, setStoredTasks] = useLocalStorage("tasks", []);
  const [tasks, dispatchBase] = useReducer(taskReducer, storedTasks);

  const dispatch = (action) => {
    const updated = taskReducer(tasks, action);
    setStoredTasks(updated);
    dispatchBase(action);
  };

  return (
    <TaskContext.Provider value={{ tasks, dispatch }}>
      {children}
    </TaskContext.Provider>
  );
};
