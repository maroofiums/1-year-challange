import React, { useState } from 'react'
import Counter from './components/Counter'
import Button from './components/Button'

const App = () => {
    const [count, setCount] = useState(0);
  const handleIncrement = () => setCount(count + 1);
  const handleDecrement = () => setCount(count - 1);
  return (
    <div>
      <h1>React Counter App</h1>
      <Counter value={count}/>
      <Button label="Increment" onClick={handleIncrement}/>
      <Button label="Decrement" onClick={handleDecrement}/>
    </div>
  )
}

export default App