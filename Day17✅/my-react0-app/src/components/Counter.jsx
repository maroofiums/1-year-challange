import React, { useState } from 'react'

const [count, setCount] = useState(0)
const Counter = () => {
  return (
    <div>
        <h1>Count: {count}</h1>
        <button onClick={()=>{setCount(count+1)}}>Increace</button>
        <button onClick={()=>{setCount(count-1)}}>Decreace</button>
    </div>
  )
}

export default Counter